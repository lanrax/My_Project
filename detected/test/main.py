import threading
import time


def print_number(i):
    time.sleep(1)
    print(i)


for i in range(10):
    t_thread = threading.Thread(target=print_number, args=(i,))
    t_thread.start()