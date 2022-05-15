# print("Finding GCD using Euclidean Algorithm")
# num1=int(input("Enter first number\t"))
# num2=int(input("Enter second number\t"))

# num3=num1
# num4=num2
# while num4!=0:
#     temp=num3 % num4
#     num3=num4
#     num4=temp
# print(f"The GCD of {num1} and {num2} is {num3}")



# base1= []
# index = -1
# answer = ""
# decimal= int(input("Enter decimal to convert\t"))
# numbase= int(input("Enter base to convert to\t"))
# a=0
# k=0
# dec=decimal
# while dec > 0:
#     a= int(dec % numbase)
#     base1.append(a)
#     dec= (dec-a)/numbase

# for i in base1:
#     answer += str(base1[index])
#     index-=1
# #print(base1[index],end="")
# print(f"Decimal {decimal} in base {numbase} is {answer}")




num1= input("Enter first number: ")
num2= input("Enter second number: ")
base1= int(input("Enter the number base: "))
a=[]
b = []
# for i in range(0,len(num1)):
#     a.append(int(num1[i]))
# print(a)

a_prime  = []
b_prime  = []
indexa = -1
indexb = -1

a = [int(num1[i]) for i in range(0,len(num1))]
print(a)
for i in a:
    a_prime.append(a[indexa])
    indexa -= 1
print(a_prime)

b = [int(num2[i]) for i in range(0,len(num2))]
print(b)
for i in b:
    b_prime.append(b[indexb])
    indexb -= 1
print(b_prime)

ans=[]
carry= 0
while base1>0:
    if len(a_prime)<len(b_prime):
        rng=len(a_prime)
    else: 
        rng=len(b_prime)

    for i in range(0,rng):
        add =carry + a_prime[i] + b_prime[i]
        tmp= add % base1
        carry= (add-tmp)/base1
        ans.append(tmp)

print(ans)


# for i in range(0,len(num2)):
#     b.append(int(num2[i]))
# print(b)
# ara=[]
# ar2=[]

#

