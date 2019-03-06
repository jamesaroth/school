import sqlite3

DBFILENAME = 'campus.db'


def create_db(dbfilename=DBFILENAME):
    with sqlite3.connect(dbfilename) as conn:
        cur = conn.cursor()

        SQL = """ DROP TABLE IF EXISTS campus;"""
        cur.execute(SQL)

        SQL = """
        CREATE TABLE campus (
            campuspk INTEGER PRIMARY KEY AUTOINCREMENT,
            campusname VARCHAR(255),
            city VARCHAR(50),
            state VARCHAR(2)
        );
        """
        cur.execute(SQL)

        SQL = """ DROP TABLE IF EXISTS students;"""
        cur.execute(SQL)

        SQL = """
        CREATE TABLE students (
            studentspk INTEGER PRIMARY KEY AUTOINCREMENT,
            campuspk INTEGER, 
            firstname VARCHAR(255),
            lastname VARCHAR(255),
            gpa REAL,
            studentid VARCHAR(50),            
            FOREIGN KEY(campuspk) REFERENCES campus(campuspk)
        );
        """
        cur.execute(SQL)

        


if __name__ == "__main__":
    create_db(DBFILENAME)