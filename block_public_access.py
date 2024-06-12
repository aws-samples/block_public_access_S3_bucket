import json
import logging
import boto3

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Create an S3 client
s3 = boto3.client('s3')

def lambda_handler(event, context):
    logger.debug('## EVENT')
    logger.debug(event)
    
    try:
        # Extract the S3 bucket name from the event
        bucket_name = event['detail']['findings'][0]['Resources'][0]['Details']['AwsS3Bucket']['Name']

        # Check if the bucket name is not None
        if bucket_name is not None:
            # Check if the bucket has the specified tag
            bucket_tag_key = "bucket.status"
            bucket_tag_value = "public.bucket"
            
            # Get the bucket tagging
            response = s3.get_bucket_tagging(Bucket=bucket_name)
            tags = response['TagSet']
            
            # Check if the specified tag is present
            tag_found = False
            for tag in tags:
                if tag['Key'] == bucket_tag_key and tag['Value'] == bucket_tag_value:
                    tag_found = True
                    break
            
            # If the tag is not found, block public access
            if not tag_found:
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
            else:
                print(f'Bucket {bucket_name} has the required tag, skipping public access block.')
    except Exception as e:
        logger.error(f'Error occurred: {str(e)}')
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error occurred: {str(e)}')
        }

    return {
        'statusCode': 200,
        'body': json.dumps(f'Public access blocked for bucket: {bucket_name}')
    }
