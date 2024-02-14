lst = ['friend', 'y', 'ye', 'yes', 'fin', 'add', 'none']
sort_lst = sorted(sorted(lst), key=lambda x: len(x)) # sort the lst alphabetically, then sort in ascending order
print(sort_lst)