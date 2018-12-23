def countDown(num):
    for i in range(num, -1, -1):
        print(i)

countDown(5)
####################################
def PReturn(num1, num2):
    print(num1)
    return num2

y = PReturn(1, 2)
print(y)
####################################
def first_plus_length(*arr):
    if len(arr) > 1:
        return arr[0] + len(arr)

y = first_plus_length(1,2,3,4,5)
print(y)
####################################
def values_greater_than_second(*arr):
    counter = 0
    arr = []
    for i in arr:
        if len(arr) == 1:
            return False
        if len(arr) > 1:
            if arr[i] > arr[1]:
                arr.append(arr[i])
                counter += 1
    print(arr)
    return counter
y = values_greater_than_second(1,2,3,4,5)
print(y)
#######################################
def greater(*arr):
    sub_arr = []
    count = 0
    if (len(arr) > 1):
        for i in arr:
            if(i > arr[1]):
                sub_arr.append(i)
                count += 1
        print(count)
        return sub_arr
    else:
        return False

greater(2,2,3,4,1,2)
#################################
def this_that(num1, num2):
    sub_arr = []
    if num1 == num2:
        print('Jinx')
    for x in range(0, num1):
        sub_arr.append(num2)
    return sub_arr

y = this_that(3, 5)
print(y)