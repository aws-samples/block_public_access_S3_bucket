import json
import boto3

def lambda_handler(event, context):
    # Extract the S3 bucket name from the event
    bucket_name = event['detail']['findings'][0]['Resources'][0]['Details']['AwsS3Bucket']['Name']

    # Create an S3 resource
    s3 = boto3.resource('s3')

    # Get the bucket object
    bucket = s3.Bucket(bucket_name)

    # Get the current public access block configuration
    public_access_block = bucket.PublicAccessBlockConfiguration()

    # Update the public access block configuration
    public_access_block.update(
        BlockPublicAcls=True,
        IgnorePublicAcls=True,
        BlockPublicPolicy=True,
        RestrictPublicBuckets=True
    )

    print(f'Public access blocked for bucket: {bucket_name}')

    return {
        'statusCode': 200,
        'body': json.dumps(f'Public access blocked for bucket: {bucket_name}')
    }