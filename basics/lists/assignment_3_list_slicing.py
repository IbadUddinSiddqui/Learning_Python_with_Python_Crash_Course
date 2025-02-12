colors = ["red","blue","green","yellow","purple","orange","black"]
#printing the first three colors in the list
print(f'the first three colors in the list are {colors[:3]}')
print(f' the last 2 colors of colors list is {colors[-2:]}')
#printing every second color in the list
for color in colors[::2]:
    print(color)
#printing the colors in reverse order
for color in colors[::-1]:
    print(color)

