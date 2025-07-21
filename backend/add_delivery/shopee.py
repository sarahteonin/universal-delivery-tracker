import requests
from datetime import datetime


base_url = "https://spx.sg/shipment/order/open/order/get_order_info?spx_tn="
    
def get_status_history(tracking_number):
    url = f"https://spx.sg/shipment/order/open/order/get_order_info?spx_tn={tracking_number}"
    status_history = []

    try:
        response = requests.get(url)
        records = response.json().get("data", {}).get("sls_tracking_info", {}).get("records", [{}])
        
        for record in records:
            timestamp = record.get("actual_time")
            timestamp = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
            description = record.get("buyer_description")
            status = record.get("milestone_name")

            status_history.append({
                "timestamp": timestamp,
                "description": description,
                "status": status
            })
        
        status_history.sort(key=lambda x: x["timestamp"], reverse=True)
        
        return status_history
        
    except Exception as e:
        print(f"Error scraping Shopee: {e}")
        return "Error fetching status"
    

def get_latest_status(tracking_number):
    status_history = get_status_history(tracking_number)
    latest_status = status_history[0]["status"] if status_history else "Pending updates"

    return latest_status