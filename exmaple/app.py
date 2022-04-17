from aggra import Aggra

app = Aggra(debug=True)
celery = app.celery


@app.celery.task(name='tasks.add')
def add(x, y):
    """
    Add two numbers
    :param x:
    :param y:
    :return:
    """
    return x + y


app.run()
