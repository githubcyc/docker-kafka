from kafka import KafkaProducer
import time
#  connect to Kafka
producer = KafkaProducer(bootstrap_servers='kafka:9092')


def emit():
    for i in range(100):
        print(f'send message {i}')
        producer.send('foobar', bytes(i))
        time.sleep(1)

if __name__ == '__main__':
    emit()
