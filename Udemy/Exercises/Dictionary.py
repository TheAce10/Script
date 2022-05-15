Person={"name":"The Ace","gender":"M","age":"18","address":"KNUST","phone":"553994884"}

info=input("What would like to know about me?").lower()
print(f"My {info} is {Person.get(info,'Not available')}")