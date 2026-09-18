class Dog():
    def __init__(self,name,age):
        # name and age are the properties
        self.name = name # properies are saved using self
        self.age = age
    def bark(self):
        print(self.name + " says Woof!")

c1 = Dog("Tommy", 23) # object created
c1.bark() # method accessed
print(c1.age)


# Learning

# about "SELF" Parameter

# self is how an object keeps track of its own specific data
#so it doesn't get confused with other objects

#It literally means
#"the specific object I am working with right now."
