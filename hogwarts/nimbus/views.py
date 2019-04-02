from django.shortcuts import render
from django.conf import settings
import boto3

# Create your views here.


def checking_dynamodb(request):
    DYNAMO_ENDPOINT = getattr(settings, "DYNAMO_ENDPOINT", None)
    dynamodb = boto3.resource('dynamodb', endpoint_url=DYNAMO_ENDPOINT)
    view_table = dynamodb.Table('Music')
    if view_table is None:
        value = 'Not Present'
        return render(request, 'nimbus/broomstick_list.html', {'value': value})
    else:
        value = 'Present'
        return render(request, 'nimbus/broomstick_list.html', {'value': value})

def view_tables(request):
    DYNAMO_ENDPOINT = getattr(settings, "DYNAMO_ENDPOINT", None)
    dynamodb = boto3.resource('dynamodb', endpoint_url=DYNAMO_ENDPOINT)
    client = boto3.client('dynamodb', endpoint_url=DYNAMO_ENDPOINT)

    table_hash = client.list_tables()
    table_names = table_hash['TableNames']

    return render(request, 'nimbus/broomstick_list.html', {'value': 'Present', 'tables': table_names})



