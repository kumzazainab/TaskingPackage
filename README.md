# TaskingPackage 🚀

A lightweight Python task execution framework for building simple background task systems using decorators, workers, and queue-based execution.

## 📌 Features

- 🧩 Simple task decorator system
- ⚙️ Worker-based task execution
- 📬 In-memory queue handling
- 🔄 Task registry system
- 🧪 Lightweight and easy to understand architecture


## 📂 Project Structure

tasker/
│── decorator.py   # Task decorator
│── executor.py    # Task execution logic
│── queue.py       # Task queue system
│── registry.py    # Task registry
│── worker.py      # Worker to process tasks


---

## 🚀 How It Works

1. Define a task using decorator
2. Register task automatically
3. Push task into queue
4. Worker executes tasks


## 🧪 Example Usage

```python
from tasker.decorator import task
from tasker.worker import Worker

@task
def add(a, b):
    return a + b

worker = Worker()
worker.run()


## 📦 Installation & Setup

Clone the repository:

```bash
git clone https://github.com/kumzazainab/TaskingPackage.git
cd TaskingPackage

## Install in editable mode
pip install -e . 