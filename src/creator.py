import time
import json
import uuid

import redis


QUEUE_NAME = "queue:ai-tasks"
REDIS_HOST = "localhost"
REDIS_PORT = 6379


if __name__ == "__main__":
    redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)

    # Create task
    example_data = {
        "n_rooms": 1,
        "area": 50,
    }
    example_id = str(uuid.uuid4())

    data = {"id": example_id, "data": example_data}

    redis_client.rpush(QUEUE_NAME, json.dumps(data))

    # Get result 
    time.sleep(5)
    print(json.loads(redis_client.get(example_id)))