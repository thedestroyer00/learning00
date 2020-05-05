# This is a simple library management system written in python3 using mongodb...

import pymongo
from pprint import pprint
from datetime import datetime

class Library:
    
    def __init__(self):
        self.library_client = pymongo.MongoClient()
        self.db = self.library_client["library_database"]
        self.students_records = self.db["students_records"]
        self.books_records = self.db["books_records"]
        self.transactions = self.db["transactions"]
        self.books_stocks = self.db["books_initial_stock"]
        
        
    def insert_student(self, student_info):
        self.students_records.insert_one(student_info)
        print("following data is inserted.")
        pprint(self.students_records.find_one(student_info))
        
    
    def insert_book(self, book_info):
        book_flag = self.check_book(book_info['book_id'])
        
        if book_flag == False:
            self.books_records.insert_one(book_info)
            book_stock_info = {"book_id": book_info["book_id"],
                               "book_initial_stock": book_info["book_in_stock"]
                               }
            self.books_stocks.insert_one(book_stock_info)
            print("following data is inserted.")
            pprint(self.books_records.find_one(book_info))
        else:
            print(f"Book with id = {book_info['book_id']} already exits.")
        
    
    def insert_transaction(self, mode, transaction_info):
        if mode == 'b':
            student_list = self.books_records.find_one({"book_id": transaction_info["book_id"]})["students_ids"]
            if transaction_info["student_id"] in student_list:
                print(f"Student: {transaction_info['student_id']} has already taken book: {transaction_info['book_id']}")
            else:
                student_list.append(transaction_info["student_id"])
                stock_num = self.books_records.find_one({"book_id": transaction_info["book_id"]})["book_in_stock"]
                self.books_records.update_one({"book_id":transaction_info["book_id"]}, {"$set": {"students_ids": student_list, "book_in_stock":stock_num-1}})  
                self.transactions.insert_one(transaction_info)
                print("book withdraw record")
                pprint(self.transactions.find_one(transaction_info))
        
        else:
            book_record = self.transactions.find_one(transaction_info)
            if book_record == None:
                print('Book id or Student id is wrong!')
            else:
                student_list = self.books_records.find_one({"book_id": transaction_info["book_id"]})["students_ids"]
                student_list.remove(transaction_info["student_id"])
                stock_num = self.books_records.find_one({"book_id": transaction_info["book_id"]})["book_in_stock"]
                self.books_records.update_one({"book_id":transaction_info["book_id"]}, {"$set": {"students_ids": student_list, "book_in_stock":stock_num+1}})
                self.transactions.update_one(transaction_info,{"$set": {"return_date": str(datetime.now().date())}})
                print("book return record")
                pprint(self.transactions.find_one(transaction_info))
            
    
    def check_student(self, student_id):
        student_data = self.students_records.find_one({"student_id": student_id})
        if student_data == None: 
            return False
        else: 
            return True
        
    
    def check_book(self, book_id):
        book_data = self.books_records.find_one({"book_id": book_id})
        if book_data == None: 
            return False
        else:
            return True
        
        
            
class Get_info:
    def __init__(self):
        self.library = Library()
        
    def students(self):
        student_record = list(self.library.students_records.find())
        if len(student_record) == 0:
            student_id = 1
        else:
            student_id = student_record[-1]["student_id"]+1
            
        name = input("Student Name: ").lower()
        student_class = input("Student class: ").lower()
        semester = int(input("semester: "))
        contact = input("Contact no: ")
        address = input("Student address: ").lower()
        
        student_info = {"student_id": student_id,
                        "name": name,
                        "class": student_class,
                        "semester": semester,
                        "contact": contact,
                        "address": address}
        self.library.insert_student(student_info)
        
    def books(self):
        name = input("Book name: ").lower()
        author = input("Author : ").lower()
        book_id = int(input("Book id : "))
        book_stock = int(input("Number of books available(in stock): "))
        
        book_info = {"book_id": book_id,
                     "book_name": name,
                     "author": author,
                     "book_in_stock": book_stock,
                     "students_ids": []}
        self.library.insert_book(book_info)
    
    def registration(self, record_name):
        while True:
            print(f"would you like register new {record_name}")
            choice = input("[y/n]: ").lower()
            if choice == 'y' or choice == 'n':
                break
            else: pass
            
        if choice == 'y':
            if record_name == 'student':
                self.students()
            else:
                self.books()
        else:
            print("exit")
    
        
        
    def withdraw(self):
        student_id = int(input("Student id : "))
        book_id = int(input("Book id : "))
        with_date = str(datetime.now().date())
        
        if self.library.check_student(student_id):
            if self.library.check_book(book_id):
                book_info = self.library.books_records.find_one({"book_id": book_id})
                book_num = book_info["book_in_stock"]
                if book_num <= 0:
                    book_name = book_info["book_name"]
                    print(f"Sorry! we don't have {book_id} : {book_name} currently.")
                
                else:
                    withdraw_info = {"student_id": student_id,
                                        "book_id": book_id,
                                        "withdraw_date": with_date,
                                        "return_date": ''
                                        }
                    self.library.insert_transaction('b', withdraw_info)
            else:
                print(f"No book with id = {book_id}")
                self.registration('book')        
        else:
            print(f"No student with id ={student_id}")
            self.registration('student') 
        
    def insert_return(self):
        student_id = int(input("Student id : "))
        book_id = int(input("Book id : "))
    
        return_info = {"student_id": student_id,
                       "book_id": book_id}
        
        self.library.insert_transaction('r', return_info)
        
class Show_records:
    
    def __init__(self):
        self.library = Library()
        
    def show_student_record(self):
        choices = ('all','id', 'class', 'name', 'semester', 'address')
        print("Find student By: " + ', '.join(choices))
        c = input("enter filter method : ").strip().lower()
        if c in choices :
            if c == "all":
                pprint(list(self.library.students_records.find()))
            elif c == "id":
                sid = int(input("Enter student id: "))
                student_list = list(self.library.students_records.find({"student_id":sid }))
                pprint(student_list) if len(student_list) > 0 else print(f"No student with {c} = {sid}.")
                
            else: 
                choice2 = input(f"Enter {c}: ").lower()
                if c == "semester":
                    choice2 = int(choice2)
                student_list = list(self.library.students_records.find({c:choice2}))
                pprint(student_list) if len(student_list) > 0 else print(f"No student with {c} = {choice2}.")
        else:
            print("Entered method is not available")
            print("Exit")
    
    
    def show_book_record(self):
        choices = ('all', 'id', 'name', 'author')
        print("Find book By: " + ', '.join(choices))
        c = input("enter filter method : ").strip().lower()
        if c in choices:
            if c == "all":
                pprint(list(self.library.books_records.find()))
            elif c == "author":
                author = input("Enter author name: ").lower()
                book_list = list(self.library.books_records.find({c:author}))
                pprint(book_list) if len(book_list) > 0 else print(f"No book with {c} = {author}.")
            else:
                method = "_".join(["book", c])
                choice2 = input(f"Enter {c}: ").lower()
                if c == "id":
                    choice2 = int(choice2)
                book_list = list(self.library.books_records.find({method:choice2}))
                pprint(book_list) if len(book_list) > 0 else print(f"No book with {c} = {choice2}.")
                
        else:
            print("Entered method is not available")
            print("Exit")
    
    
    def show_transaction(self):
        choices = ('all', 'student', 'book')
        print("Find book By: " + ', '.join(choices))
        c = input("enter filter method : ").strip().lower()
        if c in choices:
            if c == "all":
                pprint(list(self.library.transactions.find()))
            else:
                choice2 = int(input(f"Enter {c} id: "))
                method = c+"_id"
                transaction_list = list(self.library.transactions.find({method: choice2}))
                pprint(transaction_list) if len(transaction_list) > 0 else print(f"No record with {c} = {choice2}")
                
        else:
            print("Entered method is not available")
            print("Exit")
            
        

        
def outlook():
    print("This is a simple library management project: ")
    print("write mode allows to register new book/student and to perform transaction")
    print("read mode allows to check to check details about book/students/transaction")
    print(" w : Enter write mode \n r : read mode")
    choice = input("Enter choice : ").strip().lower()
    
    if choice == 'w':
        lib = Get_info()
        print(" ns : register new student \n nb : register new book (use by authorized people only) \n t : borrow or return a book")
        user_choice = input("Enter choice : ").strip().lower()
        if user_choice == "ns":
            print("student registration mode entered: ")
            lib.students()
        elif user_choice == "nb":
            print("book registartion mode entered : ")
            lib.books()
        elif user_choice == "t":
            print("transaction mode entered : ")
            print(" b : to borrow a book \n rt : to return a book ")
            user_choice2 = input("Enter choice : ").strip().lower()
            if user_choice2 == "b":
                lib.withdraw()
            elif user_choice2 == "rt":
                lib.insert_return()
            else:
                print("Entered method is not available")
                print("Exit")
        else: 
            print("Entered method is not available")
            print("Exit")
   
    elif choice == 'r':
        lib = Show_records()
        print(" s : to get student information \n b : to get book information \n t : to get transaction information")
        user_choice = input("Enter choice : ").strip().lower()
        if user_choice == "s":
            lib.show_student_record()
        elif user_choice == "b":
            lib.show_book_record()
        elif user_choice == "t":
            lib.show_transaction()
        else:
            print("Entered method is not available")
            print("Exit")
        
    

outlook()
 
        
