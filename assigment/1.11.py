#Question 1
# Greatest Common Divisor

#Function definition for gcd
def gcd(num1,num2):

    while num2 != 0:
        temp = num1 % num2
        num1 = num2
        num2 = temp
    return num1

#Taking input
print("Finding Greatest Common Divisor")
num1=int(input("Enter first number\t"))
num2=int(input("Enter second number\t"))

#Function call and Result display
print(f"The GCD of {num1} and {num2} is {gcd(num1,num2)}\n")



#Question 2
#CONVERT FROM DECIMALS TO BASES LESS THAN 11

#Function Definition for numconvert
def numconvert(n,b):
    m=int(n)
    k=0
    a=[]

    #loop to convert number
    while m != 0 and b>1:
        a.append(0)

        a[k] = m % b
        m = int(m / b)
        k += 1

    a.reverse()

    num= ""
    for i in range(0,len(a)):
        num= num + str(a[i])

    return num

print("Converting Decimal to Other Bases")
num=int(input("Enter integer to convert:\t"))
base=int(input("Enter base of conversion:\t"))
print(f"{num} in base {base} = {numconvert(num,base)}\n")



#ADDITION OF INTEGERS

#Function definition


def add(num1,num2,base):
    
    #Variable Declaration
    x= 0
    sum0=[]

    num1 = list(numconvert(num1,base))
    num1.reverse()

    num2 = list(numconvert(num2,base))
    num2.reverse()
    
    index=0
    #For equal number digits
    if len(num1) == len(num2):
        index= len(num1)
        for i in range(index):
            rsum=((int(num1[i]) + int(num2[i]) + x))
            tmp = int((rsum / base))
            sum0.append(int(rsum - base * tmp))
            x= int(tmp)

        #For number1 having more digits than number2
    elif len(num1) > len(num2):
        index= len(num2)

            #first we work with the length of the shorter number
        for i in range(index):
            rsum=((int(num1[i]) + int(num2[i]) + x))
            tmp = int((rsum / base))
            sum0.append(int(rsum - base * tmp))
            x= int(tmp)
            
            #next we continue with the remaining digits of the longer number
        for i in range(index,len(num1)):
            rsum=((int(num1[i]) + x))
            tmp = int((rsum / base))
            sum0.append(int(rsum - base * tmp))
            x= int(tmp)

        #For number2 having more digits
    elif len(num1) < len(num2):
        index= len(num1)

            #first we work with the length of the shorter number
        for i in range(index):
            rsum=((int(num1[i]) + int(num2[i]) + x))
            tmp = int((rsum / base))
            sum0.append(int(rsum - base * tmp))
            x= int(tmp)

            #next we continue with the remaining digits of the longer number
        for i in range(index,len(num2)):
            rsum=((int(num2[i]) + x))
            tmp = int((rsum / base))
            sum0.append(int(rsum - base * tmp))
            x= int(tmp)

    if x>0:
            sum0.append(x)

    #Reverse sum back to the right order
    sum0.reverse()

    #Change sum in list form to string
    sum1=''
    for m in range(0,len(sum0)) :
        sum1= sum1 + str(sum0[m])
    
    return sum1


print("Performing integer addition")
a=input("Enter two numbers to add\nNum1:\t")
b=input("\nNum2:\t")
c=int(input("\nEnter Number base: "))
if c>0:
    print(f"  {a} + {b} (base {c})\n= {add(a, b, c)}")
else: 
    print("Base cannot be zero or less")
