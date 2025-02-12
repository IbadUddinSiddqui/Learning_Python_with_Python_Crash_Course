fruits = ["apple","banana","orange","mango","pineapple"]
print(f'First fruit in the list is  {fruits[0]} and the last fruit in the list is {fruits[-1]}')
#replacing second fruit with mangoes
fruits[1] = "mangoes"
print(f'fruits after replacing the second fruit with mangoes are {fruits}')
#adding a new fruit to the list
fruits.append("pineapple")
print(f'fruits after adding grapes to the list are {fruits}')
#removing the third fruit from the list 
fruits.pop(2)
print(f'fruits after removing the third fruit from the list are {fruits}')
