def hello():
    print("Hello, human!")

def pack(element1, element2, element3):
    return [element1, element2, element3]

def eat_lunch(list):
    if len(list) == 0:
        print("My lunchbox is empty :(")
    else:
        for i in range(len(list)):
            if i == 0:
                print(f"First, I eat {list[0]}")
            else:
                print(f"Next, I eat {list[i]}")

hello()
print(pack("item 1", "item 2", "item 3"))
eat_lunch([])
eat_lunch(["Apple"])
eat_lunch(["Sandwich", "Burrito", "Apple", "Cake"])

