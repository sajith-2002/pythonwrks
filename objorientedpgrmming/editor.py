class editor:

    def __init__(self,name,vendor):

        self.name=name
        self.vendor=vendor

    def display(self):

        print(self.name,self.vendor)

    def __str__(self):
        
        return self.name
    

editor_instance1=editor("vs code","abcc")
editor_instance2=editor("pycharm","jebrains")
editor_instance2=editor("intellij","jetbrains")

print(editor_instance2)  