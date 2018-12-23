#%% 
import time

ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def s_list(l, n):   
    for i in range(0, len(l), n):
        yield l[i:i + n]

sliced_list = list(s_list(ls, 3))

c1 = []
c2 = []
c3 = []

for i in sliced_list:
    c1.append(i[0])
    c2.append(i[1])
    c3.append(i[2])

print(c1)
time.sleep(1)
print(c2)
time.sleep(1)
print(c3)

#%%