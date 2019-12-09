from abc import ABC, abstractmethod


class AbstractValidator(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def is_valid(self, value) -> bool:
        pass


class TextValidator(AbstractValidator, ABC):

    def __init__(self, min_length: int = 16, max_length: int = 256):
        self.range = range(min_length, max_length + 1)

    def is_valid(self, value) -> bool:
        return len(value) in self.range


class IntegerValidator(AbstractValidator, ABC):

    def __init__(self, min_value: int = 32, max_value: int = 1024):
        self.range = range(min_value, max_value + 1)

    def is_valid(self, value) -> bool:
        return value in self.range
