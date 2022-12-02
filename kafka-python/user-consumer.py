import json 
from kafka import KafkaConsumer


topic_nm = 'topic_user_location'


if __name__ == '__main__':
    # Kafka Consumer 
    consumer = KafkaConsumer(
        topic = topic_nm,
        bootstrap_servers='localhost:9092', #broker
        auto_offset_reset='earliest'
    )
    for message in consumer:
        print(json.loads(message.value))