import sqlite3 as sql

def insert_customer(company, email):
    # SQL statement to insert into database goes here
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO customers(company,email) VALUES (?,?)",(company, email))
        con.commit()
#con = sql.connect("app.db")
#sql code here
#con.commit()
#con.close
#this is the same as above code

def retrieve_customers():
    # SQL statement to query database goes here
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        result = 