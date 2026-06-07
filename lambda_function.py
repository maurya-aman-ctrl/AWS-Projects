import boto3

ec2 = boto3.client('ec2')
sns = boto3.client('sns')

SNS_TOPIC_ARN = "arn:aws:sns:ap-south-1:780065485778:newtopic"

def lambda_handler(event, context):

    response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'instance-state-name',
                'Values': ['running']
            }
        ]
    )

    stopped_instances = []

    for reservation in response['Reservations']:

        for instance in reservation['Instances']:

            instance_id = instance['InstanceId']

            tags = {
                tag['Key']: tag['Value']
                for tag in instance.get('Tags', [])
            }

            auto_stop = tags.get('AutoStop', '').lower()
            environment = tags.get('Environment', '').lower()

            if auto_stop == 'true' and environment != 'production':

                ec2.stop_instances(
                    InstanceIds=[instance_id]
                )

                stopped_instances.append(instance_id)

    if stopped_instances:

        message = (
            "The following EC2 instances were stopped:\n\n"
            + "\n".join(stopped_instances)
        )

        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="AWS Cost Optimization Alert",
            Message=message
        )

    return {
        "statusCode": 200,
        "stopped": stopped_instances
    }
