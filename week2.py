#Control Flow
print("VOTING ELIGIBILITY BASED ON AGE")
age = int(input("Enter Your age: "))
if age <= 18:
    print("Not eligible to vote" )
elif age >= 60:
    print("Too old to vote")
else:
    print ("Vote ya" )


#Year of Experience
print("\nTO TELL ROLE BASED ON YEAR OF EXPERIENCE")
year_of_experience = float(input("Enter your year of experience: "))
if year_of_experience <= 2:
    print("You are eligible for the Juinior Developer role")    
elif year_of_experience <= 3:
    print("You are eligible for the Juinior Developer role")    
elif year_of_experience <= 5:
    print("You are eligible for the Senior Developer role")
elif year_of_experience >= 30:
    print("You need rest") 
else:
    print ("You are eligible for the Project Manager role")

    
print("\n TO TELL BASED ON RACE")
race = str(input("Enter your race: "))
if race == "Black":
    print("You are a nigger")
elif race == "White":
    print("You are a cracker")
elif race == "Asian":
    print("You are a chink")
else:
    print("Get outta here")   


#for loop for printing streets
print("\nFOR LOOP WITH ARRAY")
street = ["Yoni", "Panlap", "Turner Street", "New London", "Church Street", "Kono Spart", "Sina Town", "Hill Station", "Mabanta Road", "Silicon"]
for st in street:
    print(st)


#Reverse number assignment wiithou using reverse function
print("\nPRINTING THE REVERSE OF NUMBERS")
dNumbers = int(input("Enter numbers: "))
dNumber_str = str(dNumbers)
reversed_str = ""

for i in range(len(dNumber_str) -1, -1, -1):
    reversed_str += dNumber_str[i]
rever_dNumber = int(reversed_str)
print("Reversed Number: ", rever_dNumber)


# Assigment for counting prime numbers in range
print("\nTO TELL NUMBER OF PRIME NUMBERS BASED ON USER INPUT")
sasa = int(input("Enter start value: "))
danga = int(input("Enter end value: "))
cont_prime = 0

for num in range(sasa, danga + 1):
    if num > 1:
        na_prime = True
        
        for i in range(2, num):
            if num % i == 0:
                na_prime = False
                break
        
        if na_prime:
            cont_prime += 1
print("Total prime numbers between", sasa, "and", danga, "is:", cont_prime)


#Printing Triangle Pattern
print("\nTO PRINT TRIANGLE PATTERN")
rows = 5
for i in range(1, rows + 1):
    for fen in range(1, i + 1):
        print(fen, end="")
    print()


#The reverse triangle pattern
rowss = 5
for i in range(rowss, 0, -1):
    for que in range(rowss, i - 1, -1):
        print(que, end="")
    print()


#The divisors of an entered number
print("\nTO PRINT THE DIVISORS OF AN ENTERED NUMBER")
n = int(input("Enter a number: "))
print("The divisors of", n, "are:")
for i in range(1, n + 1):
    if n % i == 0:
        print(i)
  
        
#Print total of numbers after input of numbers reaches 0
print("\nTO PRINT THE TOTAL OF NUMBERS ENTERED AFTER 0 IS ENTERED")
fenfaq = 0
while True:
    numb = int(input("Enter a number (0 to stop): "))
    if numb == 0:
        break
    fenfaq += numb
print("total is:", fenfaq)


#Reverse of numbers using WHILE loop
print("\nTO PRINT THE REVERSE OF A NUMBER USING WHILE LOOP")
nums = int(input("Enter a number: "))
reverse = 0
while nums > 0:
    digit = nums % 10
    reverse = reverse * 10 + digit
    nums = nums // 10
print("Reversed number:", reverse)


#Count numbers using WHILE loop
print("\nTO COUNT THE NUMBER OF DIGITS IN A NUMBER USING WHILE LOOP")
num = int(input("Enter a number: "))
count = 0
while num > 0:
    num = num // 10
    count += 1
print("Number of digits:", count)


#Multiplication table of a number using a while loop
print("\nTO PRINT THE MULTIPLICATION TABLE OF A NUMBER USING WHILE LOOP")
n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1


#The Task for Number Guessing Game
print("\nNUMBER GUESSING GAME")
import random
secret = random.randint(1, 20)
attempts = 0
max_attempts = 5
print("NUMBER GUESS GAME")
print(f"I have thought of a number between 1 and 20.")
print(f"You have {max_attempts} attempts to guess it. Good luch\n")

while attempts < max_attempts:
    attempts_left = max_attempts - attempts
    guess_input = input(f"Attempt {attempts + 1}/{max_attempts} : Enter your guess:")
    if not guess_input.isdigit():
        print("Please enter a whole number\n")
        continue
    
    guess = int(guess_input)
    attempts += 1
    if guess == secret:
        print(f"CORRECT! The number was {secret}.")
        print(f"You guessed the number in {attempts} attempts(s).")
        break
    elif guess < secret:
        difference = secret - guess
        if difference <= 2:
            print("too low")
        else:
            print("A little too low")
    elif guess > secret:
        difference = guess - secret
        if difference > 20:
            print("Too high")
        else:
            print("A little too high")
    else:
        print(f"\n Out of attempts! The number was {secret}. Better luck next time!\n")
            
