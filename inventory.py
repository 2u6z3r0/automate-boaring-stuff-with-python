#!/usr/bin/python3
#chapter 5 exercise

stuff = {'gold coin': 42, 'rope': 1}

def displayInventory(stuff):
    '''
    :param stuff: It takes a dictionary of item name as key and its quantity as value
    :return: Nothing, but it prints all items and respective quantity and total quantity(sum of all itmes qty)
    '''

    print("Inventory:")
    totalCount = 0
    for k, v in stuff.items():
        print(v,k)
        totalCount += v
    print('Total number of items ' + str(totalCount))

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addItems):
    '''
    This function takes existing inventoy(dict) and new items to be added to inventory.
    :param inventory: existing inventory(dictionay of item_name:qty)
    :param addItems: list of items to be added to existing inventory
    :return: updated inventory dict by adding new items or if item exists already, qty will be increased by 1
    '''
    for item in addItems:
        inventory.setdefault(item, 0) #initialize qty to 0 if item does not exist already
        inventory[item] += 1
        
addToInventory(stuff, dragonLoot)
displayInventory(stuff)

