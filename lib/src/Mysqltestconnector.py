import mysql.connector 

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root5870",
    database="deletedb1"
)

class globals():
    mycursor = conn.cursor()
Glob = globals 

def SHOW():
    global fetch
    fetch = Glob.mycursor.fetchall()

def SELECT():
    Glob.mycursor.execute("SELECT * FROM fullnames")
    SHOW()
    print(fetch)

def INSERT(x,y):
    insert = "INSERT INTO fullnames (first_name,last_name) VALUES (%s,%s)"
    newname = (x,y)
    Glob.mycursor.execute(insert,newname)
    conn.commit()


def DELETE():
    delete = "DELETE FROM fullnames"
    Glob.mycursor.execute(delete)
    conn.commit()






