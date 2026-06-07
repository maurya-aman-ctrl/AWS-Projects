# Smart EC2 Cost Optimizer

## Project Overview

A serverless AWS cost optimization solution that automatically identifies and stops non-production EC2 instances based on tags. The solution uses AWS Lambda, EventBridge, SNS, IAM, and EC2.

## Architecture

EventBridge → Lambda → EC2 + SNS

1. EventBridge triggers Lambda on a schedule.
2. Lambda checks all running EC2 instances.
3. Lambda reads instance tags.
4. Instances with:
   * AutoStop=true
   * Environment not equal to Production
     are automatically stopped.
5. SNS sends an email notification when instances are stopped.

## AWS Services Used

* AWS Lambda
* Amazon EC2
* Amazon SNS
* Amazon EventBridge
* AWS IAM role
* Amazon CloudWatch

## Tags Used

Key          Value 
AutoStop     true  
Environment  Dev   

## Lambda Logic

1. Retrieve running EC2 instances.
2. Read instance tags.
3. Filter instances using:
   * AutoStop=true
   * Environment != Production
4. Stop matching instances.
5. Publish SNS notification.

## Benefits

* Reduces unnecessary EC2 costs.
* Protects production instances.
* Fully automated.
* Serverless architecture.

## Future Enhancements

* Auto-start instances in the morning.
* Slack notifications.
* Cost reporting dashboard.
* Environment-specific schedules.

## Project Outcome
- Successfully identified running EC2 instances using AWS Lambda
- Automatically stopped non-production instances using tags
- Integrated Amazon SNS for email notifications
- Automated execution using Amazon EventBridge
- Used CloudWatch Logs for monitoring and troubleshooting

## Author
Aman Verma
AWS Cloud Projects Portfolio
