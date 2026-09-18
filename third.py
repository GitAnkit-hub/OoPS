# Properties belong to a class

#Properties stores the data for each object


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 = Person("Mohit", 23)
print(p1.age)
p1.age = 25   # value of a property can be modified
print(p1.age)

# delete property
#del p1.age        # property can be deleted

print(p1.age)

# previously it was object itself

del p1
#print(p1.name)


# Instance Property Vs Class Property

# Instance Property -> inside __INIT__
# its like employee's personal ID card
# Everyone one one
# but data on it is unique

# Class Property -> outside the methods
# its like office building's address
# every employee shares the exact same address



class Employee:
    # CLASS PROPERTY: Shared by every object
    company_name = "TechCorp"

    def __init__(self, name):
        # INSTANCE PROPERTY: Unique to this specific object
        self.name = name

# Create two different employees
emp1 = Employee("Alice")
emp2 = Employee("Bob")

# 1. Accessing their unique Instance Properties
print(emp1.name)  # Prints: Alice
print(emp2.name)  # Prints: Bob

# 2. Accessing the shared Class Property
print(emp1.company_name)  # Prints: TechCorp
print(emp2.company_name)  # Prints: TechCorp





emp1.company_name = "NewCorp"
print(emp1.company_name)  # NewCorp

print(emp2.company_name)  # techCorp (still same)

#to change the  class property for evert object,
# use class name instead object name

Employee.company_name = "NTRO"

print(emp1.company_name) # shows NewCorp
# above happens bkz
#Python checks Step 1: Does emp1 have a personal property
#called company_name ? Yes, it has "NewCorp"

#Python prints it and stops looking
#It never even reaches Step 2 to see "NTRO".
print(emp2.company_name)  # NTRO



# do delete the proprty if you want to see the class property

del emp1.company_name
print("emp1", emp1.company_name)









    
