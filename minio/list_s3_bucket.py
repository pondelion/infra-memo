import boto3
from boto3.session import Session

s3_client = boto3.client(
    's3',
    aws_access_key_id='minio_root',
    aws_secret_access_key='minio_password',
    # region_name='<REGION NAME>',
    endpoint_url='http://127.0.0.1:9000'
)
response = s3_client.list_buckets()

for bucket in response['Buckets']:
    print(f'{bucket["Name"]}')
