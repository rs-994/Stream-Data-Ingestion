import os, json, uuid
import boto3
from datetime import datetime

s3 = boto3.client('s3')
BUCKET = 'airbnb-data-store2'

def lambda_handler(event, context):
    # EventBridge Pipes passes a list or a record—handle both
    records = event if isinstance(event, list) else [event]
    written = 0

    for rec in records:
        # For SQS sources, the message body usually lives at rec["body"]
        body = rec.get("body", rec)
        if isinstance(body, str):
            body = json.loads(body)

        # Optional: double-check nights > 1 (defensive)
        if int(body.get("nights", 0)) <= 1:
            continue

        # Partition by date
        ts = datetime.utcnow().strftime("%Y/%m/%d")
        key = f"bookings/year={ts.split('/')[0]}/month={ts.split('/')[1]}/day={ts.split('/')[2]}/{uuid.uuid4()}.json"
        s3.put_object(Bucket=BUCKET, Key=key, Body=json.dumps(body).encode("utf-8"))
        written += 1

    return {"status":"ok","written":written}
