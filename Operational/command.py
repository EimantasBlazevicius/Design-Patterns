from abc import ABC, abstractmethod


class Remote(ABC):

    @abstractmethod
    def execute(self, channel):
        pass


class TVRemote(Remote):
    def __init__(self, company):
        self.company = company
        self.channels = {1: 'Discovery', 2: 'Cookies', 3: 'BBC'}

    def execute(self, channel):
        if int(channel) > len(self.channels):
            return "Nothing Ha Ha"

        print(f"Click the remote of company {self.company} to switch channel to {channel}")
        # Interpreter concept
        return self.channels[channel]


class Person(ABC):

    @abstractmethod
    def click(self, command, button):
        pass

    @abstractmethod
    def see(self):
        pass


class CouchPotato(Person):
    def __init__(self):
        self.result=''

    def click(self, command, button):
        self.result = command(button)

    def see(self):
        print(f"The TV is now showing this: {self.result}")


if __name__ == "__main__":
    potatoMonster = CouchPotato()
    samsungRemote = TVRemote('Samsung')

    potatoMonster.click(samsungRemote.execute, 3)
    potatoMonster.see()
