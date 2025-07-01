import json
import uuid
import boto3
import os
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('TABLE_NAME')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        body = json.loads(event["body"])
        tracking_number = body.get("trackingNumber")
        courier = body.get("courier")

        if not tracking_number or not courier:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing tracking number or courier"})
            }

        delivery_id = str(uuid.uuid4())
        user_id = "demo-user"  # Replace with real Cognito identity later

        item = {
            "userId": user_id,
            "deliveryId": delivery_id,
            "trackingNumber": tracking_number,
            "courier": courier,
            "latestStatus": "Pending",
            "statusHistory": [],
            "createdAt": datetime.utcnow().isoformat(),
            "lastChecked": None
        }

        table.put_item(Item=item)

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Delivery added", "delivery": item})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
