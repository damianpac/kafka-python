from kafka import KafkaConsumer
from kafka.consumer import group
import json

if __name__ == '__main__':
    consumer = KafkaConsumer(
        'kitt_prog-created-prog',
        bootstrap_servers=['localhost:9092'],
        group_id='ConsumerGroupA'
    )

    print("Consumer started!")

    for i in consumer:
        print(f"consumer data {json.loads(i.value)}")
    