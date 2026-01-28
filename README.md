# AWS IAM User Onboarding Automation

A Python automation script using Boto3 to provision AWS IAM users, groups, and login profiles based on HR data from a CSV file.

## Features
- **Idempotent Design:** Handles existing users/groups gracefully without crashing.
- **Best Practices:** Enforces password reset on first login.
- **Automated Grouping:** Assigns users to IAM groups based on their department.

## Tech Stack
- Python 3.12
- AWS SDK for Python (Boto3)
- AWS IAM

## Validation
Successfully provisioned users and groups in the AWS Console:

### Users Created
<img width="1080" height="455" alt="image" src="https://github.com/user-attachments/assets/fdde339c-c249-4203-a01b-390da2e55c47" />

### Groups Assigned
<img width="1899" height="791" alt="image" src="https://github.com/user-attachments/assets/6d1b9aa7-7bbb-42c4-bb2b-6a59a4d084ae" />
