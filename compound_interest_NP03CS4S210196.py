# Coding Challenge 1, compound_interest_NP03CS4S210196.py
# Name: Nikesh Shrestha
# Student No:NP03CS4S210196

# Compound Interest Calculator

"""
Requirements:
    You will develop a program to calculate compound interest.

    • Print a welcome message explaining the purpose of the program.
    • Prompt the user for the necessary inputs (see formulae and brief)
    • Convert input values to suitable data types.
    • Perform compound interest calculation using the forumlae provided.
    • Print the result to the terminal using appropriate formatting.
    
    • Your program should be as close as possible to the example shown in the assessment brief.

Constraints:
    • Ensure that the interest rate is entered as a percentage and not a decimal.
    • Ensure that all monetary values are formatted to two decimal places.

Hints:
    • Think about what data types are the most appropriate for each input value.
    • Order of operations will be important, make sure you use parenthesis.
    • Review lecture two for more information on string formatting.
    • Your programs output should be as close as possible to the example in the assessment brief.
"""

# TODO: Write your code here!

print("\nWelcome to the Wolving compound interest calculator.\nThis program calculate your potential returns when you invest with us.\n\n")
        
# asking for user input and storing it in variable named P(principle) after typecasting it to integer
p = int(input("How much would you like to invest?:£"))

# asking for user input and storing it in variable named rate after typecasting it to float
r = float(input("What is the interest on your account?: "))

# asking for user input and storing it in variable named t(time of years) after typecasting it to integer 
t = int(input("How long are you planning to to invest [in years]?: "))

# asking for user input and storing it in variable named n(number of times interest is compounded) after typecasting it to integer 
n = int(input("Enter the number of times the interest is compounded per year: "))

print("\n-----------------------------------------------------------------------------------------------------")

# using tab to create the header
print("Year:\t\tPeriod:\t\tOld balance:\t\tInterest:\t\tNew balance:")

print("-----------------------------------------------------------------------------------------------------")

old_p= p #old_p is consider as principle
# using nested for_loops with time and n
for i in range(t):
    print(i + 1)
    for j in range(n):
        old_balance = p
        interest = (p * r) /(100*n) #interest prints  the interest amount of  number of month as per user wants
        p = p + interest# while we add the interest amount and the old amount as principal we get new balance

        # Applying (\t) tabs to print output under the header and arranging them properly
        print(f"\t\t{j + 1}\t\t£{format(old_balance, '.2f')}\t\t{format(interest, '.2f')}\t\t\t£{format(p, '.2f')}")

#Printing the final compound interest in systematic order 
print(f"\n£{old_p} invested at rate {r}% for {t} years compounded {n} times per year is £{format(p, '.2f')}")

print("Enter any key to exit:")#To control program from shutting down.
