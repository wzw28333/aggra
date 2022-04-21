from typing import Any
from datetime import datetime
from aggra import Aggra

app = Aggra(debug=True)
celery = app.celery
server = app.server


@app.celery.task(name='tasks.add')
def add(x: int, y: int) -> int:
    """
    Add two numbers
    :param x:
    :param y:
    :return:
    """
    return x + y


@app.celery.task(name="tasks.hello")
def hello(name: str) -> Any:
    """
    Say hello
    :param name:
    :return:
    """
    return f"Hello {name}"


@app.celery.task(name="task.get_current_time")
def get_current_time() -> str:
    """
    Get current time
    :return:
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
