var1 = '5 4' 
var2 = '1 3 5 7 9' 
var3 = '2 3 4 5' 

a = var2.split(' ')
b = var3.split(' ')

a2 = set(a)
b2 = set(b)

# Введите ваше решение ниже

i = list(a2.intersection(b2))
i.sort()
print(*[x for x in i])