import sqlite3


class Person:
    def __init__(self, number=1, first="", last="", age=1):
        self.number = number
        self.first = first
        self.last = last
        self.age = age
        self.connection = sqlite3.connect('mydata.db')  # connects to a database
        self.cursor = self.connection.cursor()

    def load_person(self, number):
        self.cursor.execute("""
        SELECT * FROM persons
        WHERE id = {}
        """.format(number))

        results = self.cursor.fetchone()
        self.number = number
        self.first = results[1]
        self.last = results[2]
        self.age = results[3]
    def insert_person(self):
        self.cursor.execute("""
        INSERT OR IGNORE INTO persons VALUES
        ({}, '{}', '{}', {})
        """.format(self.number, self.first, self.last, self.age))

        self.connection.commit()
        self.connection.close()



#p1 = Person()
#p1.load_person(1)
#print(p1.first)
#print(p1.last)
#print(p1.age)
#print(p1.number)

p2 = Person(7, "Alex", "Robbins", 30)
p2.insert_person()

connection = sqlite3.connect('mydata.db')
cursor = connection.cursor()
cursor.execute("SELECT * FROM persons")
results = cursor.fetchall()
print(results)
connection.close()