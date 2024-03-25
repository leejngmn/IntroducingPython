#연습문제
#8.1 ~ 8.2
e2f={'dog':'chien', 'cat' : 'chat', 'walrus':'morse'}
print(e2f['walrus'])

#8.7~ 8.9
life ={'animals':{'cats':'Henri','octopi':'Grumpy','emus':'Lucy'}, 'plants':'', 'other':{}}
print(life.keys())
print(life['animals'].keys())
print(list(life['animals'].keys()))
print(life.values())

#8.10
squares ={k:k**2 for k in range(10)}
print(squares)

#8.11
a_set={number for number in range(10) if number %2 ==1}
print(a_set)

#8.12
