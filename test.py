import time
import threading

from tasker.decorator import task
from tasker.worker import start_worker
from tasker.queue import enqueue_task


@task()
def add(a, b):
    time.sleep(1)
    print("Result:", a + b)


threading.Thread(target=start_worker, daemon=True).start()

time.sleep(1)

enqueue_task("add", 2, 3)
enqueue_task("add", 10, 20)

time.sleep(5)
print("Main finished")