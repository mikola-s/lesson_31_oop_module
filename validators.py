from abc import ABC, abstractmethod


# Создать два абстрактных класса AbstractValidator и AbstractField в соответственных
# файлах. Каждый из потомков этих классов обязан будет реализовывать два метода
# __init__  и is_valid(self, value) , который возвращает bool.

class AbstractValidator(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def is_valid(self, value) -> bool:
        pass


# На основе AbstractValidator в validators.py необходимо создать следующие классы:
# TextValidator и IntegerValidator.

class TextValidator(AbstractValidator, ABC):

    # TextValidator при инициализации должен принимать 2 аргумента min_length ,
    # max_length со значениями по-умолчанию 16 и 256 соотвественно.

    def __init__(self, min_length: int = 16, max_length: int = 256):
        self.range = range(min_length, max_length + 1)

    def is_valid(self, value) -> bool:
        # Проверка в методе .is_valid(self, value) должна проверять, чтобы значение,
        # которое передали в валидацию находилось в рамках проверки min_length и
        # max_length включительно.
        return len(value) in self.range


class IntegerValidator(AbstractValidator, ABC):

    # IntegerValidator при инициализации должен принимать 2 аргумента min_value ,
    # max_value со значениями по-умолчанию 32 и 1024 соотвественно.

    def __init__(self, min_value: int = 32, max_value: int = 1024):
        self.range = range(min_value, max_value + 1)

    def is_valid(self, value) -> bool:
        # Не забываем про реализацию is_valid
        print(f"IntegerValidator is_valid {value in self.range}")
        return value in self.range
