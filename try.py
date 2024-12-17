# random code 
import random
words = ['on', 'in']
msg = input(': ')

tell = [words[0] if msg == 'ground' else words[1]]
print(f'Its moving {tell} the {msg}')

# making a random number
num = random.randint(1, 100)
print(num)