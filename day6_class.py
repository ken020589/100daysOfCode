##!/usr/bin/env python
#day6 class

from msilib.schema import Class


class Human():
    def __init__(self, name, age):
        self._name = name
        self._age = age
    def __introduce(self):
        print("my name is " + self._name + " I'm " + str(self._age) + " years old.")
    def talk(self):
        self.__introduce()
        print("I join 100DaysOfCode")
    def old(self):
        self._age += 1
        print("my name is " + self._name + " I'm " + str(self._age) + " years old.")

Ken = Human("Ken", 22)
Ken.talk()
Ken.old()