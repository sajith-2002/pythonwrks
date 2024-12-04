from abc import ABC,abstractmethod



class bike(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod    
    def stop(self):
        pass

class hunter(bike):

    def start(self):
        print("hunter strt mthd")

    def accelerate(self):
        print("hunter accelerate")

    def stop(self):
        print("hunter stop")

hunter_instnce=hunter()
hunter_instnce.start()
hunter_instnce.accelerate()
hunter_instnce.stop()

