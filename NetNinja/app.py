from pdb import line_prefix
from tkinter import Menu
from turtle import goto
from icecream.class1 import Table
from Try.linkedlist import Node

def feed():
    global item
    global amount
    global reply
    print(Table.menu)
    item= input('What would you like to have please:\t').title()
    amount= int(input('How many please:\t'))
    reply= input("Is that all you'll like to have (Y/N))")

item= ''
reply= ''
amount= 0
table1= Table()

amount=0
feed()
table1.add(item, amount)


x=0
while x==0:
    if reply== 'N':
        feed()
        table1.add(item, amount)
    else:
        break
    

table1.bill(0.1)
