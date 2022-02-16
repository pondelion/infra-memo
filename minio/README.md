

## Start minio server

```bash
$ sudo docker-compose up -d
```

```bash
$ sudo docker container logs minio
API: http://192.168.144.2:9999  http://127.0.0.1:9999 
RootUser: minio_root 
RootPass: minio_password 

Console: http://192.168.144.2:9001 http://127.0.0.1:9001 
RootUser: minio_root 
RootPass: minio_password 

Command-line: https://docs.min.io/docs/minio-client-quickstart-guide
   $ mc alias set myminio http://192.168.144.2:9999 minio_root minio_password

Documentation: https://docs.min.io
```

## Access from browser console

http://[MINIO_SERVER_IP]:9001

## Access file

```bash
$ curl http://[MINIO_SERVER_IP]:9000/bkt1/test.txt
aaaaa
```

## Access minio bucket using aws-cli

- Set user account credentials (for temporary by export)

AWS_ACCESS_KEY_ID = minio's user name  
AWS_SECRET_ACCESS_KEY = minio's user password  

```bash
$ export AWS_ACCESS_KEY_ID=minio_root
$ export AWS_SECRET_ACCESS_KEY=minio_password
```

- List bucket

```bash
$ aws --endpoint-url http://127.0.0.1:9000 s3 ls
2022-02-17 01:23:59 bkt1
```

## Access minio bucket using python boto3

- List bucket

```python
import boto3
from boto3.session import Session

s3_client = boto3.client(
    's3',
    aws_access_key_id='minio_root',
    aws_secret_access_key='minio_password',
    endpoint_url='http://127.0.0.1:9000'
)
response = s3_client.list_buckets()

for bucket in response['Buckets']:
    print(f'{bucket["Name"]}')
```

```bash
$ python list_s3_bucket.py 
bkt1
```

## Stop minio server

```bash
$ sudo docker-compose down
```