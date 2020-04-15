import mysql.connector 

class Library:

	def __init__(self):
		self.db = mysql.connector.connect(host='localhost', user='username', passwd='password')
		self.dbcursor = self.db.cursor()
		
		# self.dbcursor.execute("drop database library;")
		self.dbcursor.execute("CREATE DATABASE IF NOT EXISTS library;")
		self.dbcursor.execute("USE library;")

		self.dbcursor.execute("CREATE TABLE IF NOT EXISTS books_records(book_id INT PRIMARY KEY , book_name VARCHAR(150) NOT NULL, author VARCHAR(50) NOT NULL, books_in_stock INT DEFAULT 0 );")
		self.dbcursor.execute("CREATE TABLE IF NOT EXISTS students_records(student_id INT PRIMARY KEY AUTO_INCREMENT , student_name VARCHAR(50) NOT NULL, class VARCHAR(20) NOT NULL ,semester INT NOT NULL);")
		self.dbcursor.execute("CREATE TABLE IF NOT EXISTS transactions(sn INT AUTO_INCREMENT PRIMARY KEY, student_id INT , book_id INT ,withdraw_date DATE NOT NULL DEFAULT CURDATE(), return_date DATE,FOREIGN KEY (student_id) REFERENCES students_records(student_id), FOREIGN KEY (book_id) REFERENCES books_records(book_id));")
		self.dbcursor.execute("CREATE TABLE IF NOT EXISTS books_initial_stock(book_id INT, books_stock INT, FOREIGN KEY (book_id) REFERENCES books_records(book_id));")
	
	def insert_into(self, table, vals):
		insert_students = "INSERT INTO students_records(student_name, class, semester) VALUES(%s, %s, %s);"
		insert_books = "INSERT INTO books_records(book_id, book_name, author, books_in_stock) VALUES(%s, %s,%s,%s);"
		insert_withdraw = "INSERT INTO transactions(student_id, book_id) VALUES(%s, %s);"
		transaction_record = "SELECT book_id FROM transactions WHERE  student_id = {};".format(vals[0])
		insert_return = "UPDATE transactions SET return_date = CURDATE() WHERE student_id = {} AND book_id = {};".format(vals[0], vals[1])
		insert_initial_stock = "INSERT INTO books_initial_stock(book_id,books_stock) VALUES(%s,%s);"
		
		if table == 'students':
			self.dbcursor.execute(insert_students, vals)
		
		elif table == 'books':
			self.dbcursor.execute(insert_books, vals)
			self.dbcursor.execute(insert_initial_stock,(vals[0], vals[-1]))
		
		elif table == 'withdraw':	
			self.dbcursor.execute("SELECT books_in_stock FROM books_records WHERE book_id = {};".format(vals[-1]))
			books_available = self.dbcursor.fetchone()[0]
			
			if books_available > 0:
				self.dbcursor.execute(insert_withdraw, vals)
				self.dbcursor.execute("UPDATE books_records SET books_in_stock = books_in_stock -1 WHERE book_id = {};".format(vals[-1]))
			else:
				self.dbcursor.execute("SELECT book_name FROM books_records WHERE book_id = {};".format(vals[-1]))
				bookname = self.dbcursor.fetchone()[0]
				print("Sorry! We are out of stock. We don't have {} right now.".format(bookname))
		

		elif table == 'return':
			self.dbcursor.execute(transaction_record)
			book_taken = self.dbcursor.fetchall()

			flag = True
			for i in book_taken:
				
				if i[0] == vals[-1]:
					flag = True
					self.dbcursor.execute(insert_return)
					self.dbcursor.execute("UPDATE books_records SET books_in_stock = books_in_stock + 1 WHERE book_id = {};".format(vals[-1]))
					break
				
				else: 
					flag = False

			if flag:
				print('The book was returned.')
			else: 
				print("The book id doesn't matches to the book taken.")
		
		else:
			print("Sorry! The requested data is not available...")


		self.db.commit()


data = Library()

# following are the dummy data for this code.

# students_infos = [('Jackson Coffee', 'Bsc CS', 3),('Jhonson Tea', 'Bsc Physics', 2),('Ellen Talker', 'Bsc Maths', 7),
# ('Rakesh Rana', 'Bsc Chemistry', 1),('Ruby Red', 'Bsc Biology', 2),('Scralet Charl', 'Msc Physics', 4),
# ('Charl Jonshon', 'Bsc CS', 8),('Allen Walker', 'Msc Maths', 1),('Hari Robert', 'Bsc CS', 7),
# ('Xin Jin', 'Bsc Chemistry', 1),('Chau Li ', 'Msc CS', 2),('Kagamaya Tobio', 'Bsc Biology', 5),
# ('Akashi Rujaki', 'Msc Physics', 3),('Cake Pitterson', 'Bsc Chemistry', 5),('Barni Bird', 'Msc Physics', 2)]

# for i in students_infos:
# 	data.insert_into('students',i)

# books_infos = [(101, 'Fundamental of C Programming', 'Dennis Ritchie', 50),(102, 'Physics', 'Isaac Newton', 50),(103, 'Organic Chemistry', 'Friedrich Wohler', 30),(104, 'The selfish Gene', 'Richard Dawkins', 20),
# (105, 'Data Mining', 'Jiawei Han', 25),(106, 'Physics Numerical 2nd Edition', 'Albert Einstein', 50),(107, 'Physical Chemistry', 'Wilhelm Ostwald', 40),
# (108, 'Object Oriented Programming in Java', 'Alan Kay', 30),(109, 'On the Origin of species', 'Charles Darwin', 15),(110, 'Working with DBMS', 'Charles Babbage', 10),
# (111,'Calculus 1','Isaac Newton', 20),(112,'Calculus 2','Isaac Newton', 20),(113,'Calculus 3','Isaac Newton', 25),(114,'How to Lie with Statistics','Darrell Huff', 40),
# (115,'The Elements of  Statistical Learning','Trevor Hastie', 25),(116,'Discrete mathematics with applications','Susanna S. Epp', 50)]

# for i in books_infos:	
# 	data.insert_into('books', i)

# transactions_infos = [(1,101),(1,110),(2,102),(2,111),(3,111),(3,114),
# (4,103),(5,109),(5,103),(6,112),(6,106),(7,105),(7,116),(8,116),
# (8,115),(9,114),(9,108),(10,107),(10,103),(11,110),(12,109),(12,107),
# (13,102),(14,107),(15,102),(15,103)]

# for i in transactions_infos:
# 	data.insert_into('withdraw', i)

# return_info = [(1,101),(1,110),(5,103),(8,116),(3,111),(9,114),(12,107)]

# for i in return_info:
# 	data.insert_into('return', i)

