#Question 1

# Greatest Common Divisor

#Function for gcd
def gcd(n1,n2):

    while n2 != 0:
        rem = n1 % n2
        n1 = n2
        n2 = rem
    return n1

#Taking input
n1=int(input("Enter first number\t"))
n2=int(input("Enter second number\t"))

#Result display
print(f"The GCD of {n1} and {n2} is {gcd(n1,n2)}\n")



#Question 2
#CONVERTING FROM DECIMALS TO BASES LESS THAN 10 

#Function Definition for base_conversion
def base_convert(num,b):
    q=int(num)
    k=0
    a=[]

    #loop to convert number
    while q != 0 and b>1:
        a.append(0)

        a[k] = q % b
        q = int(q / b)
        k += 1

    a.reverse()

    answer= ""
    for c in range(0,len(a)):
        answer= answer + str(a[c])

    return answer


print("Converting Decimal to Other Bases")
n=int(input("Enter integer to convert:\t"))
b=int(input("Enter base of conversion:\t"))
print(f"{n} in base {b} = {base_convert(n,b)}\n")


#ADDITION OF INTEGERS

#Function definition


def add(n1,n2,base):
    
    #Variable Declaration
    c= 0
    sum0=[]

    n1 = list(base_convert(n1,base))
    n1.reverse()

    n2 = list(base_convert(n2,base))
    n2.reverse()
    
    ind=0
    #For equal number digits
    if len(n1) == len(n2):
        ind= len(n1)
        for i in range(ind):
            rsum=((int(n1[i]) + int(n2[i]) + c))
            tmp = int((rsum / base))
            sum0.append(int(rsum - base * tmp))
            c= int(tmp)

        #For number1 having more digits than number2
    elif len(n1) > len(n2):
        ind= len(n2)

            #first we work with the length of the shorter number
        for i in range(ind):
            rsum=((int(n1[i]) + int(n2[i]) + c))
            tmp = int((rsum / base))
            sum0.append(int(rsum - base * tmp))
            c= int(tmp)
            
            #next we continue with the remaining digits of the longer number
        for i in range(ind,len(n1)):
            rsum=((int(n1[i]) + c))
            tmp = int((rsum / base))
            sum0.append(int(rsum - base * tmp))
            c= int(tmp)

        #For number2 having more digits
    elif len(n1) < len(n2):
        ind= len(n1)

            #first we work with the length of the shorter number
        for i in range(ind):
            rsum=((int(n1[i]) + int(n2[i]) + c))
            tmp = int((rsum / base))
            sum0.append(int(rsum - base * tmp))
            c= int(tmp)

            #next we continue with the remaining digits of the longer number
        for i in range(ind,len(n2)):
            rsum=((int(n2[i]) + c))
            tmp = int((rsum / base))
            sum0.append(int(rsum - base * tmp))
            c= int(tmp)

    if c>0:
            sum0.append(c)

    #Reverse sum back to the right order
    sum0.reverse()

    #Change sum in list form to string
    sum1=''
    for m in range(0,len(sum0)) :
        sum1= sum1 + str(sum0[m])
    
    return sum1



a=input("Enter two numbers to add\n1:\t")
b=input("\n2:\t")
c= 2
if c>0:
    print(f"  {a} + {b} (base {c}) = {add(a, b, c)}\n")
else: 
    print("Base cannot be zero or less")
