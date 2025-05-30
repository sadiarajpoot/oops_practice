# class Student:
#     def __init__(self, name ,age):
#         self.name=name
#         self.age =age
#     def __str__(self):
#         return f"{self.name} {self.age}"
# student=Student("sadia",32)
# print(student)  

# 1. Encapsulation:
# class BankAccount:
#     def __init__(self,balance,name,age):
#         self.balance=balance
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return f"My Name is {self.name} Age is {self.age} and balance {self.balance}"
# bankaccount=BankAccount(20000,"sadia",18)
# print(bankaccount)
    # #  private 
# class Person:
#     def __init__(self,name):
#         self.__name=name   #private ko __ se likhty hain 
#     def get_name(self):
#         return self.__name  # access private varaible 
#     def __str__(self):
#         return self.__name
# person=Person("Ali")
# print(person.get_name())

# class Student:
#     def __init__(self,name,age,marks):
#         self.name=name
#         self.age=age
#         self.__marks=marks
#     def marks_Access(self):
#         return self.__marks
#     def __str__(self):
#         return f"{self.name} {self.age} {self.__marks}"
# s1=Student("sadia",18,2220)
# s2=Student(s1.name , s1.age ,  s1.marks_Access())
# print(s1)

# class person:
#     def __init__(self, name , age , marks):
#         self.__name =name 
#         self.age =age 
#         self.marks =marks
#     def Access_Name(self):
#         return self.__name
#     def __str__(self):
#         return f"{self.__name} {self.age} {self.marks}"
# p1=person("sadia",18,220)
# print(p1.Access_Name())

# protect
# class person:
#     def __init__(self, name , age , marks):
#         self._name =name 
#         self.age =age 
#         self.marks =marks
#     def __str__(self):
#         return f"{self._name} {self.age} {self.marks}"
# p1=person("sadia",18,220)
# print(p1._name)

# class person:
#     def __init__(self,name,age,marks):
#         self.name=name
#         self._age=age
#         self.marks=marks
#     def __str__(self):
#         return f"{self.name} {self._age} {self.marks}"
# p1=person("sadia",12,200)
# print(p1)

# 2. Abstraction:

# from abc import ABC,abstractmethod
# class Vehicles:
#     @abstractmethod
#     def start_engine(self):
#         pass
#     @abstractmethod
#     def stop_engine(self):
#         pass

# class Car (Vehicles):
#     def start_engine(self):
#         print("engine started now drive")
#     def stop_engine(self):
#           print("engine stopped not drive")
# car=Car()
# car.start_engine()
# car.stop_engine()

# from abc import ABC ,abstractmethod
# class Fan:
#     @abstractmethod
#     def Fan_On(self):
#         pass
#     @abstractmethod
#     def Fan_Off(self):
#         pass
# class Fan_Function(Fan):
#     def Fan_On(self):
#         print("Fan is ON ")
#     def Fan_Off(self):
#         print("Fan is OFF ")
# fan = Fan_Function()
# fan.Fan_Off()
# fan.Fan_On()

# from abc import ABC , abstractmethod
# class Washing_machine:
#     @abstractmethod
#     def washing_Started():
#         pass
#     @abstractmethod
#     def washing_Stopped():
#         pass
# class Washing_Function(Washing_machine):
#     def washing_Started():
#         print("washing started")
#     def washing_Stopped():
#         print("washing stopped")
# washed=Washing_Function
# washed.washing_Started()
# washed.washing_Stopped()

# encapsulation
# class Parents:
#     def __init__(self , name , age , marks):
#         self.__name=name
#         self.age=age
#         self.marks=marks
#     def Access_name(self):
#         return self.__name
#     def __str__(self):
#         return f" my name is {self.__name} and age is {self.age} marks i {self.marks}"
# p1=Parents("Sadia",18,550)
# print(p1.Access_name())

# from abc import ABC ,abstractmethod

# class Mobile:
#     @abstractmethod
#     def Started_mobile(self):
#         pass
#     @abstractmethod
#     def Mobile_Off(self):
#         pass
# class Mobile_Function(Mobile):
#     def Started_mobile(self):
#         print("Mobile is ON ")
#     def Mobile_Off(self):
#         print("Mobile is OFF ")

# m=Mobile_Function()
# print(m.Mobile_Off())
# print(m.Started_mobile())

# inheritance (single) 
# class Parents:
#     def greet():
#         print("hello from parents")

# class Child(Parents):
#     def salam():
#         print("hello from child")
# c=Child
# c.greet()
# c.salam()

# # multiple inheritance
# class Parents_1:
#     def greet_1(self):
#         print("hello parent 1")
# class Parents_2:
#     def greet_2(self):
#         print("hello parents 2 ")
# class Child(Parents_1,Parents_2):
#     def child(self): 
#        print("hello child")
# c=Child()
# c.greet_1()
# c.greet_2()
# c.child()

# class Person:
#     def hello(self):
#         print("Hello Person")
# class Child(Person):
#     def hello_change(self):
#         super().hello()
#         print("Super change")
#     def Hello(self):
#         print("Hello Child")
# c=Child()
# c.hello()
# c.Hello()
# c.hello_change()

# class Fan_On:
#     def fan_on(self):
#         print("Fan is Open Now")
# class Fan_Off(Fan_On):
#     def super_fan(self):
#         super().fan_on()
#         print("Fan is super")
#     def fan_off(self):
#         print("Fan is Close Now")
# c=Fan_Off()
# c.fan_off()
# c.fan_on()
# c.super_fan()

# class Hello_1:
#     def Hello(self):
#         print("Hello from Hello_1")
# class Hello_2(Hello_1):
#     def change_text(self):
#         super().Hello()
#         print("super function")
#     def hello(self):
#         print("Hello from Hello_2")
# c=Hello_2()
# c.Hello()
# c.change_text()
# c.hello()

# polymorphzam
# duck typing
# class Birds:
#     def fly (self):
#         print("Fly Birds")
# class Eagle:
#     def fly (self):
#         print("Fly Eagle")
# class Fish:
#     def swim(self):
#         print("Fish is swimming")
# def make_fly(make_fly):
#     make_fly.fly()
# birds=Birds()
# eagle=Eagle()
# fish=Fish()
# make_fly(birds)
# make_fly(eagle)
# make_fly(fish)

# class Parrot:
#     def fly(self):
#         print("Parrot can Fly")
# class Helicopter:
#     def fly (self):
#          print("Helicopter can fly")
# class Stone:
#     def hard(self):
#         print( "I m hard stone cannot fly")
# def animals_fly(animals):
#     animals.fly()
# parrot=Parrot()
# helicopter=Helicopter()
# stone=Stone()
# animals_fly(parrot)
# animals_fly(helicopter)
# # animals_fly(stone)