from threading import Lock
with open('notes.txt', 'w') as file:
    file.write('some to do....')
from contextlib import contextmanager

# file = open('nodes.txt', 'w')
# try:
    # file.write('some to do...')
# finally:
    # file.close()
lock = Lock()
lock.acquire()
# ...
lock.release()

# with lock:
# Do Something

class ManagedFile:
    def __init__(self, filename):
        print('init')
        self.filename = filename

    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print('exception has been handled')
        # print('exc:', exc_type, exc_val)
        print('Exit')
        return True

with ManagedFile('notes.txt') as file:
    print('Do some stuff')
    file.write('Something to do....')
    file.somemethod()
print('continuing')

@contextmanager
def open_managed_file(filename):
    f = open(filename, 'w')
    try:
        yield f
    finally:
        f.close()

with open_managed_file('notes.txt') as f:
    f.write('Another thing to do')  # Context managers
