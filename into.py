# Data types

#Strings


greeting = "hi"
name = "Frida"

message = f'{greeting}, {name.upper()}. Welcome!'



print(message)

print(len(message))
print(message[0:5])

#
# print(dir(name)) #check all methods available for the element
# print(help(str)) #all methods for that data type


num =  3

print(type(num)) #returns back information about the type of number it is float vs. integer

print(3 / 2) #returns decimals (only on python 3)
print(3//2) #returns Floor division
print(3 ** 2) #exponent
print (3 % 2) # modulus

print(abs(-3)) #absolute value
print(round(3.7))# returns 4
# the round up of the value. It accepts a second argument
#to specify the digits we want to round (first digit after the decimal):
print(round(3.7, 1)) #returns 3.8

# casting
num_1 = 100
num_2 = 200
num_1 = int(num_1)
num_2 = int(num_2)
print(num_1 + num_2)