from fluent import sender
from fluent import event

TAG = 's3.test2'
sender.setup(TAG, host='localhost', port=24224)
event.Event('test_event', {
    'message': 'aiueo',
}, )
