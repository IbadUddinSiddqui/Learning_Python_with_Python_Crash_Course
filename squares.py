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
print(f'the first three items in the list are {number_list[:3]}')
print(f'the middle three items in the list are {number_list[49:52]}')
print(f'the last three items in the list are {number_list[-3:]}')

my_favorite_players = ["messi","neymar","mbappe","ronaldo","salah"]
print(my_favorite_players)
my_favorite_players.append("kane")
print(my_favorite_players)
my_favorite_players.insert(0,"de gea")
print(my_favorite_players)

my_brothers_favorite_players = my_favorite_players[:]
my_brothers_favorite_players.append("modric")

print(f'{my_brothers_favorite_players} are my brothers favorite players')
my_brothers_favorite_players.append("neymar")
my_favorite_players.remove("neymar")
print(f'{my_favorite_players} are my favorite players now')
print(f'{my_brothers_favorite_players} are my brothers favorite players now')

# definign a tuple

dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])



























