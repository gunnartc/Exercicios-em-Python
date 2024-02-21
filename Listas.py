list1 = [
    ['camisa',10.0,25.0,5.0],
    ['calsa',25.0,20.0,5.0],
    ['meia',10.0,45.0,2.0],
    ['bermuda',20.0,44.0,3.0]
]

list2 = [
    ['camisa',10.0,25.0,5.0],
    ['calsa',25.0,30.0,5.0],
    ['meia',10.0,45.0,2.0],
    ['bermuda',20.0,20.0,3.0]
]

list3 = [
    ['camisa',10.0,25.0,5.0],
    ['calsa',25.0,22.0,5.0],
    ['meia',10.0,45.0,2.0],
    ['bermuda',20.0,33.0,3.0]
]

same_products = []

for a in range(len(list1)):
    for b in range(len(list2)):
        for c in range(len(list3)):
            if list1[a][0:] == list2[b][0:] == list3[c][0:]\
                    and list1[a][1] == list2[b][1] == list3[b][1]\
                    and list1[a][2] == list2[b][2] == list3[b][2]\
                    and list1[a][3] == list2[b][3] == list3[b][3]:
                same_products.append(list1[a][0])

same_products = list(set(same_products))

print ('os produtos iguais são: ', same_products)
