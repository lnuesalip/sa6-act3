lst1 = [1, 2, 3, 4, 8, 5, 6]
lst2 = [3, 7, 9, 6, 8, 10]
# should return 3, 6, 8 (sorted by ascending)

lst_intersect = sorted(list(filter(lambda x: x in lst2, lst1)))
print(lst_intersect)