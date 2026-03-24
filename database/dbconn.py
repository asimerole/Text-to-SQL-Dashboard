import os
import sqlite3

def dbInit():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    db_path = os.path.join(current_dir, 'sales.db')
    
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            city TEXT NOT NULL,
            total_spent INTEGER 
        )
    ''')

    cursor.execute('SELECT COUNT(*) FROM Users')
    count = cursor.fetchone()[0] 

    if count == 0:
        cursor.execute('''
            INSERT INTO Users (name, city, total_spent) 
            VALUES  ('Ivan', 'Kyiv', 1500),
                    ('Anna', 'Berlin', 3200),
                    ('Marko', 'Warsaw', 800),
                    ('Elena', 'Kyiv', 4500),
                    ('Max', 'Berlin', 150),
                    ('Sophie', 'Paris', 2700),
                    ('Oleg', 'Warsaw', 5000)
        ''')
        connection.commit()
        print("The database has been successfully populated with test data!")
    else:
        print(f"There are already {count} records in the database. Skipping the insertion.")

    connection.commit()

    cursor.execute('SELECT * FROM Users')
    users = cursor.fetchall()
    print("Data in the database:")
    for user in users:
        print(user)

    connection.close()