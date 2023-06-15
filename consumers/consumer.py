from kafka import KafkaConsumer

consumer = KafkaConsumer('kitt_prog-created-prog')

for message in consumer:
    print('\n', message)