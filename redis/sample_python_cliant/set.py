import os

import redis


r = redis.Redis(host='localhost', port=os.environ['PORT'], db=0)

r.set('test', 'test_value')
