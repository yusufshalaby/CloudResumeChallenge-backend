import json
import os
import boto3

def lambda_handler(event, context):
    DYNAMODBTABLE = os.environ["DynamoDBTable"]

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(DYNAMODBTABLE)

    # Update the count
    table.update_item(Key={'id': 'resume'}, AttributeUpdates={'visit_count': {'Value': 1, 'Action': 'ADD'}})
    response = {"visitors":str(table.get_item(Key={'id': 'resume'})['Item']['visit_count'])}

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin" : "*",
            "Content-Type": "application/json"
        },
        "body": json.dumps(response)
    }

