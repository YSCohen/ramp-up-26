import os

import redis

redis_host = os.environ.get("REDIS_HOST", "localhost")
redis_port = int(os.environ.get("REDIS_PORT", "6379"))

r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

pubsub = r.pubsub()
pubsub.subscribe("my_channel")

print("Subscriber started. Listening for messages on 'my_channel'...", flush=True)

for message in pubsub.listen():
    if message["type"] == "message":
        print(f"[RECEIVED]: {message['data']}", flush=True)
