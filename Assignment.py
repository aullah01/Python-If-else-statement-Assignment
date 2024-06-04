# Problem # 1:
# Write a program to check whether a person is eligible to vote or not?

# Solution:

# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")
    
    
    
# Problem # 2:
# Write a program to check char is vowel or not.

# solution:

# char = input("Enter a character: ")
# if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
#     print("It is a vowel")
# else:
#     print("It is not a vowel")
    
    
    
# Problem # 3:
# Write a program to check the number is positive or negative. User input.

# Solution:

# num = int(input("Enter a number: "))
# if num > 0:
#     print("The number is positive")
# elif num < 0:
#     print("The number is negative")
   
   
    
# Problem # 4:
# Write a program to check whether a number is odd or even?

# Solution:

# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print(num ,"is even")
# else:
#     print(num ,"is odd")




# Problem # 5:
# Write a program to display the grade of the user in subject A, ask user marks obtained out of 100

# Solution:

# subject_math_score = int(input("Enter the marks obtained out of 100: "))
# if subject_math_score >= 90:
#     print("A+1")
# elif subject_math_score>=80:
#     print("A1")
# elif subject_math_score>=70:
#     print("A")
# elif subject_math_score>=60:
#     print("B")
# elif subject_math_score>=50:
#     print("C")
# else:
#     print("F")




# Problem # 6:
# Write a program to check whether a number is divisible by 7

# Solution:

# num = int(input("Enter a number: "))
# if num % 7 == 0:
#     print(num,"is divisible by 7")
# else:
#     print(num,"is not divisible by 7")




# Problem # 7:
# Write a program to check if year is leap year.

# Solution:

# year = int(input("Enter a year: "))
# if year % 4 == 0:
#     print(year,"is a leap year")
# else:
#     print(year,"is not a leap year")
    


# Problem # 8:
# Write a program to ask user its name and check whether name consists of 5 or more letters

# Solution:

# name = input("Enter your name: ")
# if len(name) >= 5:
#     print(name,"has 5 or more letters")
# else:
#     print(name,"has less than 5 letters")
    
    
    
    
# Problem # 9:
# Write a program that accepts 3 inputs from user. input 1 and input 2 should be numbers and the third input should be mathematical operator.

# Solution:

# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
# operator = input("Enter an operator: ")
# if operator == "+":
#     print(num1 + num2)
# elif operator ==  "-":
#     print(num1 - num2)
# elif operator == "*":
#     print(num1 * num2)
# elif operator == "/":
#     print(num1 / num2)
# else:
#     print("Invalid operator")



# Problem # 10:
# Write a program that accepts 1 input from user and check if the number is divisible by 2 and 3 both.

# Solution:

# num = int(input("Enter a number: "))

# if num % 2 == 0 and num % 3 == 0:
#     print(num,"is divisible by 2 and 3 both")
# elif num % 3 == 0:
#     print(num,"is only divisible by 3")
# elif num % 2 == 0:
#     print(num,"is only divisible by 2")
# else:
#     print(num,"is not divisible by 2 and 3 both")
   
   
   
# Problem # 11: 
# Write a program that accepts 2 inputs from user and check which number is largest.

# Solution:

# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))

# if num1 > num2:
#     print(num1,"is greater than",num2)
# else:
#     print(num2,"is greater than",num1)
    
    
    
    
# Problem # 12:
# Write a program that accepts 3 input from user and check which number is largest.

# Solution:

# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))
# num3 = int(input("Enter a number: "))
# if num1 > num2:
#     if num1 > num3:
#         print(num1,"is greater than",num2,"and",num3)
#     else:
#         print(num3,"is greater than",num1,"and",num2)
# elif num2 > num1:
#     if num2 > num3:
#         print(num2,"is greater than",num1,"and",num3)
#     else:
#         print(num3,"is greater than",num1,"and",num2)
# else:
#     print(num3,"is greater than",num1,"and",num2)
    
    
# Problem # 13:
# Write a program that accepts 3 input from user and check the second largest.

# Solution:

# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))
# num3 = int(input("Enter a number: "))

# if num1 > num2:
#     if num1 > num3:
#         if num2 > num3:
#             print(num2,"is the second largest")
#         else:
#             print(num3,"is the second largest")
#     else:
#         print(num1,"is the second largest")
# else:
#     if num2 > num3:
#         if num1 > num3:
#             print(num1,"is the second largest")
#         else:
#             print(num3,"is the second largest")
#     else:
#         print(num2,"is the second largest")



# Problem # 14:
# Write a program that accepts 3 input from user and check the second largest.
# for example:
# input1 is 5 and input2 is 10 and input3 is 15
# output should be 10 as this number is larger than 5 and smaller than 15

#Solution:

# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))
# num3 = int(input("Enter a number: "))

# if num1 > num2:
#     if num1 > num3:
#         if num2 > num3:
#             print(num2,"is larger than",num3,"and smaller than",num1)
#         else:
#             print(num3,"is larger than",num2,"and smaller than",num1)
#     else:
#         print(num1,"is larger than",num2,"and smaller than",num3)
# else:
#     if num2 > num3:
#         if num1 > num3:
#             print(num1,"is larger than",num3,"and smaller than",num2)
#         else:
#             print(num3,"is larger than",num1,"and smaller than",num2)
#     else:
#         print(num2,"is larger than",num1,"and smaller than",num3)
        
            
    
# Problem # 15:
# Write a python program that accept user an input. The valid input should be of following

# Solution:

# signal = (input("Enter a color: "))

# if signal == "green" or signal == "GREEN" or signal == "gREEN":
#     print("Car is allowed to go")
# elif signal == "red" or signal == "RED" or signal == "rEd":
#     print("Car has to wait")
# elif signal == "yellow" or signal == "YELLOW" or signal == "yELlOw":
#     print("Car has to stop")
# else:
#     print("Invalid signal")
        
        
        
# Problem # 16:      
"""
Write a program that takes two numbers as input and prints:

"First number is greater" if the first number is greater than the second number.
"Second number is greater" if the second number is greater than the first number.
"Both numbers are equal" if the two numbers are equal.
"""
# Solution:

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# if num1 > num2:
#     print("First number is greater")

# elif num2 > num1:
#     print("Second number is greater")

# else:
#     print("Both numbers are equal")



# Problem # 17:
"""
Write a program that takes a password as input and checks its strength:

If the password length is less than 6, print "Weak password".
If the password length is between 6 and 12, print "Moderate password".
If the password length is more than 12, print "Strong password".
"""

# Soluton:

# password = input("Enter a password: ")    
# if len(password) < 6:
#     print("Weak password")
# elif len(password) >= 6 and len(password) <= 12:
#     print("Moderate password")
# elif len(password) > 12:
#     print("Strong password")



# Problem # 18:
"""
Write a program that takes an employee's salary and years of service as input. Calculate the bonus as follows:

If the years of service are less than 5, no bonus.
If the years of service are between 5 and 10, bonus is 10% of the salary.
If the years of service are more than 10, bonus is 20% of the salary.
Print the bonus amount.
"""

# Solution:

# salary = float(input('Enter the salary: '))
# years_of_service = int(input('Enter the years of service: '))

# if years_of_service < 5:
#     bonus = 0
# elif years_of_service >= 5 and years_of_service <= 10:
#     bonus = salary * 0.1
# elif years_of_service > 10:
#     bonus = salary * 0.2
# print(salary + bonus)
# print(bonus)




# Problem # 19:
"""
Write a program that takes the total amount of a purchase as input and applies a discount:

If the amount is less than $100, no discount.
If the amount is between $100 and $500, apply a 10% discount.
If the amount is more than $500, apply a 20% discount.
Print the final amount after the discount.

"""

# Solution:

# amount = float(input("Enter the purchase amount: "))

# if amount < 100:
#     discount = 0
#     final_amount = amount - discount
# elif amount > 100:
#     discount = amount * 0.1
#     final_amount = amount - discount
# elif amount > 500:
#     discount = amount * 0.2
#     final_amount = amount - discount
# print("Final amount after discount: ",final_amount)



# Problem # 20:
"""
Write a program that takes a person's age as input and prints the age group they belong to:

If the age is less than 13, print "Child".
If the age is between 13 and 19 (inclusive), print "Teenager".
If the age is 20 or above:
    If the age is less than 65, print "Adult".
    If the age is 65 or above, print "Senior".
"""

# Solution:

# age = int(input("Enter your age: "))

# if age < 13:
#     print("Child")
# elif age >= 13 and age <=19:
#     print("Teenager")
# elif age >= 20:
#     if age < 65:
#         print("Adult")
#     elif age >= 65:
#         print("Senior")




# Problem # 21:
"""
Write a program that checks if a customer is eligible for a discount based on their membership status and purchase amount:

If the customer is a member:
    If the purchase amount is $50 or more, print "Eligible for 10% discount".
    Otherwise, print "Eligible for 5% discount".
If the customer is not a member:
    If the purchase amount is $100 or more, print "Eligible for 5% discount".
    Otherwise, print "No discount".
"""

# Solution:

# purchase_amount = float(input("Enter the purchase amount: "))
# customer = input("Customer is member or not: ")
# if customer == "member":
#     if purchase_amount >= 50:
#         print("Eligible for 10% discount")
#     else:
#         print("Eligible for 5% discount")
# else:
#     if purchase_amount >= 100:
#         print("Eligible for 5% discount")
#     else:
#         print("No discount")




# Problem # 22:
"""
create the same ATM machine program that we do in last class.
features:
    allow only affiliated_card if age < 60
    allow govt employee regardless of age and affiliated_card
    charge 10 Rs more if grade is less than 18

# hint: filename: if_statement/if_with_nested_if.py
"""

# Solution:

# age = int(input("Enter your age: "))
# affiliated_card = (input("Do you have an affiliated card? (yes/no): "))
# govt_employee = (input("Are you a government employee? (yes/no): "))
# grade = int(input("Enter your grade: "))

# balance = 0
# print("initial  balance", balance)
# withdraw_amount = 50
# if balance < withdraw_amount:
#     print("insufficient balance")
    
# deposit_amount = 500
# # balance = balance + deposit_amount
# # print("balance after deposit", balance)
# # withdraw_amount = 50

# if govt_employee == "yes":
#     if grade < 18:
#         withdraw_amount += 10
    
#     if balance >= withdraw_amount:
#         balance -= withdraw_amount
#         print("Balance after withdrawal:", balance)
#     else:
#         print("Insufficient balance")
# else:
#     if age < 60 and affiliated_card == "yes":
#         if grade < 18:
#             withdraw_amount += 10
        
#         if balance >= withdraw_amount:
#             balance -= withdraw_amount
#             print("Balance after withdrawal:", balance)
#         else:
#             print("Insufficient balance")
#     else:
#         print("Not eligible for withdrawal based on age and card affiliation.")
    