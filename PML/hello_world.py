from datetime import datetime


class HelloWorld:
    def __init__(self):
        self.message = 'Data science is fantastic!'

    def hello(self):
        print(f'{datetime.now()}:\t{self.message}')
