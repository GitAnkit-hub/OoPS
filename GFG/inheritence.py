class Person():
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def printname(self):
        print(self.firstname +" " +  self.lastname)

p1 = Person("mohit","gupta")
p1.printname()


# Creatig a child class

class Student(Person): # passed a class name to make this class a child class
    pass

# now the student class has same properties and methods
# as person class

x = Student("Rohit Kumar", "Gupta")
x.printname() # child class object can access the method of the
# parent class

print(x.firstname)
 # child class is able to access the properties




 # Add the __INIT_() Function

 # adding the __init__()function to child class,
 # it is now no longer inherits the parent __init__() function
 # remember  -only _init_function is not accessible
 #other methods are accessible

 #NOTE: The child's __init__() function overrides
 #the inheritance of the parent's __init__() function.


class Student1(Person):
     def __init__(self, fname, lname):
         self.fname = fname
         self.lname = lname

s1 = Student1("Mohit Kumar", "Gupta")
#s1.printname()
# Error : AttributeError: 'Student1' object has no attribute 'firstname'
# Cancelling the inheritence= = overriding
# child method overrides the parent's method

## The inherited printname() looks for self.firstname,
#which no longer exists.

# adding __init__ only cancels the parent __INIT__ method.
# rest of the methods of parent class are accessible.


class Student1(Person):
     def __init__(self, firstname, lastname):
         self.firstname = firstname
         self.lastname = lastname

s1 = Student1("Mohit Kumar", "Gupta")
#s1.printname()  # Works perfectly
# but need to keep same attribute name

## The inherited printname() looks for self.firstname,
#which actually exists in the child class.











# to keep the inheritence of the parent__init__() function,
# add a call to parent's __init() function.




class Student2(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

s1 = Student2("Nitin", "Gupta")
#s1.printname()





# Use the Super() Function

# makes the child class inherit all the methods and
# properties from its parent.

# by using super, you do not have to use the name of parent element
# automatically inherits the methods and properties from its parent


class Student3(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname) # No Self
        
s1 = Student3("Ankit", "Agrawal")
s1.printname()





# Add Properties

class Student4(Person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
        self.graduationyear = 2019
s1 = Student4("ankit", "agrawal")
print(s1.graduationyear)    





# 






