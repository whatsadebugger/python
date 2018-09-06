class Human:

    # A class attribute. It is shared by all instances of this class
    species = "H. sapiens"

    def __init__(self, name, age):
        # Assign the argument to the instance's name attribute
        self.name = name

        # Initialize property
        self._age = age 

    # An instance method. All methods take "self" as the first argument
    def say(self, msg):
        print("{name}: {message}".format(name=self.name, message=msg))

    # Another instance method
    def sing(self):
        return 'I cant'

    # A class method is shared among all instances
    # They are called with the calling class as the first argument
    @classmethod
    def get_species(cls):
        return cls.species

    # A static method is called without a class or instance reference
    @staticmethod
    def grunt():
        return "*grunt*"

    # A property is just like a getter.
    # It turns the method age() into an read-only attribute of the same name.
    # There's no need to write trivial getters and setters in Python, though.
    @property
    def age(self):
        return self._age

    # This allows the property to be set
    @age.setter
    def age(self, age):
        self._age = age

    # This allows the property to be deleted
    @age.deleter
    def age(self):
        del self._age


# When a Python interpreter reads a source file it executes all its code.
# This __name__ check makes sure this code block is only executed when this
# module is the main program.
if __name__ == '__main__':
    # Instantiate a class
    i = Human("ahmad", 24)
    i.say("hi")
    
    # i is an instances of type Ahmad, or in other words: an Ahmad object

    # Call our class method
    i.say(i.get_species())          # "Ahmad: H. sapiens"
    # Change the shared attribute
    Human.species = "H. neanderthalensis"
    i.say(i.get_species())          # => "Ahmad: H. neanderthalensis"


    # Call the static method
    print(Human.grunt())            # => "*grunt*"


    # Update the property for this instance
    i.age = 200
    # Get the property
    i.say(i.age)                    # => "Ahmad: 200"
    # Delete the property
    del i.age
    # i.age                         # => this would raise an AttributeError
