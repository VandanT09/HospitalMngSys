# EXP - 1
#list = ["Mumbai","Pune","Kolkata","Hydrabad","Delhi"]
#print(list)
#list.append("Goa")
#print(list)
#list.remove(list[2])
#print(list)
# numbers=[1,2,3,4,5,6,7,8,9,10]
# even_num=numbers[1::2]
# print(even_num)
#-----------------------------------------------------------
#tuple=("Red","Green","Blue")
#print(tuple)
#weekdays=('Monday','Tuesday','Wednesday','Thursday','Friday')
#weekend=('Saturday','Sunday')
#new_tuple=weekdays+weekend
#print(new_tuple)
#first=tuple[0]
#third=tuple[2]
#print(first)
#print(third)
#check='Green' in tuple
#print(check)
#color1,color2,color3=tuple
#print(color1)
#print(color2)
#print(color3)
#-----------------------------------------------------------
#set1={1,3,5,7}
#set2={0,2,4,6,8,10}
#set3=set1.union(set2)
#print(set3)
#set4=set1.intersection(set2)
#print(set4)
#set1.add(9)
#set2.remove(0)
#print(set1)
#print(set2)
#check=set1.issubset(set2)
#print(check)
#-----------------------------------------------------------
#dict={'Book1':'Author1','Book2':'Author2','Book3':'Author3','Book4':'Author4'}
#print(dict)
#dict['Book5']='Author5'
#print(dict)
#del dict['Book1']
#print(dict)
#check='Book6' in dict
#print(check)
#for book,author in dict.items():
#    print({book},{author})
#-----------------------------------------------------------
# def histogram(l):
#     count = {}
#     for num in l:
#         if num in count:
#             count[num] += 1
#         else:
#             count[num] = 1
#     sorted_count = sorted(count.items(), key = lambda item:(item[1],item[0]))
#     result = [(key,value) for key,value in sorted_count]
#     return result

# l = [13,18,13,18,9,9,9,4]
# result = histogram(l)
# print(result)

# from itertools import combinations

# def find_combinations(l, target):
#     result = []
#     for r in range(1, len(l) + 1):
#         for combo in combinations(l, r):
#             if sum(combo) == target:
#                 result.append(combo)
#     return result

# # Example usage:
# l = [10, 20, 10, 40, 60, 70]
# target = 70

# combinations_result = find_combinations(l, target)
# print(combinations_result)
#-----------------------------------------------------------
# def perfNum(num):
#     sum = 0
#     for i in range(1,num):
#         if(num%i==0):
#             sum += i
#     if(sum == num):
#         return True
#     else:
#         return False
# num = int(input('Enter a number :'))
# if(perfNum(num)):
#      print(num, "is a perfect number!")
# else:
#      print(num, "is not a perfect number.")
#-----------------------------------------------------------
# EXP - 2
# def towerOfHanoi(n,source,auxiliary,target):
#     if n == 1:
#         print(f"Move disk 1 from {source} to {target}")
#         return
#     towerOfHanoi(n - 1, source, target, auxiliary)
#     print(f"Move disk {n} from {source} to {target}")
#     towerOfHanoi(n - 1, auxiliary, source, target)
# n = int(input("Enter The Number Of Disks : "))
# towerOfHanoi(n,'A','B','C')
#-----------------------------------------------------------
# n1 = int(input('Enter number 1:'))
# n2 = int(input('Enter number 2:'))
# x = lambda n1,n2: n1 if n1>n2 else n2
# print(x(n1,n2))
#-----------------------------------------------------------
# list1 = [1,3,5,7,9]
# list2 = [2,4,6,8,10]
# result = list(map(lambda x,y: x+y, list1,list2))
# print(result)
#-----------------------------------------------------------
# input_list = [1,2,3,4,5,6,7,8,9,10]
# odd_numbers = list(filter(lambda x: x%2!=0, input_list))
# cube_odd_numbers = list(map(lambda x: x**3, odd_numbers))
# print(cube_odd_numbers)
#-----------------------------------------------------------
# EXP - 3
# class Employee:
#     def __init__(self,employee_id,name):
#         self.employee_id = employee_id
#         self.name = name

# class Developer(Employee):
#     def __init__(self,employee_id,name,programming_language):
#         super().__init__(employee_id,name)
#         self.programming_language = programming_language

# class Tester(Employee):
#     def __init__(self,employee_id,name,testing_type):
#         super().__init__(employee_id,name)
#         self.testing_type = testing_type

# class Manager(Employee):
#     def __init__(self,employee_id,name):
#         super().__init__(employee_id,name)
#         self.managed_employees = []
    
#     def add_employee(self,employee):
#         self.managed_employees.append(employee)
#         print(f"{employee.name} is added to the team")
    
#     def remove_employee(self,employee):
#         if employee in self.managed_employees:
#             self.managed_employees.remove(employee)
#             print(f"{employee.name} removed from the team")
#         else:
#             print(f"{employee.name} is not part of the team")
    
#     def display_managed_employees(self):
#         print("Employees managed by ",self.name)
#         for employee in self.managed_employees:
#             print(f"ID : {employee.employee_id}, Name : {employee.name}")

# if __name__ == "__main__":
#     dev = Developer(1,"Vandan Thakar","Python")
#     tester = Tester(2,"Vandan Kava","Debugging")
#     manager = Manager(3,"Varun Tank")

#     manager.add_employee(dev)
#     manager.add_employee(tester)

#     manager.display_managed_employees()

#     manager.remove_employee(tester)

#     manager.display_managed_employees()
#-----------------------------------------------------------
# EXP - 4
# class CustomError(Exception):
#     def __init__(self,message = "A custom error occured!"):
#         self.message = message
# try:
#     user_input = int(input("Enter a number :"))
#     print(f"Entered number : {user_input}")

#     num = int(input("Enter number :"))
#     divisor = int(input("Enter divisor:"))
#     result = num/divisor
#     print(f"Result of division :{result}")

#     list = [1,2,3,4]
#     print(list[5])

#     check = int(input('Enter number : '))
#     if check in range(1,100):
#         print("Ok!")
#     else:
#         raise CustomError("Error")
    
# except ValueError as ve:
#     print(f"Value Error :{ve}")
# except ZeroDivisionError as zd:
#     print(f"Zero Division Error (divisor cannot be 0) :{zd}")
# except IndexError as ie:
#     print(f"List Index Out Of Bounds :{ie}")
# except CustomError as ce:
#     print(f"Custom Error :{ce}")
# except Exception as e:
#     print(f"An unexpected error occured :{e}")
# print("Program Continue...")
#-----------------------------------------------------------
# EXP - 5
# import random

# random_numbers = [random.randint(1,10000) for i in range(10000)]

# with open("random_numbers.txt","w") as file:
#     for number in random_numbers:
#         file.write(str(number) + '\n')

# with open("random_numbers.txt","r") as file:
#     numbers = [int(line.strip()) for line in file]
# sorted_numbers = sorted(numbers)

# with open("sorted_numbers.txt","w") as file:
#     for number in sorted_numbers:
#         file.write(str(number) + '\n')
# ----------------------------------------
# EXP - 6
# import re

# text = """
# Mr. Anderson
# Ms. Thareja
# Mrs. Morris
# Mr. Roy
# Ms. Gandhi
# Mrs. Modi

# https://www.google.com
# http://www.udemy.com
# www.udacity.com
# https://www.stackoverflow.com
# http://www.djsce.ac.in
# https://plus.google.com

# rishit.grover@gmail.com
# kapeesh.grover@yahoo.co.in
# abhishek.shah@gmail.com
# shahp98@gmail.com
# demo_user@gmail.com
# rolflmoa@yahoo.co.in

# 27777647
# 233*333*88
# 455-78-888
# 022-240-93836
# 02642*221*381
# """

# names = re.findall(r'(Mr\.|Ms\.|Mrs\.)\s([A-Za-z]+)\s', text)
# print(f"Name of the Users: {[f'{title}{name}' for title, name in names]}")

# websites = re.findall(r'(?:https?://)?(www\.[^\s]+)', text)
# print("Websites Names:", websites)

# emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
# print("Email IDs:", emails)

# phone_no = re.findall(r'\b(?:\d{3}[-.*])*\d{2,5}\b', text)
# print("Phone Numbers:", phone_no)

# import re

# def count_info(input_string):
#     words = re.findall(r'\b\w+\b', input_string)
#     word_count = len(words)
#     sentence_count = len(re.findall(r'[.!?]', input_string))

#     line_count = len(re.findall(r'\n', input_string)) + 1

#     words_less_than_7 = [word for word in words if len(word) < 7]
#     words_greater_than_3 = [word for word in words if len(word) > 3]

#     return {
#         'word_count': word_count,
#         'sentence_count': sentence_count,
#         'line_count': line_count,
#         'words_less_than_7': words_less_than_7,
#         'words_greater_than_3': words_greater_than_3
#     }

# input_text = """This is a sample sentence. It has multiple lines.
# Each line is separated by a newline character.
# Short words like 'dog' and 'cat' are less than 7 characters,
# while longer words like 'elephant' and 'python' are greater than 3 characters."""

# result = count_info(input_text)
# print("Word count:", result['word_count'])
# print("Sentence count:", result['sentence_count'])
# print("Line count:", result['line_count'])
# print("Words with length less than 7:", result['words_less_than_7'])
# print("Words with length greater than 3:", result['words_greater_than_3'])
#-----------------------------------------------------------
# EXP - 7
# import sqlite3

# def create_table(cursor):
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY,
#             name TEXT NOT NULL,
#             age INTEGER
#         )
#     ''')
#     print("Table created successfully")

# def insert_values(cursor, name, age):
#     cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
#     print("Values inserted successfully")

# def delete_row(cursor, name):
#     cursor.execute("DELETE FROM users WHERE name=?", (name,))
#     print("Row deleted successfully")

# def display_rows(cursor):
#     cursor.execute("SELECT * FROM users")
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)

# def update_values(cursor, id, age):
#     cursor.execute("UPDATE users SET age=? WHERE id=?", (age, id))
#     print("Values updated successfully")

# def search_record(cursor, name):
#     cursor.execute("SELECT * FROM users WHERE name=?", (name,))
#     row = cursor.fetchone()
#     if row:
#         print("Record found:", row)
#     else:
#         print("Record not found")

# def main():
#     connection = sqlite3.connect('example.db')
#     cursor = connection.cursor()
#     create_table(cursor)

#     while True:
#         print("\nMenu:")
#         print("1. Insert values")
#         print("2. Delete a row")
#         print("3. Display rows")
#         print("4. Update values")
#         print("5. Search record")
#         print("6. Exit")

#         choice = input("Enter your choice: ")

#         if choice == '1':
#             name = input("Enter name: ")
#             age = int(input("Enter age: "))
#             insert_values(cursor, name, age)

#         elif choice == '2':
#             name = input("Enter name to delete row: ")
#             delete_row(cursor, name)

#         elif choice == '3':
#             display_rows(cursor)

#         elif choice == '4':
#             id = int(input("Enter ID to update: "))
#             age = int(input("Enter new age: "))
#             update_values(cursor, id, age)

#         elif choice == '5':
#             name = input("Enter name to search: ")
#             search_record(cursor, name)

#         elif choice == '6':
#             break

#         else:
#             print("Invalid choice. Please try again.")

#     connection.commit()
#     connection.close()

# main()
#-----------------------------------------------------------
# EXP - 8
# server-side
# import socket
# host = "127.0.0.1"
# port = 10000
# server = socket.socket()
# server.bind((host,port))
# server.listen()
# conn, addr = server.accept()
# print('Connection Established with Vandan!')
# while True:
#     x = conn.recv(1024)
#     x=x.decode()
#     print(x)
#     y = input('Enter Data :')
#     data = y.encode()
#     conn.send(data)
#     if(y=='Close'):
#         break
# server.close()

# client-side
# import socket
# host = "127.0.0.1"
# port = 10000
# print('Connecting to servers......')
# cs = socket.socket()
# print('........wait for it USER.........')
# cs.connect((host,port))
# print('Connection established to Vandan\'s server!\nWelcome to Vandan\'s SERVER')
# while True:
#     x = input('Enter message to be sent :')
#     y = x.encode()
#     cs.send(y)
#     data = (cs.recv(1024)).decode()
#     if(data == 'Close'):
#         break
#     print(data)
# print('Server is closed')
# cs.close()
#-----------------------------------------------------------
# EXP - 9
# import tkinter as tk

# def on_click(button_value):
#     current_text = entry_var.get()
    
#     if button_value == 'C':
#         entry_var.set('')
#     elif button_value == '=':
#         try:
#             result = eval(current_text)
#             entry_var.set(str(result))
#         except:
#             entry_var.set('Error')
#     else:
#         entry_var.set(current_text + button_value)

# window = tk.Tk()
# window.title("Basic Calculator")

# entry_var = tk.StringVar()
# entry = tk.Entry(window, textvariable=entry_var, font=('Arial', 14))
# entry.grid(row=0, column=0, columnspan=4, padx=8, pady=8)

# buttons = [
#     '7', '8', '9', '/',
#     '4', '5', '6', '*',
#     '1', '2', '3', '-',
#     '0', 'C', '=', '+'
# ]

# row_val = 1
# col_val = 0
# for button in buttons:
#     tk.Button(window, text=button, padx=20, pady=20, font=('Arial', 14),
#               command=lambda btn=button: on_click(btn)).grid(row=row_val, column=col_val)
    
#     col_val += 1
#     if col_val > 3:
#         col_val = 0
#         row_val += 1

# window.mainloop()
#-----------------------------------------------------------