class Person():
    def __init__(self,name,age):
        # these are propeties (data/variables)
        self.name = name
        self.age = age
        
     # this is a method   
    def greet(self):
         print("Hello, my name is " + self.name)
p1 = Person("mohit", 25) # object created
p1.greet() # method is accessed
print(p1.name)  # property is accessed 



# learning
#1 "__INIT__ is a built in method, always executed when
#class is being initiated

#2 when object is created, this method is used to assign values to
#object properties.

# Object property means ? -> variables holding the data


#3 Why to Use __INIT__ ?
# if dont use, then need to set properties manually for each object.

#4 Default values of parameters in the __INIT__ method can be set

#5
