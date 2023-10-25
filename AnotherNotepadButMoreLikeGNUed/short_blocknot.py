import time
import os
print("имя файла")
x=input()
txt = open(x, 'w')
time.sleep(1)
print('текст файла')
y=input()
time.sleep(1)
print("чтобы сохранить введите 1, если не хотите сохранять введите 2")
z=input()
z=int(z)
if z==1:
    txt.write(y)
    txt.close()
if z==2:
    txt.close()
    os.remove(x)
time.sleep(1)
print("готово!")
#