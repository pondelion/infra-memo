import json
import time
from datetime import date, datetime

from kafka import KafkaProducer
from kafka import KafkaConsumer


TOPIC_NAME = 'topic-01'
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
data = {
    'id': 100,
    'time': datetime.now().isoformat(),
    'message': 'hello'
}
# result = producer.send(TOPIC_NAME, key=datetime.now().strftime("%Y/%m/%d").encode('utf-8'), value=json.dumps(data).encode('utf-8'))
result = producer.send(TOPIC_NAME, value=json.dumps(data).encode('utf-8'))
print(str(result))
time.sleep(5)