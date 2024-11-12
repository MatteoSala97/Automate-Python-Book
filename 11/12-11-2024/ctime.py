import time

x = time.ctime()
print(x)

for i in range(3):
    print(f"Tick")
    time.sleep(1)
    print(f"Tock")
    time.sleep(5)