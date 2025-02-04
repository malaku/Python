# Day 42: Encapsulation
class Person:
    __name="Geeks"
    __age= 10
    def get_name(self):
        print(Person.__name)
    def get_age(self):
        print(Person.__age)
    def set_name(self, name):
        Person.__name=name
    def set_age(self, age):
        Person.__age=age
# Define the Person class
person = Person() # Person Object Created
person.get_name() # Default value "Geeks" returned
person.set_name("John") # name value set to "John"
person.set_age(21) # age value set to 21
person.get_name() # "John" returned
person.get_age() # 21 returned

#{
 # Driver Code Starts.


# Function to parse function calls similar to parseFunction in Java