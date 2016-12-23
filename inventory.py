#!/usr/bin/python3

stuff = {'gold coin': 42, 'rope': 1}

def displayInventory(stuff):
    print("Inventory")
    totalCount = 0
    for k, v in stuff.items():
        print('{} {}'.format(str(v), k))
        totalCount += v
    print('Total number of items : {}'.format(totalCount))

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addItems):
    for item in addItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
        
addToInventory(stuff, dragonLoot)
displayInventory(stuff)

