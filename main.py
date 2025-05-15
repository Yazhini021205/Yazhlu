import mysql.connector

con = mysql.connector.connect(

    host = "localhost",
    user = "root",
    password = "",
    database = "python_new"
)

# if con :
#     print("Connection Successful")
# else:
#     print("Connection Failed")


def insert():
    name = input("Enter Your Name: ")
    email = input("Enter Your Email: ")
    city = input("Enter Your city: ")

    res = con.cursor()
    sql = "insert into user (name,email,city) values (%s,%s,%s)"
    res.execute(sql,(name,email,city))
    con.commit()
    print("Data inserted successfully!!")

#insert()

def read():
    res = con.cursor()
    sql = "select * from user"
    res.execute(sql)
    result = res.fetchall()
    print(result)

read()