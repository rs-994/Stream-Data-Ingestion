import json, uuid, random
from datetime import date, timedelta
import boto3

sqs = boto3.client('sqs')
QUEUE_URL = 'https://sqs.us-east-2.amazonaws.com/646047875925/AirbnbBookingQueue'

CITIES = ["New York, USA", "Austin, USA", "Paris, France", "Rome, Italy", "Tokyo, Japan"]

def make_booking():
    start = date.today() + timedelta(days=random.randint(0, 10))
    nights = random.randint(1, 5)
    end = start + timedelta(days=nights)
    return {
        "bookingId": str(uuid.uuid4()),
        "userId": f"user-{random.randint(1000,9999)}",
        "propertyId": f"prop-{random.randint(100,999)}",
        "location": random.choice(CITIES),
        "startDate": start.isoformat(),
        "endDate": end.isoformat(),
        "price": round(random.uniform(60, 450), 2),
        "nights": nights
    }

def lambda_handler(event, context):
    N = int(event.get("count", 5)) if isinstance(event, dict) else 5
    sent = 0

    for _ in range(N):
        msg = make_booking()
        response = sqs.send_message(
            QueueUrl=QUEUE_URL,
            MessageBody=json.dumps(msg)
        )
        print("Sent messageId:", response.get("MessageId"))
        sent += 1

    return {"status": "ok", "sent": sent}
