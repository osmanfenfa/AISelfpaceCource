"""
#Control Flow
age = int(input("Enter Your age: "))

if age <= 18:
    print("Not eligible to vote" )
elif age >= 60:
    print("Too old to vote")
else:
    print ("Vote ya" )


#Year of Experience
year_of_experience = float(input("\n" "Enter your year of experience: ")).case
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
    

race = str(input("\n" "Enter your race: "))
if race == "Black":
    print("You are a nigga")
elif race == "White":
    print("You are the master")
elif race == "Asian":
    print("Chink")
else:
    print("Get the fuck off")
"""   

street = ["Yoni", "Panlap", "Turner Street", "New London", "Church Street", "Kono Spart", "Sina Town", "Hill Station", "Mabanta Road", "Silicon"]

for st in street:
    print(st)