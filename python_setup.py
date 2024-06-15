def hello():
    print("Greetings user")

def pack(a,b,c):
    return [a,b,c]


# I needed to look at solution code for the 3rd one. Still need to research what the f does before the "first I eat" and "next I eat"
def eat_lunch(list):
    if len(list) == 0:
        print("My lunchbox is empty")
    else: 
        for i in range(len(list)): 
         if i == 0:
          print (f"first I  eat {list[0]}")
         else:
          print(f"next I eat {list[i]}")

hello()
print(pack("a","b","c"))
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["pizza"])
eat_lunch(["pizza","water","dessert"])