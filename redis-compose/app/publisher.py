import os

from fastapi import FastAPI, Body
import redis

app = FastAPI(title="Publisher")

redis_host = os.environ.get("REDIS_HOST", "localhost")
redis_port = int(os.environ.get("REDIS_PORT", "6379"))

r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)


@app.post("/publish")
def publish_message(message: str = Body(..., media_type="text/plain")):
    receiver_count = r.publish("my_channel", message)
    return {
        "status": "Message published successfully",
        "channel": "my_channel",
        "text": message,
        "active_subscribers": receiver_count,
    }
