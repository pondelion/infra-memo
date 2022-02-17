
## Start local dynamodb server

```bash
$ sudo docker-compose up -d
```

```bash
$ sudo docker logs dynamodb-local
Initializing DynamoDB Local with the following configuration:
Port:   8000
InMemory:       false
DbPath: /data
SharedDb:       true
shouldDelayTransientStatuses:   false
CorsParams:     *
```

## Create table using aws-cli

```bash
$ aws dynamodb create-table --endpoint-url http://localhost:8000 --table-name test_table1 --attribute-definitions AttributeName=testId,AttributeType=S --key-schema AttributeName=testId,KeyType=HASH --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1
{
    "TableDescription": {
        "AttributeDefinitions": [
            {
                "AttributeName": "testId",
                "AttributeType": "S"
            }
        ],
        "TableName": "test_table1",
        "KeySchema": [
            {
                "AttributeName": "testId",
                "KeyType": "HASH"
            }
        ],
        "TableStatus": "ACTIVE",
        "CreationDateTime": "2022-02-17T17:05:47.305000+09:00",
        "ProvisionedThroughput": {
            "LastIncreaseDateTime": "1970-01-01T09:00:00+09:00",
            "LastDecreaseDateTime": "1970-01-01T09:00:00+09:00",
            "NumberOfDecreasesToday": 0,
            "ReadCapacityUnits": 1,
            "WriteCapacityUnits": 1
        },
        "TableSizeBytes": 0,
        "ItemCount": 0,
        "TableArn": "arn:aws:dynamodb:ddblocal:000000000000:table/test_table1"
    }
}
```

## List tables using aws-cli

```bash
$ aws dynamodb list-tables --endpoint-url http://localhost:8000
{
    "TableNames": [
        "test_table1"
    ]
}
```

## List tables using python boto3

```bash
$ python list_dynamodb_table.py 
{'TableNames': ['test_table1'], 'ResponseMetadata': {'RequestId': '**********************', 'HTTPStatusCode': 200, 'HTTPHeaders': {'date': 'Thu, 17 Feb 2022 08:20:17 GMT', 'content-type': 'application/x-amz-json-1.0', 'x-amz-crc32': '2064753776', 'x-amzn-requestid': '**********************', 'content-length': '30', 'server': 'Jetty(9.4.18.v20190429)'}, 'RetryAttempts': 0}}
```