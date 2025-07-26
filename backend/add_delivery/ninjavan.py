import requests
from datetime import datetime, timezone, timedelta
    
def get_status_history(tracking_number):
    url = f"https://walrus.ninjavan.co/sg/dash/1.2/public/orders?tracking_id={tracking_number}"
    status_history = []

    def convert_to_sg_time(iso_time):
        utc_time = datetime.fromisoformat(iso_time.replace("Z", "+00:00"))
        sg_time = utc_time.astimezone(timezone(timedelta(hours=8)))
        return sg_time.strftime('%Y-%m-%d %H:%M:%S')

    try:
        response = requests.get(url)
        records = response.json().get("events", [{}])

        timestamp = response.json().get("created_at", {})
        print(timestamp)
        timestamp = convert_to_sg_time(timestamp)

        status_history.append({
            "timestamp": timestamp,
            "description": "Order Created",
            "status": "Order information received"
        })
        
        for record in records:
            timestamp = record.get("time")
            timestamp = convert_to_sg_time(timestamp)
            types = record.get("type")

            if (types == "DRIVER_PICKUP_SCAN"):
                status = "Pick up success"
                description = "Package picked up from seller by driver"
            elif (types == "HUB_INBOUND_SCAN"):
                status = "Arrived at sorting facility"
                description = "Package arrived at sorting facility"
            elif (types == "DRIVER_INBOUND_SCAN"):
                status = "Out for delivery"
                description = "Package is out for delivery"
            elif (types == "DELIVERY_SUCCESS"):
                status = "Delivered"
                description = "Package delivered to recipient"
            
            status_history.append({
                "timestamp": timestamp,
                "description": description,
                "status": status
            })
        
        status_history.sort(key=lambda x: x["timestamp"], reverse=True)
        
        return status_history
        
    except Exception as e:
        raise RuntimeError(f"Error scraping NinjaVan: {e}")
    

def get_latest_status(tracking_number):
    status_history = get_status_history(tracking_number)
    latest_status = status_history[0]["status"] if status_history else "Pending updates"

    return latest_status