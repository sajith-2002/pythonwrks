from abc import ABC,abstractmethod

class editor(ABC):

    @abstractmethod
    def open(self):
        pass
    
    @abstractmethod
    def write(self):
        pass

    @abstractmethod
    def debug(Self):
        pass

    @abstractmethod
    def execute(self):
        pass

class vscode(editor):

    def open(self):
        print("vscode open")

    def write(self):
        print("vscode write")

    def debug(self):
        print("vscode debug")

    def execute(self):
        print("vscode execute")

vscode_instsnce=vscode()
vscode_instsnce.debug()