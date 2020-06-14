#!/usr/bin/env python3
#Chapter 6 practice project

tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    for i in range(len(tableData)+1):
        for j in range(len(tableData[0])-1):
            print(tableData[j][i], end = ' ')
        print() 

printTable(tableData)
