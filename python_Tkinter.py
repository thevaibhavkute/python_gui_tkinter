import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *

# value lene ke liye


def GetValue(event):
    car1.delete(0, END)
    car2.delete(0, END)
    car3.delete(0, END)
    car4.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    car1.insert(0, select['id'])
    car2.insert(0, select['carname'])
    car3.insert(0, select['carmodel'])
    car4.insert(0, select['price'])


def Add():
    studid = car1.get()
    studname = car2.get()
    coursename = car3.get()
    feee = car4.get()

    mysqldb = mysql.connector.connect(
        host="localhost", user="root", password="", database="car_manage")
    mycursor = mysqldb.cursor()

    try:
        sql = "INSERT INTO  car (id,carname,carmodel,price) VALUES (%s, %s, %s, %s)"
        val = (studid, studname, coursename, feee)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Car data inserted successfullyyyy")
        car1.delete(0, END)
        car2.delete(0, END)
        car3.delete(0, END)
        car4.delete(0, END)
        car1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


def update():
    studid = car1.get()
    studname = car2.get()
    coursename = car3.get()
    feee = car4.get()
    mysqldb = mysql.connector.connect(
        host="localhost", user="root", password="", database="car_manage")
    mycursor = mysqldb.cursor()

    try:
        sql = "Update  car set carname= %s,carmodel= %s,price= %s where id= %s"
        val = (studname, coursename, feee, studid)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo(
            "information", "Car record updated successfully")

        car1.delete(0, END)
        car2.delete(0, END)
        car3.delete(0, END)
        car4.delete(0, END)
        car1.focus_set()

    except Exception as e:

        print(e)
        mysqldb.rollback()
        mysqldb.close()


def delete():
    studid = car1.get()

    mysqldb = mysql.connector.connect(
        host="localhost", user="root", password="", database="car_manage")
    mycursor = mysqldb.cursor()

    try:
        sql = "delete from car where id = %s"
        val = (studid,)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Car record deleted successfully")

        car1.delete(0, END)
        car2.delete(0, END)
        car3.delete(0, END)
        car4.delete(0, END)
        car1.focus_set()

    except Exception as e:

        print(e)
        mysqldb.rollback()
        mysqldb.close()


def show():
    mysqldb = mysql.connector.connect(
        host="localhost", user="root", password="", database="car_manage")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT id,carname,carmodel,price FROM car")
    records = mycursor.fetchall()
    print(records)

    for i, (id, carname, carmodel, price) in enumerate(records, start=1):
        listBox.insert("", "end", values=(id, carname, carmodel, price))
        mysqldb.close()


root = Tk()
root.geometry("800x500")


bg = "black"

global car1
global car2
global car3
global car4

tk.Label(root, text="Car Management System",
         fg="black", font=(None, 30)).place(x=300, y=5)

tk.Label(root, text="Car id:").place(x=10, y=10)
Label(root, text="Car Name:").place(x=10, y=40)
Label(root, text="Car Model:").place(x=10, y=70)
Label(root, text="Price:").place(x=10, y=100)

car1 = Entry(root)
car1.place(x=140, y=10)

car2 = Entry(root)
car2.place(x=140, y=40)

car3 = Entry(root)
car3.place(x=140, y=70)

car4 = Entry(root)
car4.place(x=140, y=100)

Button(root, text="Add", command=Add, height=3, width=13).place(x=30, y=130)
Button(root, text="update", command=update,
       height=3, width=13).place(x=140, y=130)
Button(root, text="Delete", command=delete,
       height=3, width=13).place(x=250, y=130)

Button(root, text="Show", command=show,
       height=3, width=13).place(x=360, y=130)

cols = ('id', 'carname', 'carmodel', 'price')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=200)

# show()
# listBox.bind('<Double-Button-1>', GetValue)

root.mainloop()
