from datetime import datetime


class HelloWorld:
    """
    Hello world.

    :return: A string of greetings.
    """
    def __init__(self):
        self.message = 'Data science is fantastic!'

    def hello(self):
        print(f'{datetime.now()}:\t{self.message}')
