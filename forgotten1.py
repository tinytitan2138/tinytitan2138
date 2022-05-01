import threading
import time
def helloworld():
    print('hello, world')

#t1 = threading.Thread(target=helloworld)
#t1.start()  # functions work in parralel.


def function1():
    for i in range(10):
        print('ONE')

def function2():
    for i in range(10):
        print('TWO')


t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2)

#t1.start()
#t2.start()
# threading is good for games, since audio graphics and physics is parralel not sequential


def hello():
    for i in range(50):
        print('hello')


t3 = threading.Thread(target=hello)

t3.start()
#t3.join()  # join function makes it so the thread finishes before the next code is executed
print('code ended')


def test(var):
    print(var)


t4 = threading.Thread(target=test(var='hello'))
t4.start()

x = 8192

lock = threading.Lock()


def double():
    global x, lock
    lock.acquire()
    while x < 9000:
        x *= 2
        print(x)
        time.sleep(1)
    print('reached max')
    lock.release()
def halve():
    global x, lock
    lock.acquire()
    while x > 1:
        x /= 2
        print(x)
        time.sleep(1)
    print('reached min')
    lock.release()
t5 = threading.Thread(target=halve)
t6 = threading.Thread(target=double)

#t5.start()
#t6.start()

# locking means only 1 thread at a time is allowed access to resource

semaphore = threading.BoundedSemaphore(value=5)

def access(thread_number):
    print("[] is tring to access".format(thread_number))
    semaphore.acquire()
    print("[] was granted access".format(thread_number))
    time.sleep(10)
    print("[] is now releasing".format(thread_number))
    semaphore.release()

for thread_number in range (1, 11):
    t = threading.Thread(target=access, args=(thread_number,))
    t.start()
    time.sleep(1)


