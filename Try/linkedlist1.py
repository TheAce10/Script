from urllib.request import DataHandler
from linkedlist import Node, Linkedlist, Link

fnode = Node("ELL")
print(fnode.get_data())
snode = Node()
snode.set_data("LEL")
fnode.set_next(snode)
print(fnode.get_next())

a,b,c,d,e,f,g = Node(), Node(), Node(), Node(), Node(), Node(), Node()
a.set_data("Monday")
a.set_next(b)
b.set_data("Tuesday")
b.set_next(c)
c.set_data("Wednesday")
c.set_next(d)
d.set_data("Thursday")
d.set_next(e)
e.set_data("Friday")
e.set_next(b)
f.set_data("Saturday")
f.set_next(b)
g.set_data("Sunday")
g.set_next(None)
days = [a,b,c,d,e,f,g]
for day in days:
    print(f"{day.get_data()}")


# ll = Linkedlist()
# ll.head
# ll
# fnode = Node("Stan")
# ll.head = fnode
# snode = Node("Ama")
# fnode.next = snode
# print(ll)

# co=['a','b','c']
# bb = Link(co)
# print(bb)