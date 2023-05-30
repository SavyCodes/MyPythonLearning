# Print Welcome Message
print('Hello World')

# Create a Variable
message = 'Hello World'
print(message)

# multiline comment
print('''Hello,
How are you ''')

# To resolve mutiple quote issue 
print("Hello's world")

# Length of Variable
print(len(message))

# Access Index of Characters
print(message[0:5])

# Slicing
print(message[6:])

# All Lower Case, Upper Case
print(message.lower())
print(message.upper())

# Count
print(message.count('Hello'))

# Find
print(message.find('World'))

# Replace

new_message = message.replace('World', 'Universe')

print(new_message)

# Concatination

greeting = 'Hello'
name = 'Abhishek'

message = greeting + ', ' + name

message1 = '{}, {}. Welcome!'.format(greeting, name)

print(message)
print(message1)

# F string Formating
greeting = 'Hello'
name = 'Abhishek'

message2 = f'{greeting}, {name.upper()}. Welcome!'

print(message2)

