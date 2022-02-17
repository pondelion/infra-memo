import boto3
from boto3.session import Session

dynamodb_client = boto3.client(
    'dynamodb',
    aws_access_key_id='minio_root',
    aws_secret_access_key='minio_password',
    # region_name='<REGION NAME>',
    endpoint_url='http://127.0.0.1:8000'
)
response = dynamodb_client.list_tables()

print(response)
