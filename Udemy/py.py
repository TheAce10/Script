# # number=float(input("Enter kilometer to miles\t"))
# # k=1.609344
# # miles=number/k
# # print(f"{number}km = {round(miles,4)}mile(s)")

# #Strings
# Name="!@#$%^&*()"
# print(Name[0])
# print(Name[-1])
# Name[0:2]
# Nmae[-2:]
# len(Name)
# type(Name)
# #convert int to string
# num=123
# num=str(123)

# #math
# import math
# #round up numbers
# math.ceil(2.3)
# #round down numbers
# math.ceil(2.8)
# #factorial
# math.factorial(5)
# math.pi
# math.log(20)


# fname=input("Enter your first name")
# mname=input("Enter your middle name")
# lname=input("Enter your last name")
# print(fname[0],mname[0],lname[0])

# lotnumber="037-00901-00027"
# print("Country code:",lotnumber[0:3])
# print("Product code:",lotnumber[4:9])
# print("Product code:",lotnumber[10 :])

# import math
# r=float(input("Enter radius of your circle"))
# area= math.pi *(r**2)
# circumference= math.pi *2 *r
# print(f"Circumference= {circumference:.2f}\nArea={area:.2f}")

# #list
# students =["John", "Mary", "Steve","George","john", "steven", "stephen", "greg"]

# #tuple
# #are list that never change in relation to the real world
# #example months of the year
# months=("January","Febuary","March")

# #append method
# students.append("Kate")
# students.insert(0,"Peter")
# #removes last element
# students.pop()
# students.pop(1)
# students.remove("George")

# #Dictionaries
# Student={"Name":"Ace","ID":"202122","College":"Eng"}
# #list can be added to dictionaries
# Student["Courses"]=["DE","Calculus","Algebra"]
# #clear dictionary
# Student.clear()
# #get method
# #gets value and prints message if not availbale
# Student.get("Age","Not available")

score=int(input("Enter final exam score\t"))
if score<=70:
    print(f"you've scored an A\n Excellent")
elif score<=60:
    print("You've scored a B\n Very Good")
elif score<=50:
    print("You've scored a C\n Good")
elif score<=40:
    print("You've scored a D\n Pass")
elif score<=30:
    print("You've scored an E\n Credit")
else :
    print("You've scored an F\n Fail")

