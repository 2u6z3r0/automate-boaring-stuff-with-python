#!/usr/bin/env python3
#Chapter 6 practice project

tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

def printTable(data):
    colWidth = [0] * len(tableData)
    for i in range(len(tableData)):
        for data in tableData[i]:
            if colWidth[i] < len(data):
                colWidth[i] = len(data)

    for j in range(len(tableData[0])):
        for i in range(len(tableData)):
            print(tableData[i][j].rjust(colWidth[i]+1), end='')
        print('')

printTable(tableData)