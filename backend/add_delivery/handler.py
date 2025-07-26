import json
import uuid
import boto3
import os
from datetime import datetime
from shopee import get_status_history, get_latest_status

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('TABLE_NAME')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        body = json.loads(event["body"])
        tracking_number = body.get("trackingNumber")
        courier = body.get("courier")

        if not courier:
            #courier = detect_courier(tracking_number_or_link)
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Courier not selected"})
            }

        if not tracking_number:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing tracking number"})
            }
        
        user_id = "user1"  # Replace with real Cognito identity later
        
        # Check if delivery already exists
        response = table.get_item(Key={"userId": user_id, "trackingNumber": tracking_number})
        if "Item" in response:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Delivery already exists"})
            }

        # Get status via scraper based on courier
        if courier == "Shopee":
            latest_status = get_latest_status(tracking_number)
            statusHistory = get_status_history(tracking_number)

        #elif courier == "Lazada":
            #latest_status = lazada.get_latest_status(tracking_number)
        else:
            latest_status = "Courier not supported yet"

        delivery_id = str(uuid.uuid4())
        

        item = {
            "userId": user_id,
            "trackingNumber": tracking_number,
            "deliveryId": delivery_id,
            "courier": courier,
            "latestStatus": latest_status,
            "statusHistory": statusHistory,
            "createdAt": datetime.now().astimezone(timezone(timedelta(hours=8))).strftime('%Y-%m-%d %H:%M:%S'),
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
