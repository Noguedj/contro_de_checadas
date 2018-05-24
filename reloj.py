import time
global s
global m
s = 0
m = 0
while True:
    print(str(s))
    s += 1
    if (s>=60):
        import os
        os.system("python /home/pi/Downloads/envio.py")
        break
    time.sleep(1)
