'''
    Using the concept of object oriented programming and inheritance,
    create a super class named Computer,
    which has two sub classes named Desktop and Laptop.

    Define two methods in the Computer class named getspecs and displayspecs, 
    to get the specifications and display the specifications of the computer.

    You can use any specifications which you want.
    The Desktop class and the Laptop class should have one specification which is exclusive to them 
    for example laptop can have weight as a special specification.

    Make sure that the sub classes have their own methods to get and display their special specification.
    Create an object of laptop/ desktop and make sure to call all the methods from the
    computer class as well as the methods from the own class
'''

class Computer:

    def __init__(self,ram, gpu, processor):
        self.ram = ram
        self.gpu = gpu
        self.processor = processor


    def getspecs(self):
        print("Enter specifications")
        self.ram = input("Enter RAM size: ")
        self.gpu = input("Enter GPU model: ")
        self.processor = input("Enter PROCESSOR model: ")
    
    def displayspecs(self):
        print("Specifications of your system")
        print("Ram size:{} GPU:{} Processor:{}".format(self.ram, self.gpu, self.processor))

class Desktop(Computer):
    def __init__(self, casecolor):
        self.casecolor = casecolor
    
    def get_case_color(self):
        self.casecolor = input("Enter case color: ")
    
    def show_case_color(self):
        print("Desktop specifications")
        print("Case color:{}".format(self.casecolor))

class Laptop(Computer):
    def __init__(self, weight):
        self.weight = weight
    
    def get_weight(self):
        self.weight = input("Enter weight: ")
    
    def show_weight(self):
        print("Laptop weight")
        print("Laptop weight:{}".format(self.weight))

object1 = Laptop("")
object1.getspecs()
object1.get_8weight()
object1.displayspecs()
object1.show_weight




