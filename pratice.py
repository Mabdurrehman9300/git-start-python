# practicing OOP, making a class(intended to make it parent and make other classes that will inheritance)
class Animal:
    def __init__(self, health, energy, color, body): # have attributes of health,energy,color,body
        self.health = health
        self.energy = energy
        self.color = color
        self.body = body

    # methods
    def move(self, speed): # move method, (It print)
        print(f'Animal is moving with speed of {speed}')

    def attack(self, power): # attack method, (It prints)
        print(f'Animal is attacking with power of {power} and using energy {self.energy}')
        self.energy -= power

    def camouflage(self): # camouflage method, (It print)
        print(f'"{self.color} {self.body}" is hiding')

animal = Animal(100, 100, 'red', 'mammal') # initiating the class, passing health,energy,color,mammal in it
# calling the methods
animal.move(120)
animal.attack(20)
animal.camouflage()