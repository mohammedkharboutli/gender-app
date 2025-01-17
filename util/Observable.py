from typing import List
from util.Observer import Observer


class Observable:
    def __init__(self):
        self.observers: List[Observer] = []

    def add_observer(self, observer: Observer) -> None:
        # Registrieren der Observer
        self.observers.append(observer)

    def notify_observers(self) -> None:
        # Benachrichtigen aller Observer
        for observer in self.observers:
            observer.update()
