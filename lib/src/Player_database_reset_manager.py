import sqlite3
from Player_database_connector import *

#THIS FILE MANAGES DROPPING THE TABLES IN THE DATABASE

class database_manager():

    def reset_player_hub_table():
        mycursor.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='player_hub'")
        mycursor.execute("DROP TABLE player_hub")
        database_manager.commit(database_manager.reset_player_hub_table.__name__)
        
    def reset_ai_team_tables():
        for i in range(10): #Number of ai tables in database
            i+=1
            mycursor.execute("DROP TABLE ai_team_"+str(i)+"")
            database_manager.commit(database_manager.reset_ai_team_tables.__name__)

    def reset_myteam_table():
        mycursor.execute("DROP TABLE my_team")
        database_manager.commit(database_manager.reset_myteam_table.__name__)

    
    def commit(function_name):
        conn.commit()
        print(function_name)

    def reset_all():

        try:
            database_manager.reset_myteam_table()
            database_manager.reset_ai_team_tables()
            database_manager.reset_player_hub_table()
            print("reset database")

        except:
            print("Database info already reset")


   



'''
id = str(1)
mycursor.execute("INSERT INTO test_user_table2 SELECT * FROM test_user_team WHERE id = "+id+"")

#mycursor.execute("INSERT INTO test_user_table2 (id,name,three,defense) VALUES (?,?,?,?)",val)


mycursor.execute("SELECT name FROM sqlite_schema WHERE type='table'")
x = mycursor.fetchall()
print(x)
'''



