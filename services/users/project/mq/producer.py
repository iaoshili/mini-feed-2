from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers='kafka:9093', value_serializer=lambda v: json.dumps(v).encode('ascii'))

def enqueue(feed_id):
    producer.send('feed_fanout', value={"feed_id": str(feed_id)})
    producer.flush()
