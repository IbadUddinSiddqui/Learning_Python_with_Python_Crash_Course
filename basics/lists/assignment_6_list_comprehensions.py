list = []
for item in range(1,21):
    list.append(item)
print(list)
# using list comprehension to create a list of even numbers from 1 to 20
even_numbers = [item for item in range(1,21) if item%2==0]
print(even_numbers)
#using list comprehension to create a list of squares of numbers from 1 to 20
squares = [item**2 for item in range(1,21)]
print(squares)

greetings = ["hello","hi","hey","hola"]
#using list comprehension to create a list of greetings in uppercase
upper_greetings = [item.upper() for item in greetings]
print(upper_greetings)
lower_greetings = [item.title( ) for item in greetings]
print(lower_greetings)


