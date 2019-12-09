from abc import ABC, abstractmethod
from validators import AbstractValidator
import validators as val


# Создать два абстрактных класса AbstractValidator и AbstractField в соответственных
# файлах. Каждый из потомков этих классов обязан будет реализовывать два метода
# __init__  и is_valid(self, value) , который возвращает bool.


class AbstractField(ABC):

    @abstractmethod
    def __init__(self, validators=None):
        pass

    @abstractmethod
    def is_valid(self, value) -> bool:
        pass


# На основе AbstractField в fields.py необходимо создать следующие классы: CharField,
# TextField, IntegerField

# Каждый класс, потомок AbstractField должен принимать при инициализации аргумент
# validators - это список из экземпляров потомков AbstractValidator.

# В итоге, каждый из классов должен иметь возможность иметь стандартные валидаторы и те валидаторы,
# которые будут дополнительно указаны при инициализации.

# Главным отличием этих классов будут их <стандартные валидации> , где:
# CharField - TextValidator(min_length=0, max_length=999)
# TextField - TextValidator(min_length=1001, max_length=3000)
# IntegerField - IntegerValidator(min_value=128, max_value=1024)

# Тогда логика списка валидаций приобретёт следующий вид:
# <общий_список_валидаций> = <стандартные_валидации> + validators
# Метод is_valid для потомков AbstractField должен проходить по
# <общий_список_валидаций>
# и вызывать .is_valid(value) для каждого из валидаторов.

class CharField(AbstractField, ABC):
    def __init__(self, validators=None):
        super().__init__()
        self.validators_list = [val.TextValidator(min_length=0, max_length=999)]
        if isinstance(validators, list) and validators:
            self.validators_list += validators

    def is_valid(self, value) -> bool:

        return all([valid.is_valid(value) for valid in self.validators_list])


class TextField(AbstractField, ABC):
    def __init__(self, validators=None):
        super().__init__()
        self.validators_list = [val.TextValidator(min_length=1001, max_length=3000)]
        if isinstance(validators, list) and validators:
            self.validators_list += validators

    def is_valid(self, value) -> bool:
        return all([item.is_valid(value) for item in self.validators_list])


class IntegerField(AbstractField, ABC):

    def __init__(self, validators=None):
        super().__init__()
        self.validators_list = [val.IntegerValidator(min_value=128, max_value=1024)]
        if isinstance(validators, list) and validators:
            self.validators_list += validators

    def is_valid(self, value) -> bool:
        return all([valid.is_valid(value) for valid in self.validators_list])
