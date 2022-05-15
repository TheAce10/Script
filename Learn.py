#Strings
name="Bless Elikem Krapah"
name.upper()
name.lower()
name.title()
favorite_language = ' python '
favorite_language = favorite_language.rstrip()
#.rstrip() removes whitespace from the right
print(favorite_language)
favorite_language = favorite_language.lstrip()
#.lstrip() removes whitespace from the left
print(favorite_language)
favorite_language = favorite_language.strip()
#.strip() removes whitespace from the both sides
#Lists
ab=[1,2,3,4,5]
ac=[2,4,6,8,10]
# List elements start from 0 representing the first num
ab[3]
ac[0:3]
ac[:3]
ab[1:]
#In python ranges the last value is considered a border
# (meaning it's not included in range)

ab.remove(5)
#.remove deletes the first occurence of variable
ab.append(5)
#.append add a variable to the end of list
del(ac[0:4])
#deletes specified variable

names=["Bless","Bubu","Steve"]
ages=[18,19,18]
Prog=["CpE","TcE","TcE"]
list=[names,ages,Prog]
print(list)
details= input()

print("Name:",names[1],"\n","Age:",
ages[1],"\n","Programme:",Prog[1])
print("Name:{0}\n Age:{1}\n Prog:{2}\n".format(names[2],ages[2],Prog[2]))  
print(f"Name: {names[0]}\nAge:{ages[0]}\nProg: {Prog[0]}")

#FORMATING METHODS
name00= "Bless"
name01= "Steph"
print("Name:",name00,'Name:',name01)
#FORMAT 1
print("name is {0} and name 2 is {1}".format(name00,name01))
rate00= 71.454368461
rate01= 71.325169185
print("rate 1 is {0:.5} and rate 2 is {1:.3f}".format(rate00,rate01))

#FORMAT 2
print(f"Name:     {name00}\nRate:     {rate00} \n Name is {name01} and rate is {rate01} ")

#INTEGER FORMAT
age = int(input("Enter your age\n"))

new= (f"My name is: {name00} Thank you")
print(new)


for i,m in zip_longest(num1,num2):

