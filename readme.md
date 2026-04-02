# 🚀 AWS Resource Cost Watcher

A **serverless AWS monitoring solution** that tracks active cloud resources and sends **automated daily Slack notifications** to help prevent unnecessary cloud costs.

---

## 📌 Overview

Managing cloud resources manually often leads to **forgotten running services** and unexpected billing.

This project provides an **automated, serverless cost-awareness system** that scans AWS resources daily and reports them directly to Slack — enabling quick visibility and cleanup.

---

## 🎯 Key Features

* 🔍 **Automated Resource Discovery**
* 📊 **Daily Cost Awareness Reports**
* 💬 **Slack Integration for Real-time Alerts**
* ⚡ **Fully Serverless Architecture**
* 🔁 **Scheduled Execution via EventBridge**
* ♻️ **Reusable Across Multiple AWS Accounts**

---

## 🧰 Services Monitored

* 🖥️ EC2 instances (running)
* 🗄️ RDS instances (available)
* 🪣 S3 buckets
* 💾 EBS volumes (in-use)
* ⚡ Lambda functions
* 📦 ECS services
* 🌐 VPCs
* 🔐 IAM users & roles

---

## 🏗️ Architecture

```id="arch-diagram-01"
EventBridge (Schedule)
        │
        ▼
   AWS Lambda
        │
        ▼
   Boto3 (Scan Resources)
        │
        ▼
   Slack Webhook Notification
```

---

## ⚙️ Tech Stack

* **AWS Lambda** – Serverless compute
* **Amazon EventBridge** – Scheduled trigger
* **AWS IAM** – Secure permissions
* **Slack Webhook** – Notifications
* **Python 3.9+**
* **Boto3 (AWS SDK)**

---

## 🔄 Workflow

1. EventBridge triggers Lambda **daily**
2. Lambda scans AWS resources using **Boto3**
3. Filters active/running resources
4. Formats a structured report
5. Sends notification to **Slack channel**

---

## 📸 Sample Output (Slack)

```id="sample-output-01"
📊 AWS Resource Report

EC2: 3 running instances  
RDS: 1 active instance  
S3: 5 buckets  
EBS: 2 volumes in use  
...
```

---

## 🎯 Use Cases

* 💰 Avoid unexpected AWS billing
* 🧹 Identify unused resources quickly
* 👨‍💻 Daily visibility for DevOps teams
* 🏢 Cost monitoring for startups & small teams

---

## 🚀 Setup Instructions

1. Create a **Slack Incoming Webhook**
2. Deploy Lambda function with required IAM role
3. Add EventBridge rule (daily schedule)
4. Configure environment variables (Webhook URL)
5. Deploy and monitor Slack notifications

---

## 💡 Future Enhancements

* 💸 Cost estimation per resource
* 📈 Weekly & monthly reports
* 📊 Dashboard integration (CloudWatch / Grafana)
* 🔔 Multi-channel alerts (Email, Teams)
* 🧠 AI-based cost optimization suggestions

---

## 🏆 Outcome

* ✅ Improved cost visibility
* ✅ Reduced unused resource waste
* ✅ Fully automated monitoring system
* ✅ Scalable & reusable architecture

---

## 👨‍💻 Author

**Muhammad Adeel**
AWS Certified Cloud Practitioner | Aspiring DevOps Engineer 🚀
