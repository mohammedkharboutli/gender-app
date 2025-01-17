from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self) -> None:
        # Methode, die von den Observers implementiert werden muss
        pass
