import sqlite3
conn = sqlite3.connect('nrk.sqlite')
cursor = conn.cursor()
print("Opened database successfully")

Creating Table
cursor.execute('''CREATE TABLE SCHOOL
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         MARKS          INT);''')
cursor.close()

# Inserting Table

# cursor.execute("INSERT INTO SCHOOL (ID,NAME,AGE,ADDRESS,MARKS) \
#       VALUES (1, 'Rohan', 14, 'Delhi', 200)");
# cursor.execute("INSERT INTO SCHOOL (ID,NAME,AGE,ADDRESS,MARKS) \
#       VALUES (2, 'Allen', 14, 'Bangalore', 150 )");
# cursor.execute("INSERT INTO SCHOOL (ID,NAME,AGE,ADDRESS,MARKS) \
#       VALUES (3, 'Martha', 15, 'Hyderabad', 200 )");
# cursor.execute("INSERT INTO SCHOOL (ID,NAME,AGE,ADDRESS,MARKS) \
#       VALUES (4, 'Palak', 15, 'Kolkata', 650)");
conn.commit()
# conn.close()

# Query Result

for row in cursor.execute("SELECT id, name, marks from SCHOOL"):
  print("ID = ", row[0])
  print("NAME = ", row[1])
  print("MARKS = ", row[2], "\n")
# conn.commit()
# conn.close()


# Update Bot
conn.execute("UPDATE SCHOOL set MARKS = 250 where ID = 3")
conn.commit()
for row in cursor.execute("SELECT id, name, address, marks from SCHOOL"):
  print("ID = ", row[0])
  print("NAME = ", row[1])
  print("MARKS = ", row[2], "\n")
conn.commit()

# Delete Bot
conn.execute("DELETE from  SCHOOL where ID = 2")