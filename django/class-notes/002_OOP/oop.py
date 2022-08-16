# class Person:
#     company = "clarusway"

#     def test(self):
#         print("test")

#     def set_details(self, name, age):
#         self.name = name
#         self.age = age

#     def get_details(self):
#         print(self.name, self.age)

#     @staticmethod
#     def salute():
#         print("Hi there!")


# person1 = Person()
# person2 = Person()

# # person1.test()
# # Person.test(person1)  python arkada bu şekle dönüştürüyor ve o yüzden üstteki çalışmıyor.(arguman gönderdin diyor) def tanımlamasına self ekleyerek sorunu çözebiliriz.
# person1.set_details("victor", 30)
# person1.get_details()

# person1.salute()
# person2.salute()

#! special methods(init,str)

# class Person:
#     company = "clarusway"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#         self._id = 5000
#         #! 👆 Bu id'yi değiştirirsen sıkıntı yaşarsın diyoruz "_" kullanarak. id'ye ulaşıp değiştirebiliyoruz.

#         self.__id = 3000
#         #! "__" kullanarak bu id'yi ulaşılamaz & değiştirilemez yaptık.

#     def __str__(self):
#         return f"{self.name} - {self.age}"

#     def get_details(self):
#         print(self.name, self.age)

# person1 = Person("Henry", 18)
# person1._id = 4000

# print(person1._id) # 4000
# print(person1.__id) # ....NO ATTRIBUTE...

class Person:
    company = "clarusway"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} - {self.age}"

    def get_details(self):
        print(self.name, self.age)

class Employee(Person):
    def __init__(self, name, age, path):
        # self.name = name
        # self.age = age

        #! parent'taki attribute'ları super() metoduyla alabiliyoruz👇

        super().__init__(name, age)
        self.path = path

    #? Parent'taki metodu ihtiyacımız doğrultusunda overwrite ederek tekrardan tanımlamış olduk 👇
    def get_details(self):
        print(self.name, self.age, self.path)

emp1 = Employee("Victor", 32, "FS")

print(emp1) # Victor - 32

emp1.get_details() # Victor 32 FS


#! inner class

from django.db import models
class Article(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)

    class Meta:
        ordering = ["name"]
        
        
print(Employee.mro())
        