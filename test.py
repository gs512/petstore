import json
from time import sleep

from kafka import KafkaConsumer, KafkaProducer

BOOSTRAP_SERVERS = ['localhost:29092']

def publish_message(producer_instance, topic_name, key, value):
    try:
        key_bytes = bytes(key, encoding='utf-8')
        value_bytes = bytes(value, encoding='utf-8')
        producer_instance.send(topic_name, key=key_bytes, value=value_bytes)
        producer_instance.flush()
        print('Message published successfully.')
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))


def connect_kafka_producer():
    _producer = None
    try:
        _producer = KafkaProducer(bootstrap_servers=BOOSTRAP_SERVERS)
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return _producer




if __name__ == '__main__':
    topic_name = 'test'
    
    producer = connect_kafka_producer()
    # producer.send(topic_name, b'boom')
    publish_message(producer, topic_name, 'message','hello world')

    consumer = KafkaConsumer(topic_name, auto_offset_reset='earliest',
                             bootstrap_servers=BOOSTRAP_SERVERS, consumer_timeout_ms=1000)
    for msg in consumer:
        print(msg.value)
    consumer.close()
    sleep(5)

    