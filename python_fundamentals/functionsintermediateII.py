x = [ [5,2,3], [10,8,9] ] 

x[1][0] = 15
print(x)
######################################
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

students[0]['last_name'] = 'Bryant'
print(students)
##########################################
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)
########################################
z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print(z)
######################################
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iterateDictionary(x):
    for i in range(0, len(x)):
        first_name = x[i]['first_name']
        last_name = x[i]['last_name']
        full_line = 'first_name: ' + first_name + ' - ' + 'last_name: ' + last_name
        print(full_line)
        

iterateDictionary(students)
############################################
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iterateDictionary2(key, x):
    for i in range(0, len(x)):
        print(x[i][key])
    
iterateDictionary2('first_name', students)
####################################################
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printDojoInfo(dojo):
    for key, value in dojo.items():
        if key == 'locations':
            print(len(value), 'LOCATIONS')
            for i in value:
                print(i)
        print("\n")
        if key == 'instructors':
            print(len(value), 'INSTRUCTORS')
            for i in value:
                print(i)
printDojoInfo(dojo)        