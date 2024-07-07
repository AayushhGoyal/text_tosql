import sqlite3
# connect to sqlite database

connection = sqlite3.connect('student.db')

#create a cursor object to insert records, create tables, etc

cursor = connection.cursor()

table_info = '''
CREATE TABLE STUDENT1233(
    NAME VARCHAR(20),
    CLASS VARCHAR(10),
    SECTION VARCHAR(5),
    MARKS INT
);
'''

cursor.execute(table_info)


#INSERT SOME MORE RECORDS

cursor.execute("""INSERT INTO STUDENT1233 VALUES('Rahul', 'X', 'A', 90)""")
cursor.execute("""INSERT INTO STUDENT1233 VALUES('jack', 'X', 'B', 80)""")
cursor.execute("""INSERT INTO STUDENT1233 VALUES('Ravi', 'X', 'C', 70)""")
cursor.execute("""INSERT INTO STUDENT1233 VALUES('alex', 'XI', 'A', 60)""")
cursor.execute("""INSERT INTO STUDENT1233 VALUES('matthew', 'XI', 'C', 40)""")

#display all the records

print("all the records in the table are:")
data = cursor.execute("""SELECT * FROM STUDENT1233""")

for row in data:
    print(row)
    
##close the connection
connection.commit()
connection.close()

