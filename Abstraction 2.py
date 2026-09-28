from abc import ABC, abstractmethod
class TV(ABC):
    @property
    @abstractmethod
    def turn_on(self):
        pass

    def work(self):
        return "TV Working"

class SamsungTV(TV):
    @property
    def turn_on(self):
        return "Samsung TV is now ON"

    def work(self):
        return "TV is working fine"


samsung_tv = SamsungTV()
print(samsung_tv.work())