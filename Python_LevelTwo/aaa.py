import  random

heroes = ['spiderman', 'thor', 'batman']
for h in heroes:
    print(h)

#what creates iterators are generators
g = range(6)
print(g)

def magic(): #the methos is now a generator
    for i in range(6):
        yield random.randint(1, 20)#6 different no. between 1 and 20

for number in magic():
    print('value is', number)

