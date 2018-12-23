#%% 
import time

def list_(n):
    ls = list(range(0, n, 1))
    return ls

def s_list(l, n):   
    for i in range(0, len(l), n):
        yield l[i:i + n]

sliced_list = list(s_list(list_(50), 10))

for i in sliced_list:
    print(i)

#%%
'''
for i in sliced_list:
    print(i[0])
    time.sleep(1)
    print(i[1])
    time.sleep(1)
    print(i[2])


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
'''

#%%
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
x = ls[i:i+3]
print(x)

#%%
