import boto3
import os
import json
import urllib.request
from datetime import datetime

# Get Slack webhook URL from environment variables
SLACK_WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL")

# AWS clients
ec2 = boto3.client("ec2")
rds = boto3.client("rds")
s3 = boto3.client("s3")
lambda_client = boto3.client("lambda")
ecs = boto3.client("ecs")
iam = boto3.client("iam")

# Function to send message to Slack
def send_to_slack(blocks):
    payload = {"blocks": blocks}
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        SLACK_WEBHOOK_URL,
        data=data,
        headers={"Content-Type": "application/json"}
    )
    urllib.request.urlopen(req)

# Main Lambda handler
def lambda_handler(event, context):
    # EC2 Instances
    ec2_resp = ec2.describe_instances(
        Filters=[{"Name": "instance-state-name", "Values": ["running"]}]
    )
    ec2_count = sum(len(r["Instances"]) for r in ec2_resp["Reservations"])

    # RDS Instances
    rds_resp = rds.describe_db_instances()
    rds_count = len([db for db in rds_resp["DBInstances"] if db["DBInstanceStatus"] == "available"])

    # S3 Buckets
    s3_count = len(s3.list_buckets()["Buckets"])

    # EBS Volumes
    ebs_resp = ec2.describe_volumes(
        Filters=[{"Name": "status", "Values": ["in-use"]}]
    )
    ebs_count = len(ebs_resp["Volumes"])

    # Lambda Functions
    lambda_count = len(lambda_client.list_functions()["Functions"])

    # VPCs
    vpc_count = len(ec2.describe_vpcs()["Vpcs"])

    # ECS Services
    clusters = ecs.list_clusters()["clusterArns"]
    ecs_services_count = 0
    for cluster in clusters:
        services = ecs.list_services(cluster=cluster)["serviceArns"]
        ecs_services_count += len(services)

    # IAM Users & Roles
    iam_users_count = len(iam.list_users()["Users"])
    iam_roles_count = len(iam.list_roles()["Roles"])

    # Current date
    today = datetime.utcnow().strftime("%Y-%m-%d")

    # Prepare Slack Block message
    blocks = [
        {"type": "header", "text": {"type": "plain_text", "text": "AWS Daily Resource Report"}},
        {"type": "context", "elements": [{"type": "mrkdwn", "text": f"*Date:* {today}"}]},
        {"type": "divider"},
        {
            "type": "section",
            "fields": [
                {"type": "mrkdwn", "text": f"*EC2 Running:*\n{ec2_count}"},
                {"type": "mrkdwn", "text": f"*RDS Running:*\n{rds_count}"}
            ]
        },
        {
            "type": "section",
            "fields": [
                {"type": "mrkdwn", "text": f"*S3 Buckets:*\n{s3_count}"},
                {"type": "mrkdwn", "text": f"*EBS In-use:*\n{ebs_count}"}
            ]
        },
        {
            "type": "section",
            "fields": [
                {"type": "mrkdwn", "text": f"*Lambda Functions:*\n{lambda_count}"},
                {"type": "mrkdwn", "text": f"*VPCs:*\n{vpc_count}"}
            ]
        },
        {
            "type": "section",
            "fields": [
                {"type": "mrkdwn", "text": f"*ECS Services:*\n{ecs_services_count}"},
                {"type": "mrkdwn", "text": f"*IAM Users / Roles:*\n{iam_users_count} / {iam_roles_count}"}
            ]
        }
    ]

    # Send to Slack
    send_to_slack(blocks)

    return {"statusCode": 200, "body": "Slack notification sent successfully"}
