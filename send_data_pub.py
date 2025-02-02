from google.cloud import pubsub_v1
import os
import json
import random
from dotenv import load_dotenv

load_dotenv()


PROJECT_ID = os.getenv("PROJECT_ID")
TOPIC_NAME = os.getenv("TOPIC_NAME")


def publish_message(message: dict, publisher: pubsub_v1.PublisherClient):
    """Send a dictionary message to a pubsub topic

    Args:
        message (dict): A dictionary message
        publisher (pubsub_v1.PublisherClient): A pubsub client
    """
    topic_path = f"projects/{PROJECT_ID}/topics/{TOPIC_NAME}"
    message_bytes = json.dumps(message, indent=2).encode("utf-8")
    future = publisher.publish(topic_path, data=message_bytes)

    print(future.result())


if __name__ == "__main__":
    publisher = pubsub_v1.PublisherClient()

    for i in range(5):
        message = {
            "CodCAM": "CM" + str(i).zfill(3),
            "Temperatura": random.randint(-10, 5),
            "Odometro": random.randint(0, 100),
        }

        publish_message(message, publisher)
