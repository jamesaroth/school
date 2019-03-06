import sqlite3

DBFILENAME = 'campus.db'



with sqlite3.connect(DBFILENAME) as conn:
    cur = conn.cursor()

    SQL=""" DELETE FROM campus"""
    cur.execute(SQL)

    SQL=""" DELETE FROM students"""
    cur.execute(SQL)


    SQL="""INSERT INTO campus (campusname,city,state) 
    VALUES ('New York University','New York','NY')
    """        
    cur.execute(SQL)

    SQL="""INSERT INTO students (campuspk,firstname,lastname,gpa,studentid) 
    VALUES ('1','James','Roth','4.0','911')
    """   

    cur.execute(SQL)
