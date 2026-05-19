import threading
from .registry import TASK_REGISTRY

def run_task(task_name, *args, **kwargs):
    func = TASK_REGISTRY.get(task_name)

    if not func:
        print(f"Task '{task_name}' not found")
        return

    def target():
        print(f"[START] {task_name}")
        try:
            func(*args, **kwargs)
            print(f"[DONE] {task_name}")
        except Exception as e:
            print(f"[ERROR] {task_name}: {e}")

    thread = threading.Thread(target=target)
    thread.daemon = True
    thread.start()