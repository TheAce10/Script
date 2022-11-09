#modules= files in python
#Packages= folders in python

#Importing methods from modules
from Loops import Planet

x= Planet('Mercury',1000000, 10.5, 'Solar System')
print(f"Name is {x.name}")
print(Planet.shape)
print(Planet.spin('high speed'))


#Importing methods from packages
# from package1.Functions import sumfact
# from package1.Functions import fact
#importing multiple methods
from package1.Functions import fact, sumfact
nn= fact(9)
nm= sumfact(90)