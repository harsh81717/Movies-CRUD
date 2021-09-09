import mysql.connector
# Connection with Database:
mydb = mysql.connector.connect(host='localhost', database="entertainment" ,user='root', passwd='admin')

try:
    print(mydb.connection_id)

except:
    print("Connection Failure")

cursor = mydb.cursor()
#Command for Creating Database:
Q1 = "create database entertainment"
cursor.execute(Q1)

# Command for creating Table Movies:
Q2 = 'create table movies (MovieName varchar(50)primary key,ActorName varchar(50),ActressName varchar(50),DirectorName varchar(50),YearOfRelease int(4))'
cursor.execute(Q2)
print("Table Created Successfully")
# Commands for Inserting data into Movies table:
query = 'insert into movies values (%s,%s,%s,%s,%s)'
record=  ('Harry Potter 2', 'Dainel Radcliffe','Emma Watson','David Yates', '2002')
record1= ('Fast and Furious 9', 'Vin Diesel', 'Jordana Brewster', 'Justin Lin', '2021')
record2= ('Iron Man 3', 'Robert Downey, Jr.', 'Gwyneth Paltrow', 'Jon Favreau', '2013')

cursor.execute(query, record)
cursor.execute(query,record1)
cursor.execute(query,record2)
mydb.commit()
print('Records Inserted into Database')

# Commands for Querying data from Movies table:
cursor.execute('select * from movies')
data = cursor.fetchall()

for row in data:
    print('Movie Name:', row[0])
    print('Actor Name:', row[1])
    print('Actress Name:', row[2])
    print('Director Name:', row[3])
    print('Year of Release:', row[4])
    print()