f = open('dq_unisex_names.csv','r')
names = f.read()
names_list= names.split('\n')
first_five = names_list[:5]
##print(first_five)

nested_list = []
for element in names_list:
    comma_list = element.split(',')
    nested_list.append(comma_list)

##print(nested_list[:5])

numerical_list = []
for element in nested_list:
    name = element[0]
    number = float(element[1])
    numerical_list.append([name,number])
##print(numerical_list[:5])

thousand_or_greater = []
for i in numerical_list:
    if i[1] >= 1000:
        thousand_or_greater.append(i)
print(thousand_or_greater[:10])
