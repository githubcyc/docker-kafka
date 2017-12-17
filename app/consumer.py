from kafka import KafkaConsumer, TopicPartition

consumer = KafkaConsumer(bootstrap_servers='kafka:9092')
#consumer.assign([TopicPartition('foobar',1)])
consumer.subscribe('foobar')
print('consumer connected')
for msg in consumer:
    print(f'received data：{msg}')
