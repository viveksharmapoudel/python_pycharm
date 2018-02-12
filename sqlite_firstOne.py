import  sqlite3
import sys

def printDB():
    try:
        result=theCursor.execute("SELECT ID,FName,LName, Age, Address,Salary,HireDate FROM Employees")

        for row in result:
            print("ID:",row[0])
            print("FName:",row[1])
            print("LName",row[2])
            print("age:",row[3])
            print("Address:",row[4])
            print("Salary:",row[5])
            print("Hiredate:",row[6])
    except sqlite3.OperationalError:
        print("The Table Doesn't Exist")
    except:
        print("Couldn't Retrieve Data From Database")

db_conn= sqlite3.connect('test.db')

theCursor= db_conn.cursor()

print("Database Created")
db_conn.execute("DROP TABLE IF EXISTS Employees")
db_conn.commit()

try:
    db_conn.execute("CREATE TABLE Employees(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,FName TEXT NOT NULL,LName TEXT NOT NULL, Age INTEGER NOT NULL, Address TEXT, SALARY REAL,HireDate TEXT); ")
    db_conn.commit()

except sqlite3.OperationalError:
    print("table couldn't be created")


print("table Created")

db_conn.execute(" INSERT INTO Employees (FName,LName,Age,Address,Salary,HireDate)VALUES('vivek','sharma','23','ktm','150000',date('now'))")
db_conn.commit()

printDB()

db_conn.close()

print("database Closed")