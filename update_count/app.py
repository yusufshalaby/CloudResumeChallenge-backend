import json
import os
import boto3

def lambda_handler(event, context):
    DYNAMODBTABLE = os.environ["DynamoDBTable"]

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(DYNAMODBTABLE)

    # Update the count
    response = table.update_item(Key={'id': 'resume'}, 
                                AttributeUpdates={'visit_count': {'Value': 1, 'Action': 'ADD'}},
                                ReturnValues='UPDATED_NEW')
    
    body = {"visitors":str(response['Attributes']['visit_count'])}

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin" : "*",
            "Content-Type": "application/json"
        },
        "body": json.dumps(body)
    }

