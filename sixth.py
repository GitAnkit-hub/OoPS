#Remember that __INIT__ is used to setup the initial data(proprties)
# the moment an object is created.
 #in the below code, the Calculator odesn't need to remember any
# personal data or state.

#What will be the result of the following code:
class Calculator:
  def add(self, a, b):
      return a + b

calc = Calculator()
print(calc.add(5, 3))

#is this correct code, as it does not have the init method ?

# this works, as there is no starting data to set up


class Rectangle():
    def area(self,width,height):
        return width * height
r1 = Rectangle()
print(r1.area(5,3))
