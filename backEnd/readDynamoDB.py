import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('JOBLIST')

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': table.scan()
    }
