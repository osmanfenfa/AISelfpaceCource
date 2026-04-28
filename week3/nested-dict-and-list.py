# Dictionary of List 
students = [
    {'name': 'Osman', 'grade': 90},
    {'name': 'Marah',   'grade': 80},
    {'name': 'Aliya', 'grade': 70},
    {'name': 'Dawa', 'grade': 75},
]

for s in students:
    print(s["name"], '→ grade:', s['grade'])
 
  
spam = [{"name": "Alice", "age": 3}, {"name": "Zophie", "age": 17}]
print(spam[1]["name"])
print(spam[0]["age"])

spam1 = {"humans": ["Alice", "Bob"], "pets": ["Zophie", "Pookah"]}
print(spam1["pets"])
print(spam1["pets"][0])


# Loop Over
pet_owner = {"Alice": ["Spot", "Mittens"], "Al": ["Zophie"]}
for pet in pet_owner["Alice"]:
    print(pet)
    

#  Manual baseball dictionary (9 innings)
game = {
    'Home': {
        1: 0, 2: 0, 3: 1,   # ← Home scored in 3rd
        4: 0, 5: 0, 6: 0,
        7: 0, 8: 0, 9: 0,
    },
    'Visitor': {
        1: 0, 2: 0, 3: 0,
        4: 0, 5: 0, 6: 0,
        7: 0, 8: 0, 9: 0,
    },
}

print('Home 3rd inning:', game['Home'][3])
print('Visitor total:',   sum(game['Visitor'].values()))


#  Generate the same dictionary with a loo
game1 = {'Home': {}, 'Visitor': {}}
for inning in range(1, 10):   # 1 through 9 inclusive
    game1['Home'][inning]    = 0
    game1['Visitor'][inning] = 0

game1['Home'][3] = 1 
print(game1['Home'])
print(game1['Visitor'])


# Scale to 9999 innings
game2 = {'Home': {}, 'Visitor': {}}
for inning in range(1, 10):      # was 9 innings
    game2['Home'][inning]    = 0
    game2['Visitor'][inning] = 0

for inning in range(1, 10_000):   # now 9 999 innings
    game2['Home'][inning]    = 0
    game2['Visitor'][inning] = 0

game2['Home'][3] = 1
print('Total innings:', len(game2['Home']))
print('Home inning 3:', game2['Home'][3])
print('Home total runs:', sum(game2['Home'].values()))
