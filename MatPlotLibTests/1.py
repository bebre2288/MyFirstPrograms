import os
import matplotlib.pyplot as plt
import numpy as np
w=int(input())
def save(name='', fmt='png'):
    pwd = os.getcwd()
    iPath = './pictures/{}'.format(fmt)
    if not os.path.exists(iPath):
        os.mkdir(iPath)
    os.chdir(iPath)
    plt.savefig('{}.{}'.format(name, fmt), fmt='png')
    os.chdir(pwd)
import matplotlib.pyplot as plt
import numpy as np
s = ['one','two','three ','four' ,'five']
x = [1, 2, 3, 4, 5]
z = np.random.random(100)
z1 = [w, 17, 100, 16, 22]
z2 = [12, 14, 21, 13, 17]

fig = plt.figure()
plt.bar(x, z1)
plt.title('Simple bar chart')
plt.grid(False)
# # pie()
# fig = plt.figure()
# plt.pie(x, labels=s)
# plt.title('Simple pie chart')
# save(name='pic_2_2', fmt='pdf')
# save(name='pic_2_2', fmt='png')
plt.show()