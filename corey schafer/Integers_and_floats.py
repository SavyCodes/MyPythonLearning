# Integers
# >> Integers are whole number <<

num = 3

# python has Function known as Type which represent datatype of your variable

print(type(num))

# Floats
# >> Float are decimal number <<

num = 3.15

print(type(num))

# Arithmetic Operation
# Addition:       a + b
# Substration:    a - b
# multiplication: a * b
# division:       a / b
# floor divition: a // b
# exponents:      a ** b
# Modulus:        a % b


a = 3
b = 2

Addition = a + b
Substration = a - b
multiplication = a * b
division = a / b
floor_divition = a // b
exponents = a ** b
modulus = a % b

print('a + b =', Addition)
print('a - b =', Substration)
print('a * b =', multiplication)
print('a / b =', division)
print('a // b =', floor_divition)
print('a ** b =', exponents)
print('a % b =', modulus)

# Python follows order of opration

print(1 + 2 + 3)
print(3 * (1 + 2))

# Incremental operation

num = 1
num =  num  + 1

print(num)

# shorthand way to do this

num = 1
num += 1

print(num)

# to print absolute valve 

print(abs(-3))

# round off 

print(round(3.56, 1))


# Comparison operators
# Equal:            a == b
# Not Equal:        a != b
# Greater then:     a > b
# Less then:        a < b
# Greater or Equal: a >= b
# Less or Equal:    a <= b

a = 3
b = 2
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# string addition
num = '100'
num1 = '200'

print(num + num1)