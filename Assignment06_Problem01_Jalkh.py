# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 13:04:30 2024

@author: marcj
Problem 01 attempt 2
"""
class animal:
    def __init__(self,name):
        self.name=name
        self.hierarchy={"Eagle":1,"Cat":2,"Mouse":3} #define kingdom hierarchy
    def eat(self,animal): #application of hierarchy with eat method
        if self.hierarchy[self.name]<self.hierarchy[animal]:
            print(f"{self.name} eats {animal}...")
        elif self.hierarchy[animal]<self.hierarchy[self.name]:
            print(f"{self.name} is eaten by {animal}...")
        else:
            print("Unknown outcome of animals {self.name} & {animal} based on given hierarchy...")
    def sleep(self): #sleep method
        print(f"Animal {self.name} is sleeping ...")

    
class mammal(animal):
    def is_mammal(self):
        print(f"{self.name} is a hairy being...") # mammal description
        return True
        
class avian(animal):
    def is_avian(self):
        print(f"{self.name} is a feathery being...") # avian description
        return True
    
class cat(mammal): 
    def cat(self):
        if self.is_mammal()==True:
            print(f"Identified as Mammal {self.name}") # inheritance confirmation

class eagle(avian):
    def eagle(self):
        if self.is_avian()==True:
            print(f"Identified as Avian {self.name}") # inheritance confirmation

def main():
    # Cat animal test
    Benny=cat("Cat") # cat object
    Benny.is_mammal() # check mammal class inheritance
    Benny.cat() # confirm it
    Benny.eat("Mouse") # test base class method based on hierarchy
    Benny.sleep() 
    Benny.eat("Eagle") # test hierarchy again
    # Eagle animal test (same succession as above)
    Cochi=eagle("Eagle")
    Cochi.is_avian()
    Cochi.eagle()
    Cochi.eat("Cat")
    Cochi.eat("Mouse")
    Cochi.sleep()
    
main()