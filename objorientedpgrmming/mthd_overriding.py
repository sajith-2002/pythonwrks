class parent:

    def mobile(self):

        print("nokia")

class child(parent):
            
    def mobile(self):
        
        print("iphone")

child_instance=child()
child_instance.mobile()