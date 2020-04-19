import mysql.connector 
import sys

class Library:

	def __init__(self):
		self.db = mysql.connector.connect(host='localhost', user='username', passwd='password')
		self.dbcursor = self.db.cursor()
		
		# self.dbcursor.execute("drop database library;")
		self.dbcursor.execute("CREATE DATABASE IF NOT EXISTS library;")
		self.dbcursor.execute("USE library;")

		self.dbcursor.execute("CREATE TABLE IF NOT EXISTS books_records(book_id INT PRIMARY KEY , book_name VARCHAR(200) NOT NULL, author VARCHAR(100) NOT NULL, books_in_stock INT DEFAULT 0 );")
		self.dbcursor.execute("CREATE TABLE IF NOT EXISTS students_records(student_id INT PRIMARY KEY AUTO_INCREMENT , student_name VARCHAR(50) NOT NULL, class VARCHAR(30) NOT NULL ,semester INT NOT NULL);")
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
			print("New student added.")
		
		elif table == 'books':
			self.dbcursor.execute(insert_books, vals)
			self.dbcursor.execute(insert_initial_stock,(vals[0], vals[-1]))
			print("New book added.")
		
		elif table == 'withdraw':	
			self.dbcursor.execute("SELECT books_in_stock FROM books_records WHERE book_id = {};".format(vals[-1]))
			books_available = self.dbcursor.fetchone()[0]
			
			if books_available > 0:
				self.dbcursor.execute("SELECT book_id FROM transactions WHERE student_id = {};".format(vals[0]))
				book_list = [i[0] for i in self.dbcursor.fetchall()]
				
				if vals[-1] not in book_list:
					self.dbcursor.execute(insert_withdraw, vals)
					self.dbcursor.execute("UPDATE books_records SET books_in_stock = books_in_stock -1 WHERE book_id = {};".format(vals[-1]))
					print("Book id =  {} is withdraw by student id = {}".format(vals[-1],vals[0]))
				
				else: 
					self.dbcursor.execute("SELECT book_name FROM books_records WHERE book_id = {};".format(vals[-1]))
					bookname = self.dbcursor.fetchone()[0]
					print("Student id = {} have already taken {}.".format(vals[0],bookname))

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
				print("Book id = {} was returned by student id = {}.".format(vals[-1], vals[0]))
			else: 
				print("The id of book taken  doesn't matches to the id of book taken.")

		
		else:
			print("Sorry! The requested data is not available...")


		self.db.commit()

	def check_book_id(self, book_id):
		self.dbcursor.execute("SELECT book_name FROM books_records WHERE book_id = {};".format(book_id))
		book_no = len(self.dbcursor.fetchall())
		if book_no == 0:
			return False
		else:
			return True
	
	def check_student(self,student_id):
		self.dbcursor.execute("SELECT student_name FROM students_records WHERE student_id = {};".format(student_id))
		student_list = self.dbcursor.fetchall()
		if len(student_list) == 0:
			return [True, "Student with id = {} is not registered.".format(student_id)]
		else:
			return [False, "name = {}.".format(student_list[0][0])]

	def get_student_id(self, student_name):
		self.dbcursor.execute("SELECT student_id FROM students_records WHERE student_name = '{}';".format(student_name))	
		return self.dbcursor.fetchall()[-1][0]

	def filtering(self, table_name): 
		print("You can only select one filter method....")
		print("Default (Filter By: all)")
		filter_options = {'students_records': (('all', '*'),('id', 'student_id'),('name','student_name'),('class', 'class'), ('semester','semester')),
		'books_records':(('all', '*'), ('id','book_id'), ('name', 'book_name'), ('author', 'author'), ('stock','books_in_stock')),
		'transactions': (('all','*'), ('studentid','student_id'),('bookid', 'book_id'))}

		def print_method(methods_tuple):
			methods= [i[0] for i in methods_tuple]
			print("Filter methods available : " + ", ".join(methods))
			print("Enter filter method")
			user_method = str(input("Filter By : ")).strip().lower()
			if user_method not in methods:
				print("Filter method {} is not available.".format(user_method))
				while True:
					print("choose the correct method :")
					user_method = str(input("Filter By : ")).strip().lower()
					if user_method in methods:
						break
					else:
						pass

			else:
				opts_dict = {}
				for i in methods_tuple:
					opts_dict[i[0]] = i[-1]
				return opts_dict[user_method]

		if table_name == 'student':
			method = print_method(filter_options['students_records'])
			return method

		elif table_name == 'book':
			method = print_method(filter_options['books_records'])
			return method

		else:
			method = print_method(filter_options['transactions'])
			return method

	def get_data(self,table_name):
		
		def get_table_name(self, table_name):
			if table_name == "student":
				return "student_records"
			elif table_name == "book":
				return "books_records"
			else:
				return "transactions"
		
		def data_format(self, table_name):
			if table_name == "students_records":
				return "student id | student name | class | semester"
			elif table_name == "books_records":
				return "bookid | book name | author | books in stock"
			else: 
				return " SN | student id | book id | withdraw date | return date "

		def filter_all(self,table_name):
			self.dbcursor.execute("SELECT * FROM {};".format(table_name))
			records= self.dbcursor.fetchall()
			print(self.data_format(table_name))
			for i in records:
				record = [str(i[j]) for j in range(len(i))]
				print(record)

		
		def filter_data(self,table_name):
			method = filter_method.split('_')
			filter_value = str(input("Enter {} : ".formate(method))).lower()

			self.dbcursor.execute("SELECT * FROM {} WHERE {} = {};".format(table_name, filter_method, filter_value))
			records = self.dbcursor.fetchall()
			if len(records) > 0:
				print(self.data_format(table_name))
				for i in records:
					record = [str(i[j]) for j in range(len(i))]
					print(records)
			else:
				print("No match found ")

		table = get_table_name(table_name)
		print("would you like to choose another filter method : ")
		state = str(input('y/n : ')).strip().lower()
			
		if state == 'y':
			filter_option = filtering(table_name)
				
			if filter_method == '*':
				filter_all(self, table)
					
			else:
				filter_data(table, filter_option)

		elif state == 'n':
			filter_all(table)
		else:
			while state != 'y' or state != 'n':
				print("Enter y for yes and n for no : ")
				state = str(input('y/n : ' )).strip().lower()



class Library_Mode:
	
	def __init__(self,library_class):
	
		self.data = library_class()

	def book_insert_mode(self):
		book_name = str(input("Enter book name : "))
		book_id = int(input("Enter book id: "))
		
		flag = True
		while flag:
			flag = self.data.check_book_id(book_id)
			if flag == True:
				print("Book id is already taken. ")
				book_id = int(input("Enter new book id : "))
			# else: 
			# 	break

		author_name = str(input("Enter author name : "))
		book_stock = int(input("Enter total number of book : "))

		book_info = (book_id, book_name, author, book_stock)
		self.data.insert_into("books", book_info)
		return book_id
	
	def student_insert_mode(self):
		student_name = str(input("Enter student name : ")).lower()
		student_class = str(input("Enter class : "))
		student_semester = int(input("Enter semester : "))
		student_info = (student_name, student_class, student_semester)
		self.data.insert_into("students", student_info)
		student_id = self.data.get_student_id(student_name)
		return student_id

	def withdraw_mode(self):
		student_id =int(input("Enter student id: ")) 
		book_id = int(input("Enter book id : "))
		result = self.data.check_student(student_id)

		student_check_count = 0
		while result[0]:
			if student_check_count < 2:
				if result[0] == True:
					print(result[-1])
					student_id =int(input("Please check and Enter student id again: ")) 
					result = self.data.check_student(studetn_id)
					student_check_count+=1
			else: 
				print("would you like to register new student (y for yes)/(n for no) : ")
				choice = str(input("Enter your choice : ")).strip().lower()

				while True:
					if choice1 == 'y':
						student_id = self.student_insert_mode()
						break
					elif choice1 == 'n':
						print("would you like to re-enter the student id: ")
						choice2 = str(input("Enter ( y ) (to re-enter) or ( n ) (to exit main menu): ")).strip().lower()
						while True:
							if choice2 == 'y':
								student_check_count = 1
								break
							elif choice2 == 'n':
								self.write_mode()
								break
							else:
								choice2 = str(input("Enter ( y ) (to re-enter) or ( n ) (to exit main menu): ")).strip().lower()
						break
					else:
						print("would you like to register new student (y for yes)/(n for no) : ")
						choice = str(input("Enter your choice : ")).strip().lower()
				break			
	
		else:
			print(result[-1])

		book_check_count = 0
		while flag:
			flag = not self.data.check_book_id(book_id)
			if book_check_count < 2:
				if flag == True:
					book_id = int(input("Book is not registered. Please check and Enter book id again: "))
					book_check_count+=1

				# else: 
				# 	break
			else:
				print("would you like to register new book (y for yes)/(n for no) :")
				choice3 = str(input("Enter your choice : ")).strip().lower()
				if choice3 == 'y':
					book_id = self.book_insert_mode()
				elif choice3 == 'n':
						print("would you like to re-enter the book id: ")
						choice2 = str(input("Enter ( y ) (to re-enter) or ( n ) (to exit main menu): ")).strip().lower()
						while True:
							if choice2 == 'y':
								book_check_count = 1
								break
							elif choice2 == 'n':
								self.write_mode()
								break
							else:
								choice2 = str(input("Enter ( y ) (to re-enter) or ( n ) (to exit main menu): ")).strip().lower()

		withdraw_info = (student_id, book_id)
		self.data.insert_into('withdraw', withdraw_info)

	def return_mode(self):
		student_id = int(input("Enter student id : "))
		book_id = int(input("Enter book id : "))
		return_info = (student_id, book_id)
		self.data.insert_into('return', return_info)

	def write_mode(self):
		print("You have entered write mode of library.....")
		print(" press ( b ) for withdraw/borrow  \n press ( g ) for return \n press ( n ) to enter/add new student/member \n press ( a ) to enter/add new book \n  ")
		entry_type = str(input("Your Entry Type : ")).strip().lower()

		if entry_type == 'a':
			self.book_insert_mode()

		elif entry_type == 'n':
			self.student_insert_mode()

		elif entry_type == 'b':
			self.withdraw_mode()

		elif entry_type == 'g':
			self.return_mode()		

	def read_mode(self):
		print("You have entered read mode of library.....")
		data_available = ['student', 'book', 'transaction']
		print("Here is a list of data available to read; \n" + ", ".join(data_available))
		choice = str(input("Your choice : ")).strip().lower
		if choice in data_available:
			self.data.get_data(choice)
		else:
			while choice not in data_available:
				print("Here is a list of data available to read; \n" + ", ".join(data_available))
				choice = str(input("Your choice : ")).strip().lower()


def library_management(library_class, library_mode_class):
	print("This is a simple database mananagement for a library: ")
	print("Would you like to READ or WRITE the date: \n READ = check the data entries \n WRITE = enter new student / enter new book record / withdraw book / return book. ")
	mode = str(input("Enter (r) to read (w) to write: ")).strip().lower()
	library_mode = library_mode_class(library_class)

	if mode == "w":
		library_mode.write_mode()
	elif mode == "r":
		library_mode.read_mode()
	else:
		while mode != 'w' or mode != 'r':
			print("Would you like to write or read the data.")
			mode = str(input("Enter (r) to read (w) to write: ")).strip().lower()



library_management(Library, Library_Mode)

		


# Following are the test data for this code: 
# data = Library()
# students_infos = [('jackson coffee', 'bsc cs', 3), ('jhonson tea', 'bsc physics', 2), 
# ('ellen talker', 'bsc maths', 7), ('rakesh rana', 'bsc chemistry', 1), ('ruby red', 'bsc biology', 2), 
# ('scralet charl', 'msc physics', 4), ('charl jonshon', 'bsc cs', 8), ('allen walker', 'msc maths', 1), 
# ('hari robert', 'bsc cs', 7), ('xin jin', 'bsc chemistry', 1), ('chau li ', 'msc cs', 2), 
# ('kagamaya tobio', 'bsc biology', 5), ('akashi rujaki', 'msc physics', 3), 
# ('cake pitterson', 'bsc chemistry', 5), ('barni bird', 'msc physics', 2), ('james kellson', 'msc physics', 2)]

# for i in students_infos:
# 	data.insert_into('students',i)

# books_infos = [(101, 'fundamental of c programming', 'dennis ritchie', 50), 
# (102, 'physics', 'isaac newton', 50), (103, 'organic chemistry', 'friedrich wohler', 30), 
# (104, 'the selfish gene', 'richard dawkins', 20), (105, 'data mining', 'jiawei han', 25), 
# (106, 'physics numerical 2nd edition', 'albert einstein', 50), (107, 'physical chemistry', 'wilhelm ostwald', 40), 
# (108, 'object oriented programming in java', 'alan kay', 30), (109, 'on the origin of species', 'charles darwin', 15),
# (110, 'working with dbms', 'charles babbage', 10), (111, 'calculus 1', 'isaac newton', 20), 
# (112, 'calculus 2', 'isaac newton', 20), (113, 'calculus 3', 'isaac newton', 25), (114, 'how to lie with statistics', 'darrell huff', 40), 
# (115, 'the elements of  statistical learning', 'trevor hastie', 25), (116, 'discrete mathematics with applications', 'susanna s. epp', 50)]

# for i in books_infos:	
# 	data.insert_into('books', i)

# withdraw_infos = [(1,101),(1,110),(2,102),(2,111),(3,111),(3,114),
# (4,103),(5,109),(5,103),(6,112),(6,106),(7,105),(7,116),(8,116),
# (8,115),(9,114),(9,108),(10,107),(10,103),(11,110),(12,109),(12,107),
# (13,102),(14,107),(15,102),(15,103)]

# for i in withdraw_infos:
# 	data.insert_into('withdraw', i)

# return_info = [(1,101),(1,110),(5,103),(8,116),(3,111),(9,114),(12,107)]

# for i in return_info:
# 	data.insert_into('return', i)


