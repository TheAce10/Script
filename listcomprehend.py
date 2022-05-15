# #double prize money weekend bonanza
# prizes = [5, 10, 50, 100, 1000]

# db_prizes=[]
for x in prizes:
    db_prizes.append(x*2)

print(db_prizes)

#comprehension method
db_prizes= [prize*2 for prize in prizes]
print(db_prizes)

#squaring numbers
nums =[1, 2, 3, 4, 5, 6, 7, 8, 9,10]

sq_even= []
for num in nums:
    if(num) % 2 ==0:
        sq_even.append(num ** 2)
print(sq_even)

#Comprehension Method

sq_even =[(num**2) for num in nums if(num) % 2 ==0]
print(sq_even)
