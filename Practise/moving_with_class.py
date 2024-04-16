#class Car:
#    wheels = 4 #class variable
#    def __init__(self,make,model,year,color):
#        self.make = make #instance variable
#        self.model = model #instance variable
#        self.year = year #instance variable
#        self.color = color #instance variable
#--------------------------------------------------
#class Animal:
#    alive = True
    
#    def eat(self):
#       print("This animal is eating")

#    def sleep(self):
#        print("This animal is sleeping")

#class Rabbit(Animal):
#    def run(self):
#        print("Rabbit is running")
#class Fish(Animal):
#    def swim(self):
#        print("Fish is swimming")
#class Hawk(Animal):
#    def fly(self):
#        print("Hawk is flying")

#rabbit = Rabbit()
#fish = Fish()
#hawk = Hawk()

#print(rabbit.alive)
#fish.eat()
#hawk.sleep()

#rabbit.run()
#fish.swim()
#hawk.fly()
#--------------------------------------------------
# MULTI - LEVEL INHERITANCE
#class Organism:
#    alive = True

#class Animal(Organism):
#    def eat(self):
#        print("This animal is eating")
#class Dog(Animal):
#    def bark(self):
#        print("Dog is barking")
#dog = Dog()
#print(dog.alive) #inherited from organism class
#dog.eat() #inherited from animal class
#dog.bark() #defined in dog class
#--------------------------------------------------
# MULTIPLE INHERITANCE
#class Prey:
#    def flee(self):
#        print("This animal flees")
#class Predator:
#    def hunt(self):
#        print("This predator hunts animals")
#class Rabbit(Prey):
#    pass
#class Hawk(Predator):
#    pass
#class Fish(Prey, Predator):
#    pass

#rabbit = Rabbit()
#hawk = Hawk()
#fish = Fish()

#rabbit.flee()
#hawk.hunt()
#fish.flee()
#fish.hunt()
#--------------------------------------------------
# METHOD OVERRIDING
#class Animal:
#    def eat(self):
#        print("This animal is eating")
#class Dog(Animal):
    #def eat(self):
        #print("Dog is eating a bone!")

#dog = Dog()
#dog.eat()
#--------------------------------------------------
#class Car:
#    def turn_on(self):
#        print("You turned ON the engine")
#        return self
#    def drive(self):
#        print("You drove the car")
#        return self
#    def brake(self):
#        print("You stopped the car")
#        return self
#    def turn_off(self):
#        print("You turned OFF the engine")
#        return self

#car = Car()
#car.turn_on().drive().brake().turn_off()
#--------------------------------------------------
#class Rectangle:
#   def __init__(self,length,width):
#        self.length = length
#        self.width = width
#class Square(Rectangle):
#    def __init__(self,side):
#        super().__init__(side,side)

#    def area(self):
#        return self.length*self.width
#class Cube(Rectangle):
#    def __init__(self,side,height):
#        super().__init__(side,side)
#        self.height = height

#    def volume(self):
#        return self.length*self.width*self.height

#square = Square(3)
#cube = Cube(3,3)
#print(square.area())
#print(cube.volume())
#--------------------------------------------------
# OBJECT AS ARGUMENTS
#class Car:
#    color = None
#class Motorcycle:
#    color = None
#def change_color(vehicle,color):
#    vehicle.color = color
#car_1 = Car()
#car_2 = Car()
#car_3 = Car()

#bike_1 = Motorcycle()
#change_color(car_1,"Red")
#change_color(car_2,"Blue")
#change_color(car_3,"Yellow")
#change_color(bike_1,"Black")

#print(car_1.color)
#print(car_2.color)
#print(car_3.color)
#print(bike_1.color)









































