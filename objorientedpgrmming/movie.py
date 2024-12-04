class movie:



    def set_movie(self,title,rating,runtime,dir,genre):

        self.title=title

        self.rating=rating

        self.runtime=runtime

        self.dir=dir

        self.genre=genre

    def display(self):

        print(self.title,self.rating,self.runtime,self.dir,self.genre)

movie_instance1=movie()
movie_instance2=movie()

movie_instance1.set_movie("arm",8.0,2,"ggg","fiction")

movie_instance1.display()

movie_instance2.set_movie("kgf",7.0,3,"eee","mass")

movie_instance2.display()







