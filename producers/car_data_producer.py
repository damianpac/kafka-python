import pandas as pd
from kafka import KafkaProducer
from datetime import datetime
import time
import sys

"""
App reads content of csv file containing info about various vehicles and then it'll add it on
to a Kafka topic, one vehicle at a time and every three seconds. Basically it will constantly
produce new data for a consumer to pick up.

1. CSV content to pd.DataFrame
2. Publish on the topic
"""

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python <filename.py> <hostname> <port> <topic>", file=sys.stderr)
        exit(-1)
    
    host = sys.argv[1]
    port = sys.argv[2]
    topic = sys.argv[3]

    print("Kafka Producer Application Started ...")

    kafka_producer = KafkaProducer(bootstrap_servers=host + ":" + port,
                                   value_serializer=lambda x: x.encode('utf-8'))
    
    filepath = "./germany-dataset.csv"

    data = pd.read_csv(filepath)
    data_list = data.to_dict(orient="records")
    row = None

    for row in data_list:
        data_fields_value_list = []
        data_fields_value_list.append(row["mileage"])
        data_fields_value_list.append(row["make"])
        data_fields_value_list.append(row["model"])
        data_fields_value_list.append(row["fuel"])
        data_fields_value_list.append(row["gear"])
        data_fields_value_list.append(row["offerType"])
        data_fields_value_list.append(row["price"])
        data_fields_value_list.append(row["hp"])
        data_fields_value_list.append(row["year"])

        row = ','.join(str(v) for v in data_fields_value_list)

        print("Message Type: ", type(row))
        print("Message: ", row)

        kafka_producer.send(topic, row)

        time.sleep(3)

print("Kafka Producer Application Completed!")