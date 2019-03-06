import sqlite3
import random

dbfile="campus.db"

def list_campus(campuspk):
    with sqlite3.Connection(dbfile) as conn:
        conn.row_factory = sqlite3.Row
        cur=conn.cursor()

        SQL = """
            SELECT * FROM students WHERE campuspk=? 
            """
        cur.execute(SQL, (campuspk,))
        return cur.fetchall()

def make_campus(campusname, city, state):
    with sqlite3.Connection(dbfile) as conn:
        cur=conn.cursor()

        SQL = """
            INSERT INTO campus (campusname,city,state)
            VALUES (?,?,?)
        """
        cur.execute(SQL, (campusname,city,state))

def modify_campus(campuspk):
    with sqlite3.connect(dbfile) as conn:
        cur = conn.cursor()
        SQLPATTERN = "SELECT * FROM {table} {where_clause}"
    pass

def delete_campus(campuspk):
    with sqlite3.Connection(dbfile) as conn:
        cur=conn.cursor()
        SQL = """
            DELETE FROM campus WHERE campuspk = ?
        """
        cur.execute(SQL, (campuspk,))

def check_id(studentid):
    with sqlite3.Connection(dbfile) as conn:
        cur=conn.cursor()
        SQL = """
            SELECT * FROM students WHERE studentid = ?
        """
        cur.execute(SQL, (studentid,))
        return cur.fetchone()

def make_student(campuspk,firstname,lastname, gpa):
    with sqlite3.Connection(dbfile) as conn:
        cur=conn.cursor()
        studentid = random.randint(0, 1000)
        while check_id(studentid) != None:
            studentid = random.randint(0, 1000)
        
        SQL = """
            INSERT INTO students (campuspk,firstname,lastname, gpa, studentid)
            VALUES (?,?,?,?,?)
        """
        cur.execute(SQL, (campuspk,firstname,lastname, gpa, studentid))

def modify_student(studentspk):
    pass

def delete_student(studentspk):
    with sqlite3.Connection(dbfile) as conn:
        cur=conn.cursor()
        SQL = """
            DELETE FROM students WHERE studentspk = ?
        """
        cur.execute(SQL, (studentspk,))
