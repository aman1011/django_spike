from django.shortcuts import render
from django.conf import settings
import boto3

# Create your views here.


def checking_dynamodb(request):
    DYNAMO_ENDPOINT = getattr(settings, "DYNAMO_ENDPOINT", None)
    dynamodb = boto3.resource('dynamodb', endpoint_url=DYNAMO_ENDPOINT)
    view_table = dynamodb.Table('Music')
    return render(request, 'nimbus/broomstick_list.html', {})


def create_table_in_dynamodb():
    DYNAMO_ENDPOINT = getattr(settings, "DYNAMO_ENDPOINT", None)
    dynamodb = boto3.resource('dynamodb', endpoint_url=DYNAMO_ENDPOINT)

    table = dynamodb.create_table(
        TableName='Custom_Table',
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'N',
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )

    print("Table Status:", table.table_status)
