#!/usr/local/bin/python3

class Person:
    """ Person class """
    count = 0             # class variable 
    def __init__(self, id, name, i=0, d=0):
        self.id   = id      # instance variable 
        self.name = name
        self.income  = i
        self.deposit = d
        Person.count += 1
    def sayHi(self):
        self.__sayHi()
    def __sayHi(self):      # like private method, cannot call from outside
        print(self.name + ": Hi!")
    def __str__(self):      # define the string when convert the object to string type
        return "ID:" + str(self.id) + "  Name: " + self.name 
    def showDetail(self):
        print("-------------")
        print("ID     :"  + str(self.id) + "\n"  \
              "Name   :"  + self.name    + "\n"  \
              "Income :"  + str(self.income) + "\n" \
              "Deposit:"  + str(self.deposit))
        print("-------------")

class Student(Person):
    def __init__(self, id, name, score=0): # we can use different __init__ with parent's default __init__
        super(Student,self).__init__(id,name,i=10,d=30)
        self.score = score    # child instance variable 
    def sayGoodmorning(self):
        print(self.name + ": Good morning!!!")
    def showDetail(self):
        print("-----Student------")
        print("ID     :"  + str(self.id)       + "\n" \
              "Name   :"  + self.name          + "\n" \
              "Income :"  + str(self.income)   + "\n" \
              "Deposit:"  + str(self.deposit)  + "\n" \
              "Score  :"  + str(self.score))
        print("------------------")

a = Person(8,"Apple")
b = Person(2,"Banana")
c = Person(7,"Cathy", 5000)  #i=5000
d = Person(5,"Daku" , d=888) #d=888

s1 = Student(9,"Ren",87) #This 87 refer to "score" 

a.sayHi()
s1.sayHi()
s1.sayGoodmorning()

print(a)
print(b)
print(c)
print(d)
print(s1)

c.showDetail()
d.showDetail()
s1.showDetail() #Student type still have income and deposit instance variable

print("Total number of people:" + str(Person.count))
