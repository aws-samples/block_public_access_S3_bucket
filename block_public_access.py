import json
import logging
import boto3

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def lambda_handler(event, context):
    logger.debug('## EVENT')
    logger.debug(event)
    # Extract the S3 bucket name from the event
    bucket_name = event['detail']['findings'][0]['Resources'][0]['Details']['AwsS3Bucket']['Name']

    # Create an S3 client
    s3 = boto3.client('s3')

    # Block public access configuration for the bucket
    s3.put_public_access_block(
        Bucket=bucket_name,
        PublicAccessBlockConfiguration={
            'BlockPublicAcls': True,
            'IgnorePublicAcls': True,
            'BlockPublicPolicy': True,
            'RestrictPublicBuckets': True
        }
    )

    print(f'Public access blocked for bucket: {bucket_name}')

    return {
        'statusCode': 200,
        'body': json.dumps(f'Public access blocked for bucket: {bucket_name}')
    }
