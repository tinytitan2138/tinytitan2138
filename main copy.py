from threading import Thread, Lock, current_thread
from multiprocessing import Process
import os
import time
from queue import Queue
def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)

processes = []
num_processes = os.cpu_count()
# Create processes
for i in range(num_processes):
    p = Process(target=square_numbers)  # If fuction has argument pass in args
# Start
for p in processes:
    p.start()
# Join
for p in processes:
    p.join()
print('End main')

threads = []
num_threads = 10
# Creates thread.
for i in range(num_threads):
    t = Thread(target=square_numbers)
    threads.append(t)
# Start
for t in threads:
    t.start()
# Join
for t in threads:
    t.join()

database_value = 0

def increase(lock):
    global database_value
    with lock:
        local_copy = database_value
        # Processing
        local_copy += 1
        time.sleep(0.1)
        database_value = local_copy




if __name__ == "__main__":
    lock = Lock()
    print('Start value', database_value)
    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print('end value', database_value)
    print('end main')

q = Queue()
q.put(1)
q.put(2)
q.put(3)
# 3 2 1 -->
first = q.get()
print(first)
q.task_done()
print('end main')
q.join()

def worker(q):
    while True:
        value = q.get()
        # Processing...
        print(f'in {current_thread().name} got {value}')
        q.task_done()





if __name__ == "__main__":
    q = Queue()
    num_threads = 10
    for i in range(num_threads):
        thread = Thread(target=worker, args=(q,))
        thread.daemon=True
        thread.start()
    for i in range(1, 21):
        q.put(i)
    q.join()
    print('end main')


