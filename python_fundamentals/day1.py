"""for i in range(0, 151):
    print (i)

for i in range(5, 1000001):
    if i % 5 == 0:
        print (i)

for i in range(1, 101):
    if i % 5 == 0:
        print("Coding")
    if i % 10 == 0:
        print("Dojo")
    elif i % 5 != 0:
        print(i)

sum = 0
for i in range(0, 500000):
    if i % 2 != 0:
        sum = sum + i
print(sum)

for i in range(2018, 0, -4):
    print(i)

def flex(lowNum, highNum, mult):
    for i in range(lowNum, highNum + 1):
        if i % mult == 0:
            print(i)
        
flex( 2, 9, 3)
"""
list = [3,5,1,2]
for i in list:
    print(i)

"""
The above should print each value in the list
"""
list = [3,5,1,2]
for i in range(list):
    print(i)

"""
The above will give nothing as range needs to accept integers as the parameters not a list.
"""
list = [3,5,1,2]
for i in range(len(list)):
    print(i)

"""
The above will print the numbers in the range of the length of the list. SO the list is 4 numbers in length but the range starts at 0 so it will print 0, 1, 2, 3
"""