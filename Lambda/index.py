import json
import boto3

def lambda_handler(event, context):
    detail = event.get("detail", {})
    user = detail.get("userIdentity", {}).get("userName", "Unknown")

    # Print to logs
    print(f"Unauthorized login attempt detected for user: {user}")

    # Optional: send alert via SNS
    sns = boto3.client('sns')
    sns.publish(
        TopicArn='arn:aws:sns:us-east-1:263846838953:FailedLoginAlerts',
        Subject='ALERT: Failed Console Login',
        Message=f"User {user} had a failed login without MFA."
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Alert sent')
    }
