
fset = frozenset([1, 2, 3, 4])
print(fset)

#Set-Frozenset farkı

# Set üzerinde değişiklik
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # {1, 2, 3, 4}

# Frozenset üzerinde değişiklik denemesi
my_frozenset = frozenset([1, 2, 3])
#my_frozenset.add(4)

#Frozenset hashing
my_dict = {frozenset([1, 2]): "herhangi bir değer"}

#dict_type={"Anahtar Kelime":"Değer"}

print(my_dict[frozenset([1, 2])])
