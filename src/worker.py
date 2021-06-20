import time
import random
import json

import redis


QUEUE_NAME = "queue:ai-tasks"
REDIS_HOST = "localhost"
REDIS_PORT = 6379


if __name__ == "__main__":
    redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
    
    while True:
        packed = redis_client.blpop(QUEUE_NAME, timeout=60)
        if packed is None:
            continue

        info = json.loads(packed[1])

        task_id = info["id"]
        data = info["data"]
        
        print("=" * 20)
        print(f"TASK_ID: {task_id}")
        print(f"DATA: {data}")
        print("JUST DO AI...")
        time.sleep(2)
        redis_client.set(
            task_id, json.dumps({"price": random.randint(0, 100)})
        )
        print("DONE")

