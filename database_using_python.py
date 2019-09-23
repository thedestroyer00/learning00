# first create a database using mysql or by using python as following

import mysql.connector 

mydb = mysql.connector.connect( host = 'localhost', user= 'username', passwd = 'password')

mycursor = mydb.cursor()
mycursor.execute('CREATE DATABASE test_database')

#This will create the database 
#Now to create a table and  insert in the database or table


import mysql.connector

mydb = mysql.connector.connect(host = "localhost", user = "username", passwd = "password", database = "test_database")

mycursor = mydb.cursor()
mycursor.execute('create table student_data  (student_id int not null primary key auto_increment ,name varchar(25) not null, subject varchar(25) defult "not choosen" )')

mycursor.execute('insert into student_data (name, subject) values ("student1","computer science"), ("student2", "physics"), ("student3", "chemistry")')
mydb.commit()  

#mydb.commit most be included otherwise no change or no data will be inserted in the databae


#finally to display data 
import mysql.connector 

mydb = mysql.connector.connect(host = 'localhost', user = 'username', passwd = 'password', database = 'test_database')
mycursor = mycursor.cursor()
mycursor.execute('select * from studen_data')
for i in mycursor:
	print(i)









