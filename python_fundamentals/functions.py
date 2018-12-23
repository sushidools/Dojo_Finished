def a():
    return 5
print(a())
"""This will print 5 as the function returns 5 to where the function was called"""
##################################### 
def a():
    return 5
print(a()+ a())
"""This will print 10 as it calls the function and adds it to the call of the function"""
##################################### 
def a():
    return 5
    return 10 """This doesn't matter because of the return before it"""
print(a())"""This just prints 5"""
##################################### 
def a():
    return 5
    print(10)"""This again is never reached"""
print(a())  """SO it only prints the return 5"""
##################################### 
def a():
    print(5)
x = a()"When the function is called and run above it prints 5"
print(x)    "X does not have a return so when printed there is nothing to print" 
##################################### 
def a(b,c):
    print(b+c)"When the function is called it prints with the given parameters, but again no return so they cannot be added below"
print(a(1,2) + a(2,3))
#####################################
def a(b,c):
    return str(b)+str(c)"returns whatever b and c are concatenated"
print(a(2,5)) "This will print 25"
#####################################
def a():
    b = 100
    print(b)"When the function is called 100 will print"
    if b < 10:
        return 5
    else:
        return 10 "The else statement is read first so the return of 10 will be put back where the function is called"
    return 7
print(a()) "So here is where it will tell it to print the returned value of 10"
#####################################
def a(b,c):
    if b<c:
        return 7 "if this is true this is what will be returned"
    else:
        return 14 "else this will return"
    return 3 "this will never return"
print(a(2,3)) "This will print 7"
print(a(5,3)) "This will print 15"
print(a(2,3) + a(5,3))   "This will print the return of 7 + 14 or 21"
#####################################
def a(b,c):
    return b+c "only this return runs"
    return 10
print(a(3,5))  "Only prints 8"
#####################################
b = 500
print(b) "500 will print here"
def a():
    b = 300
    print(b) "The function when called will print 300"
print(b) "As the function is not called yet 500 will print again"
a() "Nothing returned"
print(b) "This will print 500 again."
#####################################
b = 500
print(b) "This will print 500"
def a():
    b = 300
    print(b)
    return b
print(b) "This will print 500"
a() "This will return 300 as it is what b is within the function"
print(b)  "This will still print 500"
#####################################
b = 500
print(b) "This will print 500"
def a():
    b = 300
    print(b) "When called this will print 300"
    return b
print(b) "This will print 500"
b=a() "B is now 300 as it was returned within the function"
print(b) "This will print 300"
#####################################
def a():
    print(1) "This prints 1"
    b() "calls function b but returns nothing"
    print(2) "This is printed after function b is finished so 2 is printed"
def b():
    print(3) "3 is printed right after 1"
a()"function is called but returns nothing"
#####################################
def a():
    print(1) "1 is printed"
    x = b() "5 was returned here"
    print(x) "5 is printed"
    return 10
def b():
    print(3) "3 is printed here"
    return 5 "5 is returned to x"
y = a() "goes up to run function a and returns 10 to y"
print(y) "so here after everything else 10 is printed"
