import threading
import time
import queue
import socket

event = threading.Event()

def myfunc():
    print('waiting for event to trigger')
    event.wait()
    print('performing action now')


t1 = threading.Thread(target=myfunc)
#t1.start()

#x = input('Do you want to trigger the event? (y/n)\n')
#if x == 'y':
    #event.set()
# daemon threads works in the background, is terminated once script is terminated

path = 'text.txt'
text = ''


def readfile():
    global path, text
    while True:
        with open('text.txt', 'r') as f:
            text = f.read()
        time.sleep(3)


def printloop():
    for i in range(30):
        print(text)
        time.sleep(1)

t2 = threading.Thread(target=readfile, daemon=True)
t3 = threading.Thread(target=printloop)


#t2.start()
#t3.start()

numbers = [10, 20, 30, 40, 50, 60, 70]

q = queue.Queue()

for i in numbers:
    q.put(i)
print(q.get())
print(q.get())

z = queue.LifoQueue()

numbers2 = [1, 2, 3, 4, 5, 6, 7]

for i in numbers2:
    z.put(i)

print(z.get())
print(z.get())

y = queue.PriorityQueue()


y.put((2, "hello World"))  # priority value is highest at 1
y.put((11, 99))
y.put((5, 7.5))
y.put((1, True))

while not y.empty():
    print(y.get())

# socket is endpoint in communication channel, server and client, 2 sockets for data exchange

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 55555))
s.listen()

while True:
    client, address = s.accept()
    print('Connected to []'.format(address))
    client.send('You are connected'.encode())
    client.close()


