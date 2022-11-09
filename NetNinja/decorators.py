def deco(func):
    
    def just():
        #
        print("Loading From our server's")
        func()
        #
        print("Your download should start in 3 secs")
    return just

@deco
def load():
    num=[1,2,3,4,5,6,7,8,9,10,11]
    x=0
    while x<11:
        print(f"Importing {list(num[0:x])}...")
        x+=1

load()