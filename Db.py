import mysql.connector

# connect to database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="IrannaDK@0504",
    database="student_databse"
)

cursor = db.cursor()

# create table
cursor.execute("CREATE TABLE IF NOT EXISTS student (id INT, name VARCHAR(50))")

# insert data
cursor.execute("INSERT INTO student (id, name) VALUES (1, 'Rahul')")

db.commit()

print("Data inserted successfully")

# show data
cursor.execute("SELECT * FROM student")

for row in cursor:
    print(row)

db.close()