list = ['egg', 'chicken', 'beef', 'egg', 'chicken', 'egg', 'chicken', 'beef', 'egg', 'chicken', 'egg', 'chicken', 'beef', 'egg']

unic_items = set()
dup_items = set()
count = {}

for item in list:
    if item in unic_items:
        dup_items.add(item)
    else:
        unic_items.add(item)

print ('Itens duplicados na lista: ')
for item in dup_items:
    print (item)

print ()
print ('Quantas vezes os items se repetem?')
print ()

for item in list:
    if item in count:
        count [item] +=1
    else:
        count [item] =1

for item, frequency in count.items():
    print(f'Os item {item} se repete {frequency} vezes')
