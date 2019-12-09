from abc import ABC, abstractmethod
import validators as val


class AbstractField(ABC):

    @abstractmethod
    def __init__(self, validators=None):
        pass

    @abstractmethod
    def is_valid(self, value) -> bool:
        pass


class CharField(AbstractField, ABC):
    def __init__(self, validators=None):
        self.validators_list = [val.TextValidator(min_length=0, max_length=999)]
        self.validators_list += validators if isinstance(validators, list) and validators else []

    def is_valid(self, value) -> bool:
        return all([valid.is_valid(value) for valid in self.validators_list])


class TextField(AbstractField, ABC):
    def __init__(self, validators=None):
        self.validators_list = [val.TextValidator(min_length=1001, max_length=3000)]
        self.validators_list += validators if isinstance(validators, list) and validators else []

    def is_valid(self, value) -> bool:
        return all(item.is_valid(value) for item in self.validators_list)


class IntegerField(AbstractField, ABC):

    def __init__(self, validators=None):
        self.validators_list = [val.IntegerValidator(min_value=128, max_value=1024)]
        self.validators_list += validators if isinstance(validators, list) and validators else []

    def is_valid(self, value) -> bool:
        return all([valid.is_valid(value) for valid in self.validators_list])
