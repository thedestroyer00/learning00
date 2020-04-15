import mysql.connector 

class Library:

	def __init__(self):
		self.db = mysql.connector.connect(host='localhost', user='nischal', passwd='nischal12345')
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
