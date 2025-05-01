class vehicle():
   def  __init__(self,name):
       self.name=name

class bus(vehicle):
    def __init__(self,name,mileage,speed):
        self.mileage=mileage
        self.speed=speed
        vehicle.__init__(self,name)

school_bus=bus("VOLVO",13,80)
print("Vehicle name:",school_bus.name," Mileage:",school_bus.mileage," Speed:",school_bus.speed)
      