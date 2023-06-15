from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

future = producer.send('kitt_prog-created-prog',
                       b'test message')

print('\n', future.get(timeout=60))

future = producer.send('kitt_prog-created-prog',
                       key=b'test message 2',
                       value=b'test value 2')

print('\n', future.get(timeout=60))