import logging

n = 7
fact = 1
while n > 0:
    fact = fact * n
    n -= 1

print(fact)

def factorial(n):
    if n < 1:
        return 1
    else:
        number = n * factorial(n-1)
        return number

print(factorial(7))

def fib(n):  # faster
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

print(fib(2))

def fib2(n):  # slower, gets stack overflow error
    if n <= 1:
        return n
    else:
        return (fib2(n-1) + fib2(n-2))

print(fib2(2))

# DEBUG INFO WARNING ERROR CRITICAL
logging.basicConfig(level=logging.DEBUG)

logging.info("You have got 20 mails in your inbox")
logging.critical("All components have failed")

logger = logging.getLogger("MY logger")
logger.info('Logger info')
logger.critical("Logger critical")
logger.log(logging.ERROR, "An error occured")

logger.setLevel(logging.DEBUG)

handler = logging.FileHandler('mylog.log')
handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(levelname)s - $(asctime)s: %(message)s")
handler.setFormatter(formatter)


logger.addHandler(handler)
logger.debug("this is a debug message")
logger.info('This is important information')




