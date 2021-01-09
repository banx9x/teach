from abc import ABC, abstractmethod


class InvalidOperatorError(Exception):
    pass


class Stream(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperatorError("Stream already opened")
        self.open = True

    def close(self):
        if not self.opened:
            raise InvalidOperatorError("Steam already closed")
        self.open = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading from a file stream")


stream = FileStream()
stream.open()
stream.read()
