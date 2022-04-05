import os

import redis


r = redis.Redis(host='localhost', port=os.environ['PORT'], db=0)

value = r.get('test')
print(value.decode())

r.delete('test')
