def biggie_size(*arr):
    new_arr = []
    for i in range(0, len(arr)):
        if(arr[i] > 0):
            new_arr.append('big')
        else:
            new_arr.append(arr[i])
    print(new_arr)
    
biggie_size(2,3,-4,1,-2,2)
########################################
arr = [3,2,1,-5,2,1,3]
def countPositives(arr):
    cnt = 0
    for index in range(0, len(arr)):
        if arr[index] > 0:
            cnt = cnt + 1
        else:
            arr[index] = arr[index]
    arr[len(arr)-1] = cnt
    print(cnt)
    return arr
print countPositives(arr)
########################################
arr = [1,2,3,4]
def arr_sum(arr):
    result = 0
    for i in range(0 , len(arr)):
        result += arr[i]
    return result
print(arr_sum(arr))
#######################################
arr = [1,2,3,4,5]
def avg(arr):
    result = 0
    for i in range(0, len(arr)):
        result += arr[i]
    average = result / float(len(arr))
    return average

print (avg(arr))
#########################################
arr = [4,2,3,4,5,6,2]
def find_len(arr):
    count = 0
    for i in arr:
        count += 1
    return count

print(find_len(arr))
######################################
arr = [2,1,-4,3,4,-2]
def find_min(arr):
    mini = arr[0]
    if len(arr) == 0:
        return False
    if len(arr) > 0:
        for i in arr:
            if arr[i] < mini:
                mini = arr[i]
    return mini

print(find_min(arr))
#######################################
arr = [2,5,-1,-2,5,-6,9]
def find_max(arr):
    maxi = arr[0]
    if len(arr) == 0:
        return False
    if len(arr) > 0:
        for i in range(0, len(arr)):
            if arr[i] > maxi:
                maxi = arr[i]
    return maxi

print(find_max(arr))
#####################################
arr = [1,4,6,7,2,4]
def ultAn(arr):
    new_ult = []
    maxi = arr[0]
    mini = arr[0]
    count = 0
    result = 0

    for i in arr:
        count += 1

    new_ult.append(count)
    if count == 0:
        return False
    for i in range(0, count):
        if arr[i] > maxi:
            maxi = arr[i]
        if arr[i] < mini:
            mini = arr[i]
        result += arr[i]
    new_ult.append(result)
    new_ult.append(maxi)
    new_ult.append(mini)
    new_ult.append(int(result/count))
    return new_ult

print(ultAn(arr))
#######################################
arr = [1,2,3,4,5]
def rev(arr):
    l = len(arr)
    s = l
    new_arr = [None]*l
    for i in arr:
        s = s -1
        new_arr[s] = i
    return new_arr

print(rev(arr))