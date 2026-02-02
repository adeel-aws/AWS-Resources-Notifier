# AWS Resource Cost Watcher

**Overview:**  
This project is a **serverless AWS automation** that monitors active AWS resources and sends **daily Slack notifications**. It helps developers and teams **avoid unnecessary cloud costs** by keeping track of running resources that may be forgotten.

**Services Monitored:**
- EC2 instances (running)
- RDS instances (available)
- S3 buckets
- EBS volumes (in-use)
- Lambda functions
- ECS services
- VPCs
- IAM users & roles

**Tools & Services Used:**
- **AWS Lambda** – serverless function to scan resources
- **Amazon EventBridge** – scheduled daily trigger
- **AWS IAM** – permissions for Lambda
- **Slack Incoming Webhook** – notifications
- **Python 3.9+** – Lambda runtime
- **Boto3** – AWS SDK for Python

**Outcome:**  
- Automatically sends a daily Slack report of all active AWS resources
- Helps in cost awareness and quick cleanup of unused resources
- Fully serverless, reusable in any AWS account
