from kafka import KafkaConsumer

consumer = KafkaConsumer('topic-01', group_id='topic-01')

for msg in consumer:
    print (msg)
