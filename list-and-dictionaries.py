spam = ["cat", "bat", "rat", "hat"]
print(spam[0])
print(spam[3])
print(spam[4])
print(spam[len(spam) - 3])

del spam[0]
del spam
print(spam)

spam = ["cat", "dog", "moose"]
for i in range(len(spam)):
    print(spam[i])  
for i in range(len(spam)):
    print(i)
if "cat" not in spam:
    print(spam)
    
a, b, c = spam
print(a, b, c)

a, b, c = "Cat"
print(b)

for a, b in enumerate(spam):
    print(a, b)

import random
print(random.choices(spam, k=2))
random.shuffle(spam)
print(spam)
print(len(spam))

spam = 5
bacon = 10
eggs = 6

for i in range(5):
    spam += 1
print(spam)

spam += spam * 2
print(spam)

bacon += bacon - 3
print(bacon)

eggs *= eggs * bacon + 5
print(eggs)

spam = ["Cat", "dog", "ariel", "Tinder", "Yoga"]
print(spam.index("Cat"))

spam.sort()
print(spam)
sorted_spam = sorted(spam)
print(sorted_spam)

spam.sort(reverse=True)
print(spam)

True and print("Heloow")
False and print("Hello")
True or print("Hellow")
False or print("Hellor")

"Zophie"
print("Zophie"[1])
print("Zophie"[-1])
print("Zophie"[9999])

for i in "cat":
    print(i)
    
for i in [["cat", "dog"], "moose"]:
    print(i)

for i in "moose"[0:3]:
    print(i)

myTupple = ('cat', 'dog')
print(myTupple)
print(myTupple[:])

myTupple =['cat', 'dog']
print(myTupple)

spam = ('cat', 'dog', 'moose')
spam[2] = 'cow'
print(spam)

a = ['cat', 'dog', 'moose']
b = a
c = a
print(a)
print(b)
print(c)

import copy
a = ['cat', 'dog', 'moose']
b = copy.copy(a)
c = copy.copy(a)
print(a)
print(b)

a = [['cat', 'dog'], 'moose']
b = copy.copy(a)
c = copy.deepcopy(a)
print(b)
print(c)

def is_pangram(sentence):
    EACH_LETTER = []
    for char in sentence:
        char_upper = char.upper()
        if char_upper.isalpha() and char_upper not in EACH_LETTER:
            EACH_LETTER.append(char_upper)
    return len(EACH_LETTER) == 26
sentence = input("Enter a sentence: ")
if is_pangram(sentence):
    print("That sentence is a pangram.")
else:
    print("That sentence is not a pangram.")