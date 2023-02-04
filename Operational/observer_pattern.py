class Observer:
    def update(self, obj, *args, **kwargs):
        print("I see things")


class Observable:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observer(self, *args, **kwargs):
        for observer in self._observers:
            observer.update(self, *args, **kwargs)


observer = Observer()
thing = Observable()

thing.add_observer(observer)
thing.notify_observer()
