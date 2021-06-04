num1 = 42 #declare and set int variable
num2 = 2.3 #declare and set float variable
boolean = True #declare and set boolean variable
string = 'Hello World' #declare and set string variable
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #declare and set list variable
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #declare and set dictionary variable
fruit = ('blueberry', 'strawberry', 'banana') #declare and set a tuple variable
print(type(fruit)) #print variable type of fruit
print(pizza_toppings[1]) #print index 1 of pizza_toppings list
pizza_toppings.append('Mushrooms') #add 'Mushrooms' to end of pizza_toppings list
print(person['name']) #print value at key 'name' in dictionary person
person['name'] = 'George' #set value at key 'name' in dictionary person to value 'George'
person['eye_color'] = 'blue' #set value at key 'eye_color' in dictionary person to value 'blue'
print(fruit[2]) #print index 2 of fruit tuple

if num1 > 45: #checks if num is greater than 45
    print("It's greater") #print "It's greater"
else: #if condition not met, run this code block
    print("It's lower") #print "It's lower"

if len(string) < 5: #checks if length of string is less than five
    print("It's a short word!") #print "It's a short word!"
elif len(string) > 15: #checks if length of string is greater than fifteen
    print("It's a long word!") #print "It's a long word!"
else: #if other conditions are not met, run this code block
    print("Just right!") #print"Just right!"

for x in range(5): #for loop where x will go from 0 through 4
    print(x) #print value of x
for x in range(2,5): #for loop where x will go from 2 through 4
    print(x) #print value of x
for x in range(2,10,3): #for loop where x will go from 2 through 9 in increments of three
    print(x) #print value of x
x = 0 #set x equal to zero
while(x < 5): #while loop with condition x is less than 5
    print(x) #print value of x
    x += 1 #increment x by 1

pizza_toppings.pop() #remove last item from pizza_toppings list
pizza_toppings.pop(1) #remove item in index 1 from pizza_toppings list

print(person) #print person dictionary
person.pop('eye_color') #remove key and value at key 'eye_color' from person dictionary
print(person) #print person dictionary

for topping in pizza_toppings: #for loop for each key as 'topping' in pizza_toppings
    if topping == 'Pepperoni': #checks if topping equals 'Pepperoni'
        continue #goes to next value in for loop
    print('After 1st if statement') #print 'After 1st if statement'
    if topping == 'Olives': #checks if topping equals 'Olives'
        break #break for loop

def print_hello_ten_times(): #define function print_hello_ten_times
    for num in range(10): #for num in range 0 through 9
        print('Hello') #print 'Hello'

print_hello_ten_times() #run function print_hello_ten_times

def print_hello_x_times(x): #define function print_hello_x_times with argument x
    for num in range(x): #for num in range from 0 to argument x
        print('Hello') #print 'Hello'

print_hello_x_times(4) #runs function with print_hello_x_times with argument 4

def print_hello_x_or_ten_times(x = 10): #define function print_hello_x_or_ten_times with argument x or x is None, x=10
    for num in range(x): #for num in range from 0 to argument x
        print('Hello') #print 'Hello'

print_hello_x_or_ten_times() #run function with argument x=10
print_hello_x_or_ten_times(4) #run function with argument x=4


"""
Bonus section
"""

# print(num3) #NameError: name 'num3' is not defined
# num3 = 72 #set int variable to 72
# fruit[0] = 'cranberry' #set index 0 in list fruit
# print(person['favorite_team']) #TypeError: object has no attribute
# print(pizza_toppings[7]) #list index out of range
# print(boolean) #print True
# fruit.append('raspberry') #no append attribute on a tuple object
# fruit.pop(1) #no pop attribute on a tuple object