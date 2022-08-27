#It does not have to be named self , you can call it whatever you like, 
#but it has to be the first parameter of any function in the class:
from typing import Sequence


class Person:

  #Our constructor
  def __init__(self, name="", age=0):
    self.name = name
    self.age = age

  #Our methods
  def define(self):
      print("My name is "+str(self.name)+" and my age is "+str(self.age))
  def happy(self):
      print("I am a happy person")

p1 = Person("John", 36)
p2 = Person()

print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)
p1.define()
p2.define()
p2.name="Sarah"
p2.age=20
print(p2.name)
print(p2.age)
p2.define()

#You can delete properties on objects by using the del keyword:
del p1.age

#You can delete objects by using the del keyword:
del p1

#class definitions cannot be empty, but if you for some 
#reason have a class definition with no content, put in the pass statement to avoid getting an error.
class Empty:
    pass

e=Empty()

#Inheritance in classes
'''class Student(Person):
    pass


s1=Student("Farah",17)
s1.define()
'''

#Add the __init__() function to the Student class:
#When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
#Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
#To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

'''class Student(Person):
  def __init__(self, name, age):
    Person.__init__(self, name, age)

s1=Student("Farah",17)
s1.define()
'''

#Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
class Student(Person):
  def __init__(self, name, age,gpa):
    super().__init__(name, age) #Becareful ,here no self passing, you just pass the parameters
    #Add a property called graduationyear to the Student class:
    self.gpa=gpa
    self.__university="Cairo" #Private variable only accessible through methods

  def setUni(self,university):
      self.__university=university

  def getUni(self):
      print(self.__university)

  def welcome(self):
      print("Welcome "+self.name+" your age is "+str(self.age)+" and your GPA is "+str(self.gpa))
  def happy(self):
      print("I am a happy student")
  #If you add a method in the child class with the same name as a function in the parent class,
  # the inheritance of the parent method will be overridden.
  def define(self):
      print("My name is "+str(self.name)+" and my age is "+str(self.age)+" my GPA is "+str(self.gpa))

s1=Student("Farah",17,4)
s1.define()
s1.welcome()
s1.__university="MUST"
#print(s1.__university) not seen in the output as it is a private variable
s1.getUni()
s1.setUni("MUST")
s1.getUni()
s1.happy()
p2.happy()
#Using OOP in Python, we can restrict access to methods and variables. This prevents data from direct modification which
# is called encapsulation. 
#In Python, we denote private attributes using underscore as the prefix i.e single _ or double __


#Polymorphism allows the same interface for different objects, so programmers can write efficient code.
class Parrot:

    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

# common interface
def flying_test(bird):
    bird.fly()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)

#In the above program, we defined two classes Parrot and Penguin. Each of them have a common fly() method.
# However, their functions are different.
#To use polymorphism, we created a common interface i.e flying_test() function that takes any object and 
##calls the object's fly() method. Thus, when we passed the blu and peggy objects in the flying_test() function,
# it ran effectively.

class TrieNode:
    def __init__(self):
        self.children=[None]*4
        self.EndofSequence=False

class Trie:
    def __init__(self):
        self.root= self.getNode()

    def getNode(self):
        return TrieNode()

    def _myIndexGuide(self,character):
        if character=='A':
            return 0
        elif character=='C':
            return 1
        elif character=='G':
            return 2
        else:
            return 3
    
    def insert(self,sequence):
        length=len(sequence)
        MyNode=self.root
        for i in range(length):
            index=self._myIndexGuide(sequence[i])
            if not (MyNode.children[index]):
                MyNode.children[index]=self.getNode()
            MyNode=MyNode.children[index]
        MyNode.EndofSequence=True

    def search(self,sequence):
        MyNode=self.root
        length=len(sequence)
        for i in range(length):
            index=self._myIndexGuide(sequence[i])
            if not(MyNode.children[index]):
                return False
            MyNode=MyNode.children[index]
        return MyNode.EndofSequence

myTrie=Trie()
print(myTrie.search("CGA"))
myTrie.insert('AA')
myTrie.insert('AA')
myTrie.insert('TC')
myTrie.insert('TCG')
myTrie.insert('CGA')
myTrie.insert('AC')
print(myTrie.search("AA"))    
print(myTrie.search("AAA"))
print(myTrie.search("AAAA"))
print(myTrie.search("TC"))
print(myTrie.search("TCA"))
print(myTrie.search("CGA"))
print(myTrie.search("CGAA"))
print(myTrie.search("AC"))
print(myTrie.search("ACC"))

