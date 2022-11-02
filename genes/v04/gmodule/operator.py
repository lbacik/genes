
from typing import Union
from abc import ABC, abstractmethod
from .generation import Generation

class Operator(ABC):

    @abstractmethod
    def do(self, generation: Generation) -> Union[None, Generation]:
        pass

