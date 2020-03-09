labels = open('quickscripts/labels.txt')
values = open('quickscripts/values.txt')

output = open('quickscripts/selectoptions.txt', 'w')

lbl = labels.readline()[:-1]
val = values.readline()[:-1]

while lbl:
    output.write(f'({val}, {lbl}), ')
    lbl = labels.readline()[:-1]
    val = values.readline()[:-1]

output.close()

# print(labels.readline()[:-1])
# print(labels.readline()[:-1])
