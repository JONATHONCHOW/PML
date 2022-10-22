from datetime import datetime


class HelloWorld(object):
    def __init__(self, message: str) -> None:
        self.message: str = message

    def __str__(self) -> str:
        return f'{datetime.now()}:\t{self.message}'