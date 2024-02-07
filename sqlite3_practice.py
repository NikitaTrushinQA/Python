import sqlite3
from faker import Faker

conn = sqlite3.connect('person_data.db')    #подключаемся к датабазе ,если ее нет она будет создана
c = conn.cursor()

c.execute("""CREATE TABLE person
(id INTEGER PRIMARY KEY,
name TEXT,
age INTEGER,
address TEXT,
phone TEXT,
email TEXT)""")

faker = Faker()
for i in range(500):                # заполняем таблицу 500 различными людьми
    name = faker.name()
    age = faker.random_int(min=18, max=80,step=1)
    address = faker.address()
    phone = faker.phone_number()
    email = faker.email()
    c.execute(f'INSERT INTO person(name, age, address, phone, email) VALUES(?, ?, ?, ?, ?)',[name, age, address, phone, email])

conn.commit()
conn.close()
