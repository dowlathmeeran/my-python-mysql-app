from tabulate import tabulate
import mysql.connector
con = mysql.connector.connect(host = 'localhost', username = "root", passwd = "root", database = "crud_operation")


def insert(name,age,city):
    res = con.cursor()
    sql='insert into crud(name,age,city) values (%s,%s,%s)'
    user = (name,age,city)
    res.execute(sql,user)
    con.commit()
    print("Data Inserted Successfully")

def update(name,age,city,id):
    res = con.cursor()
    sql='update crud set name=%s,age=%s,city=%s where id=%s'
    user=(name,age,city,id)
    res.execute(sql,user)
    con.commit()
    print("Data Updated Successfully")

def select():
    res = con.cursor()
    sql = 'select * from crud'
    res.execute(sql)
    #result=res.fetchone()
    #result=res.fetchmany(2)
    result=res.fetchall()
    print(tabulate(result,headers=['ID','NAME','AGE','CITY']))

def delete(id):
    res = con.cursor()
    sql='delete from crud where id=%s'
    user=(id,)
    res.execute(sql,user)
    con.commit()
    print("Data Deleted Successfully")


while True:
    print("1.Insert data")
    print("2.Update data")
    print("3.Select data")
    print("4.Delete data")
    print("5.Exit")

    choice = int(input("Enter your choice:"))

    if choice == 1:
        name = input("Enter your name:")
        age = int(input("Enter your age:"))
        city = input("Enter your city:")
        insert(name,age,city)

    elif choice == 2:
        id=int(input("Enter id:"))
        name = input("Enter your name:")
        age = int(input("Enter your age:"))
        city = input("Enter your city:")
        update(name,age,city,id)
        
    elif choice == 3:
        select()
        
    elif choice == 4:
        id = int(input("Enter the ID to delete:"))
        delete(id)
        
    elif choice == 5:
        quit()

    else:
        print("Invalid Selection. Please Try Again!")
        

