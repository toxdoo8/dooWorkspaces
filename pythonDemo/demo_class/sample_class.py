#one.py

class NameOfClass():

    def __init__(self,param1,param2):
        self.param1 = param1
        self.param2 = param2

    def some_method(self):
        #perform some action
        print(self.param1)
        print(self.param2)

class Sample():
    pass
#create a object
my_sample = Sample()
print(type(my_sample))

class Dog():
    def __init__(self,breed):
        # Attributes
        # We take in the argument
        # Assign it using self.attribute_name
        self.breed = breed

myDog = ['Lab','Huskie']

for breedType in myDog:
    print('Dog breed type: ',breedType)
    my_dog = Dog(breed=breedType)
    print(type(my_dog))
    print(my_dog.breed)
    print('\n')
print('======================================\n')

class Dog2():
    #CLASS OBJECT ATTRIBUTE
    # SAME FOR ANY INSTANCE OF A CLASS
    species = 'mammal'

    def __init__(self,breed,name,spots):
        # Attributes
        # We take in the argument
        # Assign it using self.attribute_name
        self.breed = breed
        self.name = name

        #expected to be a boolean
        self.spots = spots

    def bark(self):
        print('WOOF! My name is {}'.format(self.name))

my_dog = Dog2(breed='lab',name='Sammy',spots=False)
print('The dog type is ',my_dog.breed,'. The dog name is ',my_dog.name,'!!!')
print('My dog has spots: ',my_dog.spots)
print('My dog classify as:',my_dog.species)

print('======================================\n')
class Dog3():
    #CLASS OBJECT ATTRIBUTE
    # SAME FOR ANY INSTANCE OF A CLASS
    species = 'mammal'

    def __init__(self,breed,name):
        # Attributes
        # We take in the argument
        # Assign it using self.attribute_name
        self.breed = breed
        self.name = name

    def bark(self,number):
        print('WOOF! My name is {} and the number is {}'.format(self.name,number))

my_dog = Dog3('lab','Scott')
print('The dog3 type is ',my_dog.breed,'. The dog3 name is',my_dog.name,'!!!')
my_dog.bark(10)