import time
from queue import Queue

TASK_QUEUE = Queue()

def enqueue_task(task_name, *args, **kwargs):
    TASK_QUEUE.put({
        "task_name": task_name,
        "args": args,
        "kwargs": kwargs,
        "timestamp": time.time()
    })
