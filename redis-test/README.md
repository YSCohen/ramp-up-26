# Run

#### Start Redis
```
docker run -p 6379:6379 -d redis
```

Run each of the following commands in a separate shell
#### Start the publisher API
```
uv run fastapi dev publisher.py --port 8080
```

#### Start the reciever
```
uv run subscriber.py
```

You can submit messages with curl/xh or from [Swagger](http://localhost:8080/docs#/default/publish_message_publish_post)