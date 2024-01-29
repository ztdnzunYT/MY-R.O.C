import random
import Player_properties as pprops
from Player_properties import pv
from simple_colors import* 
from Player_database_connector import* 

#THIS FILE IS USED TO CREATE ALL THE DATABASES ON START UP

class Player_hub_table_creator():
    def create_player_hub_table():
        mycursor.execute("""CREATE TABLE player_hub (
        player_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        age INTEGER NOT NULL,
        height REAL NOT NULL, 
        weight REAL NOT NULL,
        star_rating INTEGER NOT NULL,
        position TEXT NOT NULL,
        build TEXT NOT NULL, 
        moral TEXT NULL,
        trait TEXT NULL,
        team_name TEXT NULL, 
        skill_set TEXT NOT NULL, 
        injured TEXT NOT NULL,
        recovery_days INTEGER NOT NULL, 
        potential INTEGER NOT NULL, 
        overall INTEGER NOT NULL,
        offense INTEGER NOT NULL,
        defense INTEGER NOT NULL,
        roots TEXT NULL,
        three_pointer INTEGER NOT NULL,
        midrange INTEGER NOT NULL,
        layup INTEGER NOT NULL, 
        dunk INTEGER NOT NULL,
        ball_handle INTEGER NOT NULL, 
        speed INTEGER NOT NULL,
        stamina INTEGER NOT NULL,
        passing INTEGER NOT NULL, 
        strength INTEGER NOT NULL,
        rebounding INTEGER NOT NULL,
        interior_defense INTEGER NOT NULL,
        perimeter_defense INTEGER NOT NULL,
        steal INTEGER NOT NULL,
        block INTEGER NOT NULL,
        points INTEGER NULL,
        assists INTEGER NULL, 
        rebounds INTEGER NULL, 
        steals INTEGER NULL, 
        blocks INTEGER NULL, 
        turnovers INTEGER NULL,
        games_played INTEGER NULL, 
        points_per_game REAL NULL,
        assists_per_game REAL NULL,
        steals_per_game REAL NULL, 
        blocks_per_game REAL NULL, 
        rebounds_per_game REAL NULL, 
        turnovers_per_game REAL NULL,
        field_goal_percentage REAL NULL,
        three_point_percentage REAL NULL
        )""")

class Myteam_table_creator():
    def my_team_table_creator():
         mycursor.execute("""CREATE TABLE my_team(
        player_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        age INTEGER NOT NULL,
        height REAL NOT NULL, 
        weight REAL NOT NULL,
        star_rating INTEGER NOT NULL,
        position TEXT NOT NULL,
        build TEXT NOT NULL, 
        moral TEXT NULL,
        trait TEXT NULL,
        team_name TEXT NULL, 
        skill_set TEXT NOT NULL, 
        injured TEXT NOT NULL,
        recovery_days INTEGER NOT NULL, 
        potential INTEGER NOT NULL, 
        overall INTEGER NOT NULL,
        offense INTEGER NOT NULL,
        defense INTEGER NOT NULL,
        roots TEXT NULL,
        three_pointer INTEGER NOT NULL,
        midrange INTEGER NOT NULL,
        layup INTEGER NOT NULL, 
        dunk INTEGER NOT NULL,
        ball_handle INTEGER NOT NULL, 
        speed INTEGER NOT NULL,
        stamina INTEGER NOT NULL,
        passing INTEGER NOT NULL, 
        strength INTEGER NOT NULL,
        rebounding INTEGER NOT NULL,
        interior_defense INTEGER NOT NULL,
        perimeter_defense INTEGER NOT NULL,
        steal INTEGER NOT NULL,
        block INTEGER NOT NULL,
        points INTEGER NULL,
        assists INTEGER NULL, 
        rebounds INTEGER NULL, 
        steals INTEGER NULL, 
        blocks INTEGER NULL, 
        turnovers INTEGER NULL,
        games_played INTEGER NULL, 
        points_per_game REAL NULL,
        assists_per_game REAL NULL,
        steals_per_game REAL NULL, 
        blocks_per_game REAL NULL, 
        rebounds_per_game REAL NULL, 
        turnovers_per_game REAL NULL,
        field_goal_percentage REAL NULL,
        three_point_percentage REAL NULL
        )""")

class Ai_teams_table_creator():
    def create_ai_team_tables():

        mycursor.execute("""CREATE TABLE ai_team_1(
        player_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        age INTEGER NOT NULL,
        height REAL NOT NULL, 
        weight REAL NOT NULL,
        star_rating INTEGER NOT NULL,
        position TEXT NOT NULL,
        build TEXT NOT NULL, 
        moral TEXT NULL,
        trait TEXT NULL,
        team_name TEXT NULL, 
        skill_set TEXT NOT NULL, 
        injured TEXT NOT NULL,
        recovery_days INTEGER NOT NULL, 
        potential INTEGER NOT NULL, 
        overall INTEGER NOT NULL,
        offense INTEGER NOT NULL,
        defense INTEGER NOT NULL,
        roots TEXT NULL,
        three_pointer INTEGER NOT NULL,
        midrange INTEGER NOT NULL,
        layup INTEGER NOT NULL, 
        dunk INTEGER NOT NULL,
        ball_handle INTEGER NOT NULL, 
        speed INTEGER NOT NULL,
        stamina INTEGER NOT NULL,
        passing INTEGER NOT NULL, 
        strength INTEGER NOT NULL,
        rebounding INTEGER NOT NULL,
        interior_defense INTEGER NOT NULL,
        perimeter_defense INTEGER NOT NULL,
        steal INTEGER NOT NULL,
        block INTEGER NOT NULL,
        points INTEGER NULL,
        assists INTEGER NULL, 
        rebounds INTEGER NULL, 
        steals INTEGER NULL, 
        blocks INTEGER NULL, 
        turnovers INTEGER NULL,
        games_played INTEGER NULL, 
        points_per_game REAL NULL,
        assists_per_game REAL NULL,
        steals_per_game REAL NULL, 
        blocks_per_game REAL NULL, 
        rebounds_per_game REAL NULL, 
        turnovers_per_game REAL NULL,
        field_goal_percentage REAL NULL,
        three_point_percentage REAL NULL
        )""")

        mycursor.execute("""CREATE TABLE ai_team_2(
        player_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        age INTEGER NOT NULL,
        height REAL NOT NULL, 
        weight REAL NOT NULL,
        star_rating INTEGER NOT NULL,
        position TEXT NOT NULL,
        build TEXT NOT NULL, 
        moral TEXT NULL,
        trait TEXT NULL,
        team_name TEXT NULL, 
        skill_set TEXT NOT NULL, 
        injured TEXT NOT NULL,
        recovery_days INTEGER NOT NULL, 
        potential INTEGER NOT NULL, 
        overall INTEGER NOT NULL,
        offense INTEGER NOT NULL,
        defense INTEGER NOT NULL,
        roots TEXT NULL,
        three_pointer INTEGER NOT NULL,
        midrange INTEGER NOT NULL,
        layup INTEGER NOT NULL, 
        dunk INTEGER NOT NULL,
        ball_handle INTEGER NOT NULL, 
        speed INTEGER NOT NULL,
        stamina INTEGER NOT NULL,
        passing INTEGER NOT NULL, 
        strength INTEGER NOT NULL,
        rebounding INTEGER NOT NULL,
        interior_defense INTEGER NOT NULL,
        perimeter_defense INTEGER NOT NULL,
        steal INTEGER NOT NULL,
        block INTEGER NOT NULL,
        points INTEGER NULL,
        assists INTEGER NULL, 
        rebounds INTEGER NULL, 
        steals INTEGER NULL, 
        blocks INTEGER NULL, 
        turnovers INTEGER NULL,
        games_played INTEGER NULL, 
        points_per_game REAL NULL,
        assists_per_game REAL NULL,
        steals_per_game REAL NULL, 
        blocks_per_game REAL NULL, 
        rebounds_per_game REAL NULL, 
        turnovers_per_game REAL NULL,
        field_goal_percentage REAL NULL,
        three_point_percentage REAL NULL
        )""")

        mycursor.execute("""CREATE TABLE ai_team_3(
                         
        player_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        age INTEGER NOT NULL,
        height REAL NOT NULL, 
        weight REAL NOT NULL,
        star_rating INTEGER NOT NULL,
        position TEXT NOT NULL,
        build TEXT NOT NULL, 
        moral TEXT NULL,
        trait TEXT NULL,
        team_name TEXT NULL, 
        skill_set TEXT NOT NULL, 
        injured TEXT NOT NULL,
        recovery_days INTEGER NOT NULL, 
        potential INTEGER NOT NULL, 
        overall INTEGER NOT NULL,
        offense INTEGER NOT NULL,
        defense INTEGER NOT NULL,
        roots TEXT NULL,
        three_pointer INTEGER NOT NULL,
        midrange INTEGER NOT NULL,
        layup INTEGER NOT NULL, 
        dunk INTEGER NOT NULL,
        ball_handle INTEGER NOT NULL, 
        speed INTEGER NOT NULL,
        stamina INTEGER NOT NULL,
        passing INTEGER NOT NULL, 
        strength INTEGER NOT NULL,
        rebounding INTEGER NOT NULL,
        interior_defense INTEGER NOT NULL,
        perimeter_defense INTEGER NOT NULL,
        steal INTEGER NOT NULL,
        block INTEGER NOT NULL,
        points INTEGER NULL,
        assists INTEGER NULL, 
        rebounds INTEGER NULL, 
        steals INTEGER NULL, 
        blocks INTEGER NULL, 
        turnovers INTEGER NULL,
        games_played INTEGER NULL, 
        points_per_game REAL NULL,
        assists_per_game REAL NULL,
        steals_per_game REAL NULL, 
        blocks_per_game REAL NULL, 
        rebounds_per_game REAL NULL, 
        turnovers_per_game REAL NULL,
        field_goal_percentage REAL NULL,
        three_point_percentage REAL NULL
        )""")

        mycursor.execute("""CREATE TABLE ai_team_4(
        player_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,  
        last_name TEXT NOT NULL,
        age INTEGER NOT NULL,
        height REAL NOT NULL, 
        weight REAL NOT NULL,
        star_rating INTEGER NOT NULL,
        position TEXT NOT NULL,
        build TEXT NOT NULL, 
        moral TEXT NULL,
        trait TEXT NULL,
        team_name TEXT NULL, 
        skill_set TEXT NOT NULL, 
        injured TEXT NOT NULL,
        recovery_days INTEGER NOT NULL, 
        potential INTEGER NOT NULL, 
        overall INTEGER NOT NULL,
        offense INTEGER NOT NULL,
        defense INTEGER NOT NULL,
        roots TEXT NULL,
        three_pointer INTEGER NOT NULL,
        midrange INTEGER NOT NULL,
        layup INTEGER NOT NULL, 
        dunk INTEGER NOT NULL,
        ball_handle INTEGER NOT NULL, 
        speed INTEGER NOT NULL,
        stamina INTEGER NOT NULL,
        passing INTEGER NOT NULL, 
        strength INTEGER NOT NULL,
        rebounding INTEGER NOT NULL,
        interior_defense INTEGER NOT NULL,
        perimeter_defense INTEGER NOT NULL,
        steal INTEGER NOT NULL,
        block INTEGER NOT NULL,
        points INTEGER NULL,
        assists INTEGER NULL, 
        rebounds INTEGER NULL, 
        steals INTEGER NULL, 
        blocks INTEGER NULL, 
        turnovers INTEGER NULL,
        games_played INTEGER NULL, 
        points_per_game REAL NULL,
        assists_per_game REAL NULL,
        steals_per_game REAL NULL, 
        blocks_per_game REAL NULL, 
        rebounds_per_game REAL NULL, 
        turnovers_per_game REAL NULL,
        field_goal_percentage REAL NULL,
        three_point_percentage REAL NULL
        )""")

        mycursor.execute("""CREATE TABLE ai_team_5(
        player_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        age INTEGER NOT NULL,
        height REAL NOT NULL, 
        weight REAL NOT NULL,
        star_rating INTEGER NOT NULL,
        position TEXT NOT NULL,
        build TEXT NOT NULL, 
        moral TEXT NULL,
        trait TEXT NULL,
        team_name TEXT NULL, 
        skill_set TEXT NOT NULL, 
        injured TEXT NOT NULL,
        recovery_days INTEGER NOT NULL, 
        potential INTEGER NOT NULL, 
        overall INTEGER NOT NULL,
        offense INTEGER NOT NULL,
        defense INTEGER NOT NULL,
        roots TEXT NULL,
        three_pointer INTEGER NOT NULL,
        midrange INTEGER NOT NULL,
        layup INTEGER NOT NULL, 
        dunk INTEGER NOT NULL,
        ball_handle INTEGER NOT NULL, 
        speed INTEGER NOT NULL,
        stamina INTEGER NOT NULL,
        passing INTEGER NOT NULL, 
        strength INTEGER NOT NULL,
        rebounding INTEGER NOT NULL,
        interior_defense INTEGER NOT NULL,
        perimeter_defense INTEGER NOT NULL,
        steal INTEGER NOT NULL,
        block INTEGER NOT NULL,
        points INTEGER NULL,
        assists INTEGER NULL, 
        rebounds INTEGER NULL, 
        steals INTEGER NULL, 
        blocks INTEGER NULL, 
        turnovers INTEGER NULL,
        games_played INTEGER NULL, 
        points_per_game REAL NULL,
        assists_per_game REAL NULL,
        steals_per_game REAL NULL, 
        blocks_per_game REAL NULL, 
        rebounds_per_game REAL NULL, 
        turnovers_per_game REAL NULL,
        field_goal_percentage REAL NULL,
        three_point_percentage REAL NULL
        )""")

        mycursor.execute("""CREATE TABLE ai_team_6(
        player_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        age INTEGER NOT NULL,
        height REAL NOT NULL, 
        weight REAL NOT NULL,
        star_rating INTEGER NOT NULL,
        position TEXT NOT NULL,
        build TEXT NOT NULL, 
        moral TEXT NULL,
        trait TEXT NULL,
        team_name TEXT NULL, 
        skill_set TEXT NOT NULL, 
        injured TEXT NOT NULL,
        recovery_days INTEGER NOT NULL, 
        potential INTEGER NOT NULL, 
        overall INTEGER NOT NULL,
        offense INTEGER NOT NULL,
        defense INTEGER NOT NULL,
        roots TEXT NULL,
        three_pointer INTEGER NOT NULL,
        midrange INTEGER NOT NULL,
        layup INTEGER NOT NULL, 
        dunk INTEGER NOT NULL,
        ball_handle INTEGER NOT NULL, 
        speed INTEGER NOT NULL,
        stamina INTEGER NOT NULL,
        passing INTEGER NOT NULL, 
        strength INTEGER NOT NULL,
        rebounding INTEGER NOT NULL,
        interior_defense INTEGER NOT NULL,
        perimeter_defense INTEGER NOT NULL,
        steal INTEGER NOT NULL,
        block INTEGER NOT NULL,
        points INTEGER NULL,
        assists INTEGER NULL, 
        rebounds INTEGER NULL, 
        steals INTEGER NULL, 
        blocks INTEGER NULL, 
        turnovers INTEGER NULL,
        games_played INTEGER NULL, 
        points_per_game REAL NULL,
        assists_per_game REAL NULL,
        steals_per_game REAL NULL, 
        blocks_per_game REAL NULL, 
        rebounds_per_game REAL NULL, 
        turnovers_per_game REAL NULL,
        field_goal_percentage REAL NULL,
        three_point_percentage REAL NULL
        )""")

        mycursor.execute("""CREATE TABLE ai_team_7(
        player_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        age INTEGER NOT NULL,
        height REAL NOT NULL, 
        weight REAL NOT NULL,
        star_rating INTEGER NOT NULL,
        position TEXT NOT NULL,
        build TEXT NOT NULL, 
        moral TEXT NULL,
        trait TEXT NULL,
        team_name TEXT NULL, 
        skill_set TEXT NOT NULL, 
        injured TEXT NOT NULL,
        recovery_days INTEGER NOT NULL, 
        potential INTEGER NOT NULL, 
        overall INTEGER NOT NULL,
        offense INTEGER NOT NULL,
        defense INTEGER NOT NULL,
        roots TEXT NULL,
        three_pointer INTEGER NOT NULL,
        midrange INTEGER NOT NULL,
        layup INTEGER NOT NULL, 
        dunk INTEGER NOT NULL,
        ball_handle INTEGER NOT NULL, 
        speed INTEGER NOT NULL,
        stamina INTEGER NOT NULL,
        passing INTEGER NOT NULL, 
        strength INTEGER NOT NULL,
        rebounding INTEGER NOT NULL,
        interior_defense INTEGER NOT NULL,
        perimeter_defense INTEGER NOT NULL,
        steal INTEGER NOT NULL,
        block INTEGER NOT NULL,
        points INTEGER NULL,
        assists INTEGER NULL, 
        rebounds INTEGER NULL, 
        steals INTEGER NULL, 
        blocks INTEGER NULL, 
        turnovers INTEGER NULL,
        games_played INTEGER NULL, 
        points_per_game REAL NULL,
        assists_per_game REAL NULL,
        steals_per_game REAL NULL, 
        blocks_per_game REAL NULL, 
        rebounds_per_game REAL NULL, 
        turnovers_per_game REAL NULL,
        field_goal_percentage REAL NULL,
        three_point_percentage REAL NULL
        )""")

        mycursor.execute("""CREATE TABLE ai_team_8(
        player_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        age INTEGER NOT NULL,
        height REAL NOT NULL, 
        weight REAL NOT NULL,
        star_rating INTEGER NOT NULL,
        position TEXT NOT NULL,
        build TEXT NOT NULL, 
        moral TEXT NULL,
        trait TEXT NULL,
        team_name TEXT NULL, 
        skill_set TEXT NOT NULL, 
        injured TEXT NOT NULL,
        recovery_days INTEGER NOT NULL, 
        potential INTEGER NOT NULL, 
        overall INTEGER NOT NULL,
        offense INTEGER NOT NULL,
        defense INTEGER NOT NULL,
        roots TEXT NULL,
        three_pointer INTEGER NOT NULL,
        midrange INTEGER NOT NULL,
        layup INTEGER NOT NULL, 
        dunk INTEGER NOT NULL,
        ball_handle INTEGER NOT NULL, 
        speed INTEGER NOT NULL,
        stamina INTEGER NOT NULL,
        passing INTEGER NOT NULL, 
        strength INTEGER NOT NULL,
        rebounding INTEGER NOT NULL,
        interior_defense INTEGER NOT NULL,
        perimeter_defense INTEGER NOT NULL,
        steal INTEGER NOT NULL,
        block INTEGER NOT NULL,
        points INTEGER NULL,
        assists INTEGER NULL, 
        rebounds INTEGER NULL, 
        steals INTEGER NULL, 
        blocks INTEGER NULL, 
        turnovers INTEGER NULL,
        games_played INTEGER NULL, 
        points_per_game REAL NULL,
        assists_per_game REAL NULL,
        steals_per_game REAL NULL, 
        blocks_per_game REAL NULL, 
        rebounds_per_game REAL NULL, 
        turnovers_per_game REAL NULL,
        field_goal_percentage REAL NULL,
        three_point_percentage REAL NULL
        )""")

        mycursor.execute("""CREATE TABLE ai_team_9(
        player_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        age INTEGER NOT NULL,
        height REAL NOT NULL, 
        weight REAL NOT NULL,
        star_rating INTEGER NOT NULL,
        position TEXT NOT NULL,
        build TEXT NOT NULL, 
        moral TEXT NULL,
        trait TEXT NULL,
        team_name TEXT NULL, 
        skill_set TEXT NOT NULL, 
        injured TEXT NOT NULL,
        recovery_days INTEGER NOT NULL, 
        potential INTEGER NOT NULL, 
        overall INTEGER NOT NULL,
        offense INTEGER NOT NULL,
        defense INTEGER NOT NULL,
        roots TEXT NULL,
        three_pointer INTEGER NOT NULL,
        midrange INTEGER NOT NULL,
        layup INTEGER NOT NULL, 
        dunk INTEGER NOT NULL,
        ball_handle INTEGER NOT NULL, 
        speed INTEGER NOT NULL,
        stamina INTEGER NOT NULL,
        passing INTEGER NOT NULL, 
        strength INTEGER NOT NULL,
        rebounding INTEGER NOT NULL,
        interior_defense INTEGER NOT NULL,
        perimeter_defense INTEGER NOT NULL,
        steal INTEGER NOT NULL,
        block INTEGER NOT NULL,
        points INTEGER NULL,
        assists INTEGER NULL, 
        rebounds INTEGER NULL, 
        steals INTEGER NULL, 
        blocks INTEGER NULL, 
        turnovers INTEGER NULL,
        games_played INTEGER NULL, 
        points_per_game REAL NULL,
        assists_per_game REAL NULL,
        steals_per_game REAL NULL, 
        blocks_per_game REAL NULL, 
        rebounds_per_game REAL NULL, 
        turnovers_per_game REAL NULL,
        field_goal_percentage REAL NULL,
        three_point_percentage REAL NULL
        )""")
    
        mycursor.execute("""CREATE TABLE ai_team_10(
        player_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        age INTEGER NOT NULL,
        height REAL NOT NULL, 
        weight REAL NOT NULL,
        star_rating INTEGER NOT NULL,
        position TEXT NOT NULL,
        build TEXT NOT NULL, 
        moral TEXT NULL,
        trait TEXT NULL,
        team_name TEXT NULL, 
        skill_set TEXT NOT NULL, 
        injured TEXT NOT NULL,
        recovery_days INTEGER NOT NULL, 
        potential INTEGER NOT NULL, 
        overall INTEGER NOT NULL,
        offense INTEGER NOT NULL,
        defense INTEGER NOT NULL,
        roots TEXT NULL,
        three_pointer INTEGER NOT NULL,
        midrange INTEGER NOT NULL,
        layup INTEGER NOT NULL, 
        dunk INTEGER NOT NULL,
        ball_handle INTEGER NOT NULL, 
        speed INTEGER NOT NULL,
        stamina INTEGER NOT NULL,
        passing INTEGER NOT NULL, 
        strength INTEGER NOT NULL,
        rebounding INTEGER NOT NULL,
        interior_defense INTEGER NOT NULL,
        perimeter_defense INTEGER NOT NULL,
        steal INTEGER NOT NULL,
        block INTEGER NOT NULL,
        points INTEGER NULL,
        assists INTEGER NULL, 
        rebounds INTEGER NULL, 
        steals INTEGER NULL, 
        blocks INTEGER NULL, 
        turnovers INTEGER NULL,
        games_played INTEGER NULL, 
        points_per_game REAL NULL,
        assists_per_game REAL NULL,
        steals_per_game REAL NULL, 
        blocks_per_game REAL NULL, 
        rebounds_per_game REAL NULL, 
        turnovers_per_game REAL NULL,
        field_goal_percentage REAL NULL,
        three_point_percentage REAL NULL
        )""")

  
def create_all_tables():
    Myteam_table_creator.my_team_table_creator()
    Player_hub_table_creator.create_player_hub_table()
    Ai_teams_table_creator.create_ai_team_tables()



    try:
        conn.commit()

        print("Executed")
    except:
    
        print("closed")







































#First player created will have to have an id of 100 inserted for the auto increment to have others start with 100
# UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='table_name';



'''
def input():
    pass
    #mycursor.execute("INSERT INTO players (three,max_midrange,max_dunk,star_rating) VALUES (?,?,?,?)",x)
def clear():
    mycursor.execute("DELETE FROM players")
def Autoincreset():
    mycursor.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='players'")


#mycursor.execute("DROP TABLE players")

def te(x):
    try:
        mycursor.execute(f"INSERT INTO player_stats (player_id,three,max_midrange) VALUES ({x},3,4)")
    except: 
        print("Player stats could not be inserted")

#mycursor.execute("DELETE FROM players WHERE player_id = 1  ")

#mycursor.execute("INSERT INTO players (first_name,last_name) VALUES('jay','burdges')")
#mycursor.execute("DROP TABLE players")  
'''








