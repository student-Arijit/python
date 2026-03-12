import threading
import time

def task(name, delay):
    print(f"Thread {name} starting...")
    time.sleep(delay)
    print(f"Thread {name} finishing.")

t1 = threading.Thread(target=task, args=("one", 2))
t2 = threading.Thread(target=task, args=("two", 4))

t1.start()
t2.start()

t1.join()
t2.join()

print("done")
