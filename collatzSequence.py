# Chapter 3 exercise

def collatzSequence(num):
    if num % 2 == 0:
        return num // 2
    else:
        return 3 * num + 1

print('Enter number:')
number = int(input())

while number != 1:
    number = collatzSequence(number)
    print(number)
