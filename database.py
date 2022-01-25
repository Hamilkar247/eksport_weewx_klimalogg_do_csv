import sqlite3 
from sqlite3 import Error
from datetime import date

def create_connection(db_file):
    """ stwórz połączenie z bazą danych sqlite """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    # finally:
        # if conn:
        #     conn.close()
    return conn



def select_all_archive(conn):
    """
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM archive")
    
    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_part_of_archive(conn):
    """
    """
    cur = conn.cursor()
    cur.execute("SELECT datetime FROM archive") #, (priority,))


    rows = cur.fetchall()

    #string DateFormat = "hh mm ss"
    for row in rows:
        print(row)


if __name__ == '__main__':
    conn=create_connection("weewx-kl.sqlite")
   
    with conn:
        #print("1. Query archive by priority")
        select_part_of_archive(conn)       
        #print("2. Query all tasks")
        select_all_archive(conn)

        

 