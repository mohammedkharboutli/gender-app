
from util.Observer import Observer


class Observable:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer) -> None:
        """
        Registriert einen Observer.
        """
        self.observers.append(observer)

    def notify_observers(self) -> None:
        """
        Benachrichtigt alle registrierten Observer.
        """
        for observer in self.observers:
            observer.update()
