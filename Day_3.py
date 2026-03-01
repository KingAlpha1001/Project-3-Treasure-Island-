# If Else Statment
'''
Template
if condition:
    do this
else:
    do this
'''

print("Good morning welcome to the Velocihulkrockit Coaster")
height = int(input("What is your height in cm: "))


if height > 120:  # Checks if your height is greater than 120.
    print("Enjoyyy") # This is going to be the output if the height of 
    #me over 120 cm and it should be indented like this "     " to make sure it works
else: # This should not be indented or it will not work
    print(" Get Out!!!!") # This is the result if your height is below 120cm

'''
Comparison Operators
> : Greater Than
< : Less Than
==: Equal To
!=: Not Equal To 
>=: Greater Than Equal To
<=: Less Than Equal To 
'''



# Modulo Operator: %

print(10/3) # This is just dividing 10 by 3
print(10%3) # This is and looks like a percentage sign but it
# actually works out the remainder of the answer and it is a new operator


# Find out if the number input by the user is even or odd

print("The Odd or Even teller")
no = int(input("Kindly give yor number: "))

if no % 2 == 0:
    print("EVEN!!!!!!!")
else:
    print("ODD!!!!!!!")





# Nested If Else Statement (Basically a if else in a if else)
# And Elif: Elif is basically another if but with a condition unlike else

print("Good morning welcome to the Velocihulkrockit Coaster II")
height_person = int(input("What is your height in cm: "))


if height_person > 120:  
    print("Enjoyyy") 
    age = int(input("What Is Your Age: "))
    if age <= 12: 
        print("Pay $5 and enjoy the death coaster")
    elif age <= 18:
        print("Pay 100")
    else:
        print(" Oh! You are a oldie. Pls go its free")  

    photo = input(" U want a photo y or n")

    if photo == "y":
        print("$100 More")
else: 
    print(" Get Out!!!!") 



# Pizzeria

print("Hello welcome to Pizzeria")
Size = input(''' What Size pizza do you want:
Small: $15
Medium: $20
Large: $30            
Type S M L: ''')
Toppings = input("Do you want mushroom + $2 y or n")
Cheese = input("Do u want a looooot of cheese + $1100 y or n")


bill = 0
if Size == "S":
    bill += 15
elif Size == "M":
    bill +=20
elif Size == "L":
    bill += 30
else:
    print("Invalid Input")

if Toppings == "y":
    if Size == "S":
        bill += 2
    else:
        bill += 8


if  Cheese == "y":
    bill += 1100

print(f"Please Pay ${bill}")






#Logical Operators
# There are 3 logical operators and they are "and, or, not"
'''Logical Operators
Up to this point, we have used if statements, else statements, elif statements,
multiple if statements, as well as nested if statements. However, 
we have not yet been able to check for multiple conditions in the same line of code.

Combining Multiple Conditions
How can we combine different conditions and, for example, check if the pizza 
is large, the user wants pepperoni, and extra cheese all in the same line of code? 
To do this, we need to learn about logical operators.

There are three logical operators that are particularly useful: and, or, and not.

The and Operator
When you combine two different conditions using the and operator, both conditions 
must be True for the entire line of code to be True. If just one of them is 
 and the other is False, then the overall statement evaluates to False.'''

a = 12
print(a > 15)  # False
print(a > 10)  # True
print(a > 10 and a < 13)  # True
print(a > 15 and a < 13)  # False

'''In the example above, when both conditions are True, the statement 
evaluates to True. When just one of them is False, the result is False. Using the 
and logical operator, it checks two conditions to see if they are both True. If they are, 
 final outcome is True. If either is False, the result is False.'''

'''The or Operator
If you only need one of the conditions to be True, you can use the or operator instead.
If either condition is True, or if both are True, the statement evaluates to True.
It is only when both conditions are False that the statement becomes False.'''

a = 12
print(a > 10 or a < 10)  # True

'''
In this case, one condition is True and the other is not True, but because we use or, 
the result is True. 
So, True or True becomes True, True or False becomes True, False or True becomes True, 
and only False or False results in False. This is quite different from the and operator.

'''

'''
The not Operator
The not operator reverses a condition. If the condition is False, it becomes True. 
If it is True, it becomes False.'''



a = 12
print(a < 0)  # False
print(not (a < 0))  # True

''' Here, a < 0 evaluates to False, but putting not in front of it reverses the condition,
so it becomes True. not False is True, and not True is False.
'''

