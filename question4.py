yours = ['Yale', 'MIT', 'Berkeley']
mine = ['SFAI', 'Reed', 'Stanford']

ours1 = yours + mine
print(ours1)

#append, appending each set to the empty set ours2, ours2 is altered, not ours1

ours2 = []
ours2.append(mine)
ours2.append(yours)
print(ours2)

yours[1] = 'Massachusetts Institute of Technology'
print(yours)

mine[0] = 'San Francisco Art Institute'
print(mine)

print(ours1)
print(ours2)

#ours1 includes both lists in one set, ours2 prints the sets separately and with the changes included (since they were added after ours2)
#changing yours would only affect ours2 because the change occurs after ours2 has appended mine and yours together
