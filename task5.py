items = {
    "weapon": "bow",
    "defense":  "shield",
    "armour":  "chainmail",
    "food": "magic apple"
}

itemsSorted = []
inventory = []
while True:
    print("----------------------------------------")
    print("you can choose to quit, drop items, get item, or see inventory.")
    print("----------------------------------------")
    A = input("input: ")
    if A == "quit":
        exit()
    if A == 'get item':  
        print(items)
        get = input("choose an item from their class: ")
        if get == "bow" or "shield" or "chainmail" or "magic apple":
            inventory.append(get)
            print(inventory)
        
    if A == "drop item":
        print(inventory)
        print("this is your inventory")
        drop = input("choose which item you would like to drop: ")
        if drop == "bow" or drop == "shield" or drop=="chainmail" or drop=="magic apple":
            a = inventory.index(drop)
            #find the index/position of the item you are trying to drop
            inventory.pop(a)
            print(inventory)
            
    if A == "see inventory":
        print(inventory)
        print("this is your inventory! you can add or drop items into your inventory")

    
        #all done i believe
       
