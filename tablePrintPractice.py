#!/usr/bin/env python3

tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

colWidth = [0] * len(tableData)
for i in range(len(tableData)):
    for data in tableData[i]:
        # print(data)
        # print('{}----{}'.format(colWidth[i], len(data)))
        if colWidth[i] < len(data):
            colWidth[i] = len(data)

# print(colWidth)
# for j in range(len(tableData[i])):
#     print(str(tableData[0][j]).ljust(colWidth[0]+1)+str(tableData[1][j]).ljust(colWidth[1]+1)+str(tableData[2][j]).ljust(colWidth[2]+1))

for j in range(len(tableData[0])):
    for i in range(len(tableData)):
        print(tableData[i][j].ljust(colWidth[i]+1), end='')
    print('')