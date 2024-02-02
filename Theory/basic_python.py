"""
        Variables: variable_name = value -> type automatically infer

    Python is a dynamically typed language that means it isn't needed to specify the variable
type when you declare it( such as: C language -> int a = 4; Java -> boolean isHiring = false).
The Python Interpreter is the one who is responsible to assign types to variable at the runtime
(the time when the program is running -> we pressed Run button)

"""

name = "Alex"  # str: string/char
age = 24  # int: number/integer
height = 1.73  # float
isHired = True  # boolean: 2 possible values -> True/ False
my_list = ["Alex", 24, isHired, False]  # list
position = (45, 50)  # tuple
car = {
    "brand": "Mazda",
    "model": "Mazda3",
    "year": 2020
}  # dictionary


"""
        IF Statement - Conditional Statement

    When you should to make a choice based on a condition, you need to use an IF statement. You evaluate the
condition and take a decision based on the evaluation result: True/ False. 

Let's think at a real situation: you're at home and a friend is calling you about going with the bikes. In this 
moment, you should decide if you're going or not, based on your mood: if you are or not tired -> the condition:
IF you're not tired, you're going; ELSE you're not going:
    
    * Translate it into code:
        tired = False
        if not tired:
            going_with_bike()  # this line will execute because: not tired == True
        else:
            stay_home_and_sleep()  # this line will be ignore

"""

if isHired:
    print("isHired value is: ", isHired)

###############################################################################

if age >= 18:
    print("You are able to drive a car!")
else:
    print("You need to wait until you turn 18 years old :((")

###############################################################################

your_money = 250  # is an int variable
playstation5 = 500   # is an int variable
controller = 129.99  # is a float variable

if playstation5 + controller <= your_money:
    print("Yes, you can bought both!")
elif playstation5 < your_money:
    print("You can buy only the playstation 5!")
elif controller < your_money:
    print("You can buy only the controller!")
else:
    print("Sorry, but you can buy nothing...")


# Loops Statements:

"""
        While Loop
        
    
"""

isGameOver = False
life = 5
number_to_guess = 97

while not isGameOver and life > 0:
    your_choice = int(input("Give me a number: "))
    if your_choice < number_to_guess:
        life -= 1
        print("Choose a greater number!")
    elif your_choice > number_to_guess:
        life -= 1
        print("Choose a smaller number!")
    else:
        isGameOver = True
        print("Congratulations, you won the game!")

    if life == 0:
        print("Sorry, you are dead... :((")


"""
        For Loops
    
    When it comes about for loops we must answer to this question: We need to know the elements' position in the list
or is enough the elements' value?

    * If the answer is the first option: we need the elements' position, we should use this type of for loop:
        
        gamesWishList = ["Minecraft", "Roblox", "Fifa", "GTA VI"]
        how_many_elements_in_the_list = len(gamesWishList)  # the argument for the range function
        
        for index in range(how_many_elements_in_the_list):
            print("Element position: "+ str(index), end='; ')
            print("Element value: " + gamesWishList[index])
            
            *Result: 
                Element position: 0; Element value: Minecraft
                Element position: 1; Element value: Roblox
                Element position: 2; Element value: Fifa
                Element position: 3; Element value: GTA VI
    
    * If the answer is the second option: we need just the elements' value, we should use this type of for loop:
         
         gamesWishList = ["Minecraft", "Roblox", "Fifa", "GTA VI"]
         
         for game in gamesWishList:
            print(game, end=', ')  # Result: this will print -> Minecraft, Roblox, Fifa, GTA VI,
    
"""

all_grades = [8.75, 9.50, 9.20, 7, 8.50, 8.90, 9.70, 5]
max_grade = all_grades[0]
max_grade_index = -1

for index in range(len(all_grades)):
    if max_grade < all_grades[index]:
        max_grade = all_grades[index]
        max_grade_index = index
print(max_grade_index)

# Average
sum_all_grades = 0
for grade in all_grades:
    sum_all_grades += grade

grades_average = sum_all_grades / len(all_grades)
grades_average = round(grades_average, 2)
print(grades_average)
