import json
import boto3
import urllib3

http = urllib3.PoolManager()

def send_response(event, context, status, reason=""):
    response_body = json.dumps({
        "Status": status,
        "Reason": reason or "See CloudWatch Logs",
        "PhysicalResourceId": context.log_stream_name,
        "StackId": event["StackId"],
        "RequestId": event["RequestId"],
        "LogicalResourceId": event["LogicalResourceId"]
    })
    http.request("PUT", event["ResponseURL"], body=response_body,
                 headers={"Content-Type": ""})

def handler(event, context):
    table = boto3.resource("dynamodb").Table("FavstarAccountInventory")
    try:
        request_type = event["RequestType"]
        account_id = event["ResourceProperties"].get("AccountId", "unknown")
        env_type = event["ResourceProperties"].get("EnvironmentType", "unknown")

        if request_type in ("Create", "Update"):
            table.put_item(Item={"AccountId": account_id, "Environment": env_type})
        elif request_type == "Delete":
            table.delete_item(Key={"AccountId": account_id})

        send_response(event, context, "SUCCESS")
    except Exception as e:
        send_response(event, context, "FAILED", str(e))
