class parent:

    def vehicles(self):

        self.bikes=["passionpro","activa"]

        return self.bikes
    

class child(parent):

    def vehicles(self):
        
        self.bikes=super().vehicles()

        self.bikes.append("hunter")
        
        
        
        return self.bikes
    
child_instance=child()


print(child_instance.vehicles())