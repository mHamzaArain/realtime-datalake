# from kafka import KafkaConsumer
# import json

# def consume_kafka_topic():
#     consumer = KafkaConsumer(
#         'taxi_trip_record',
#         bootstrap_servers=['localhost:9092'],
#         value_deserializer=lambda v: json.loads(v.decode('utf-8'))
#     )

#     for message in consumer:
#         print(f"Received record from Kafka: {message.value}")

# if __name__ == "__main__":
#     consume_kafka_topic()
