class bird:
 def __init__(self):
       print("birds")
 def whoisthis(self):
  print("bird")
        
def swim(self):
     print("swim faster")
        
def spe(self):
     print("i am bird")

class penguin(bird):
    def __init__(self):
        print("penguin")
        super().__init__(self)  
        def whoisthis(self):
         print("bird")

        def run(self):
         print(" I will run faster")

        def spe(self):
         print("i am peggy")

peggy=penguin()
peggy.whoisthis()
peggy.run()
peggy.spe()