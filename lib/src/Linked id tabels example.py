def players(): 
    mycursor.execute("""CREATE TABLE players (
    player_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL, 
    last_name TEXT NOT NULL,
    CONSTRAINT player_ln UNIQUE (last_name) ON CONFLICT FAIL
    )""")

def player_stats():
    mycursor.execute("""CREATE TABLE player_stats (
    player_id INTEGER PRIMARY KEY AUTOINCREMENT,
    three INTEGER NOT NULL,
    midrange INTEGER NOT NULL,
    FOREIGN KEY (player_id) REFERENCES players(player_id)
    ON UPDATE CASCADE
    ON INSERT CASCADE
    ON DELETE CASCADE
    )""")

#mycursor.execute("DROP TABLE players")
#mycursor.execute("PRAGMA foreign_keys = ON")
    
#First player created will have to have an id of 100 inserted for the auto increment to have others start with 100
# UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='table_name';
    
def te(x):
    try:
        mycursor.execute(f"INSERT INTO player_stats (player_id,three,midrange) VALUES ({x},3,4)")
    except: 
        print("Player stats could not be inserted")

#mycursor.execute("DELETE FROM players WHERE player_id = 1  ")

#mycursor.execute("INSERT INTO players (first_name,last_name) VALUES('jay','burdges')")
#mycursor.execute("DROP TABLE players")  

