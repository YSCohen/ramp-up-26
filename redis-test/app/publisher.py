from fastapi import FastAPI, Body
import redis

app = FastAPI(title="Publisher")

r = redis.Redis(host="localhost", port=6379, decode_responses=True)


@app.post("/publish")
def publish_message(message: str = Body(..., media_type="text/plain")):
    receiver_count = r.publish("my_channel", message)
    return {
        "status": "Message published successfully",
        "channel": "my_channel",
        "text": message,
        "active_subscribers": receiver_count,
    }
