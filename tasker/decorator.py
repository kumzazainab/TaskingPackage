import functools
from .executor import run_task
from .registry import TASK_REGISTRY

def task(name=None):
    def decorator(func):
        task_name = name or func.__name__
        TASK_REGISTRY[task_name] = func

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        wrapper.run_async = lambda *a, **kw: run_task(task_name, *a, **kw)

        return wrapper
    return decorator