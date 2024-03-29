import sqlite3

#This file connects other files to the players database without having to add the following variables
#windows C:\\My R.O.C Manager\\lib\\db\\Players.db
conn = sqlite3.connect("lib/db/Players.db",check_same_thread=False)
mycursor = conn.cursor()


def commit_database():
    try:
        conn.commit()
        conn.close()
        print("Executed")
    except:
        conn.close()
        print("Error Executing")
        

#test this 
def open_connection():
    conn = sqlite3.connect("C:\\My R.O.C Manager\\lib\\db\\Players.db")
    mycursor = conn.cursor()





