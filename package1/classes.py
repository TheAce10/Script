# from re import X


# class Planet:

#     def __init__(self):
#         self.name= 'Hoth'
#         self.radius= 200000
#         self.gravity=5.5
#         self.system='Hoth System'

#     def orbit(self):
#         return f'{self.name} is orbiting in the {self.system}'

# x= Planet()
# print(f"Name is {x.name}")
# print(f"Radius is {x.radius}")
# print(f"Gravity is {x.gravity}")
# print{x.orbit()}

# #since mercury is a new instance of Planet they share the same parameters
# mercury= Planet()

class Planet:

    shape="round"
    
    def __init__(self, name, radius, gravity, system):
        self.name= name
        self.radius= radius
        self.gravity= gravity
        self.system= system

    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'
    
    #Used to define class level functions
    @classmethod
    #These have access to only class level attribute
    def comm(xyz):
        return f'All planets are {xyz.shape} because of gravity'

    #Has access to only arguments passed onto it
    @staticmethod
    def spin(speed = '1 pile per hour'):
        return f'The planets spins at {speed}'


x= Planet('Mercury',1000000, 10.5, 'Solar System')
print(f"Name is {x.name}")
print(f"Radius is {x.radius}")
print(f"Gravity is {x.gravity}")
print(x.orbit())
print(Planet.shape)

print(Planet.comm())

print(Planet.spin('high speed'))










# class Ice_C:


#     Menu= {
#         "Strawberry_mini":1,
#         "Strawberry":1.5,
#         "Vanilla": 1.5,
#         "Chocolate": 1.5,
#         "Mango_passion":2,
#         "Funky_banana":2,
#         'Lemon':2
#     }

#     def __init__(self) -> None:
#         self.item=[]
#         self.price=0

#     def taken(self, item):
#         self.item.append(item)
#         self.price += self.Menu[item]

#     def printbill(self, service):
#         service= (service/100)*self.price
#         total= service + self.price