#!/usr/bin/env python3

class Student:
    
    def __init__(self, jmeno, pohlavi, vek):
        self.__jmeno = jmeno
        self.__muz = pohlavi
        self.__vek = vek
        self.__plnolety = (vek > 18)

    def __str__(self):
        jsem_plnolety = "jsem" if self.__plnolety else "nejsem"
        pohlavi = "muž" if self.__muz else "žena"
        return "Jsem {0}, a jsem {1}. Je mi {2} let a {3} plnoletý.".format(
            self.__jmeno, pohlavi, self.__vek, jsem_plnolety)

    @property
    def vek(self):
        return self.__vek

    @vek.setter
    def vek(self, hodnota):
        self.__vek = hodnota
        self.__plnolety = (hodnota > 18)
       
s = Student("Pavel Hora", True, 20)
s.vek = 15
print(s)

input()