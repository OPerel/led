# create a list with n items
def list_(n):
    ls = list(range(0, n, 1))
    return ls

# slice a list into n sized chuncks
def s_list(l, n):   
    for i in range(0, len(l), n):
        yield l[i:i + n]

sliced_list = list(s_list(list_(100), 10))

# create columns sublists
column_list = list(zip(*sliced_list))