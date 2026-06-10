import redis

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

pubsub = r.pubsub()
pubsub.subscribe("my_channel")

print("Subscriber started. Listening for messages on 'my_channel'...", flush=True)

for message in pubsub.listen():
    if message["type"] == "message":
        print(f"[RECEIVED]: {message['data']}", flush=True)
