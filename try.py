# random code to
words = ['on', 'in']
msg = input(': ')

tell = [words[0] if msg == 'ground' else words[1]]
print(f'Its moving {tell} the {msg}')