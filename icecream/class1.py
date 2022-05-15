
class Table:

    menu = {
        'Strawberry':1.5,
        'Vanilla' :1.5,
        'Mango_Passion' :2,
        'Funky_Banana': 2,
        'Supa_Yogo': 2,

    }

    def __init__(self):
        self.items= []
        self.total= 0

    def add(self, x, y):
        self.items.append(x)
        self.total+= self.menu[x] * y
 
    def bill(self, tax):
        tax= tax * self.total
    
        for x in self.items:
            print(f'{x:20} ${self.menu[x]}')

        print(f'{"Total":20} ${self.total:.2f}')



def feed():
    global item
    global amount
    global reply
    item= input('What would you like to have please:\t').title()
    amount= input('How many please:\t')
    reply= input("Is that all you'll like to have (Y/N))")