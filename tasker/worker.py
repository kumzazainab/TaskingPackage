import time

from .queue import TASK_QUEUE
from .registry import TASK_REGISTRY

def start_worker():
    print("[WORKER STARTED]")

    while True:
        task = TASK_QUEUE.get()

        task_name = task["task_name"]
        args = task["args"]
        kwargs = task["kwargs"]

        func = TASK_REGISTRY.get(task_name)

        if not func:
            print(f"[ERROR] Task not found: {task_name}")
            continue

        try:
            print(f"[START] {task_name}")
            func(*args, **kwargs)
            print(f"[DONE] {task_name}")

        except Exception as e:
            print(f"[FAILED] {task_name} → {e}")