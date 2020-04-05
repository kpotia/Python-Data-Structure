colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'brown']

print(colors)
print(type(colors))
colors.reverse()
print(colors)
colors.sort()
print(colors)

new_colors = ['mycolor','yourcolor']
color = colors.pop(0)
print('popped', color)

print(colors)


colors.extend(new_colors)

print(colors)

colors.clear()

print(colors)