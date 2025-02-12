numbers=[]
for number in range(1,11):
    numbers.append(number)
 
print(numbers)
print(f'the sum of the numbers is {sum(numbers)}')    
print(f'the maximum number in the list is {max(numbers)}')
print(f'the minimum number in the list is {min(numbers)}')
print(f'the average of the numbers is {sum(numbers)/len(numbers)}')
numbers.reverse()
print(f'numbers in reverse order are {numbers}')
numbers.sort()
print(f'numbers in ascending order are {numbers}')
numbers.reverse()
print(f'numbers in descending order are {numbers}')  




