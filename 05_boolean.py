#boolean values: True, False (should start with the capital letter)

a = 3
b = 5

print(a==b)

print(a != b)

print(a<b)

print(a>b)

print(type(True))
print(type(False))

#converting numbers to boolean
print(bool(28))
print(bool(-2.718))
print(bool(0)) #in pythın bool(0) gives false

#converting strings to booleans

print(bool("Turing"))
print(bool(" "))
print(bool("")) #in python the empty string is converted to False while every other string is turned into True

#converting boolean value into a string
print(str(True))

#converting booleans to numbers
print(int(True)) #gives 1
print(int(False)) #gives 0

print(5+True) #takes true as 1 and gives 6
print(10*False) #takes False as 0 and gives 0


