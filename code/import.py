from packages.subpackage.human import Human

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
