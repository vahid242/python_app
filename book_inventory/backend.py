import sqlite3

def connect():
    # stablish a connection to database
    conn=sqlite3.connect("books.db")
    # cursor like a pointer to row of table
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    # commit changes
    conn.commit()
    # close connection
    conn.close()

def insert(title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    # Fetches all (remaining) rows of a query result, returning a list
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?, author=? ,year=? ,isbn=? WHERE id=?", (title,author,year,isbn,id))
    conn.commit()
    conn.close()

connect()
# insert("The Sun", "John Smith", 1818, 321856280)
# delete(3)
# update(4, "The Moon", "John Smith", 1818, 321856281)
# print(view())
# print(search(author="Ernest Hemingway"))