from fluent import sender
from fluent import event

TAG = 'python.test'
sender.setup(TAG, host='localhost', port=24224)
event.Event('test_event', {
    'message': 'aiueo',
})
