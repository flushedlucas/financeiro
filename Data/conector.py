import mysql.connector

# host="lucas-Inspiron-5558",
# user="root",
# password=""

def connect_mysql(host_in, user_in, password_in):
    mydb = mysql.connector.connect(
    host = host_in,
    user = user_in,
    password = password_in
    )
    return mydb

# print(mydb)