import time
import subprocess
import random
print("задайте время")
time_int=input()
time_int=int(time_int)
print("таймер установлен на",time_int, "сек")
for i in range (1, time_int):
    print('времени осталось' , time_int-i , "сек")
    time.sleep(1)

print("время")

subprocess.Popen( ["C:\Program Files\MPC-BE x64\mpc-be64.exe","C:\prj\s01 01 музыка.mp3"] )