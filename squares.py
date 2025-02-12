square = []
for value in range(1,21):
 square.append(value**2)
print(square)

number_list = list(range(1,101));
print(number_list,"the list of numbers is")
number_list.extend(list(range(101,201)))
print(number_list,"the list of numbers after extending is")

print(f'min is {min(number_list)}')
print(f'max is {max(number_list)}')
print(f'sum is {sum(number_list)}')






















