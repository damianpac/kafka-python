from kafka import KafkaProducer
import json
import time
#from customer_data import get_registered_user

def json_serializer(data):
  return json.dumps(data).encode('utf-8')

#def get_partitioner(key_bytes, all_partitions, available_partitions):
  # this is hardcoded to 1 (partition 1), but in real life this should be specified based on the parameters passed to this function.
#  return 1

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=json_serializer)

if __name__ == '__main__':
  while True:
    user_data = [value for value in range(20)]
    print(user_data)
    producer.send(topic='customer_details', value=user_data)
    time.sleep(3)

