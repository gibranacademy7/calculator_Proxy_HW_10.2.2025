from abc import ABC, abstractmethod

class InputTemplate(ABC):
    @abstractmethod
    def get_input(self):
        pass

    @abstractmethod
    def validate_input(self, user_input):
        pass
