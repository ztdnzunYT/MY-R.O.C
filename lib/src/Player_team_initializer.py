import sqlite3
import random
from Player_database_connector import*


#mycursor.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='test_user'")
#UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='table_name';

class My_team_query:
    mycursor.execute("SELECT * FROM my_team")
    my_team = mycursor.fetchall()

class Ai_team_picker:
    def pick_random_ai_team():
        global random_ai_team
        #random_ai_team = random.randint(1,10)
        #print(f"Team {random_ai_team}")    #THIS WILL BE USED TO HAVE RANDOM TEAMS TO GO AGAINST INSTEAD OF JUST ONE TEAM 
        random_ai_team = 5
    pick_random_ai_team()
    
class Ai_team_query:
    mycursor.execute("SELECT * FROM ai_team_"+str(random_ai_team)+"")
    ai_team = mycursor.fetchall()  #List of all the information in the the ai database


class Player_initalizer:
    def __init__(self,id,first_name,last_name,age,height,weight,star_rating,position,build,moral,trait,team_name,skill_set,injured,recovery_days, 
            potential,overall,offense,defense,roots,three_pointer,midrange,layup,dunk,ball_handle,speed,stamina,passing,strength,rebounding,
            interior_defense,perimeter_defense,steal,block,points,assists,rebounds,steals,blocks,turnovers,games_played,points_per_game,
            assists_per_game,steals_per_game,blocks_per_game,rebounds_per_game,turnovers_per_game,field_goal_percentage,three_point_percentage):

        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.weight = weight 
        self.star_rating = star_rating
        self.position = position
        self.build = build
        self.moral = moral
        self.trait = trait
        self.team_name = team_name
        self.skill_set = skill_set
        self.injured = injured
        self.recovery_days = recovery_days
        self.potential = potential
        self.overall = overall
        self.offense = offense
        self.defense = defense
        self.roots = roots 
        self.three_pointer = three_pointer
        self.midrange = midrange
        self.layup = layup
        self.dunk = dunk
        self.ball_handle = ball_handle
        self.speed = speed
        self.stamina = stamina
        self.passing = passing
        self.strength = strength
        self.rebounding = rebounding
        self.interior_defense = interior_defense
        self.perimeter_defense = perimeter_defense
        self.steal = steal 
        self.block = block 
        self.points = points 
        self.assists = assists
        self.rebounds = rebounds
        self.steals = steals 
        self.blocks = blocks
        self.turnovers = turnovers
        self.games_played = games_played
        self.points_per_game = points_per_game
        self.assists_per_game = assists_per_game
        self.steals_per_game = steals_per_game
        self.blocks_per_game = blocks_per_game
        self.rebounds_per_game = rebounds_per_game
        self.turnovers_per_game = turnovers_per_game
        self.field_goal_percentage = field_goal_percentage
        self.three_point_percentage = three_point_percentage



    def showstats(self):
        print(f"{self.first_name} {self.id} {self.three_pointer} {self.defense}") #DELETE THIS LATER



class Teams():

    
    my_team = "MY TEAM"
    ai_team = "AI TEAM " + str(random_ai_team)
    all_teams = (my_team,ai_team)


    class My_team:
        my_team_p1 = Player_initalizer(My_team_query.my_team[0][0],My_team_query.my_team[0][1],My_team_query.my_team[0][2],My_team_query.my_team[0][3],My_team_query.my_team[0][4],My_team_query.my_team[0][5],My_team_query.my_team[0][6],
                                My_team_query.my_team[0][7],My_team_query.my_team[0][8],My_team_query.my_team[0][9],My_team_query.my_team[0][10],My_team_query.my_team[0][11],My_team_query.my_team[0][12],My_team_query.my_team[0][13],
                                My_team_query.my_team[0][14],My_team_query.my_team[0][15],My_team_query.my_team[0][16],My_team_query.my_team[0][17],My_team_query.my_team[0][18],My_team_query.my_team[0][19],My_team_query.my_team[0][20],
                                My_team_query.my_team[0][21],My_team_query.my_team[0][22],My_team_query.my_team[0][23],My_team_query.my_team[0][24],My_team_query.my_team[0][25],My_team_query.my_team[0][26],My_team_query.my_team[0][27],
                                My_team_query.my_team[0][28],My_team_query.my_team[0][29],My_team_query.my_team[0][30],My_team_query.my_team[0][31],My_team_query.my_team[0][32],My_team_query.my_team[0][33],My_team_query.my_team[0][34],
                                My_team_query.my_team[0][35],My_team_query.my_team[0][36],My_team_query.my_team[0][37],My_team_query.my_team[0][38],My_team_query.my_team[0][39],My_team_query.my_team[0][40],My_team_query.my_team[0][41],
                                My_team_query.my_team[0][42],My_team_query.my_team[0][43],My_team_query.my_team[0][44],My_team_query.my_team[0][45],My_team_query.my_team[0][46],My_team_query.my_team[0][47],My_team_query.my_team[0][48])

        my_team_p2 = Player_initalizer(My_team_query.my_team[1][0],My_team_query.my_team[1][1],My_team_query.my_team[1][2],My_team_query.my_team[1][3],My_team_query.my_team[1][4],My_team_query.my_team[1][5],My_team_query.my_team[1][6],
                                My_team_query.my_team[1][7],My_team_query.my_team[1][8],My_team_query.my_team[1][9],My_team_query.my_team[1][10],My_team_query.my_team[1][11],My_team_query.my_team[1][12],My_team_query.my_team[1][13],
                                My_team_query.my_team[1][14],My_team_query.my_team[1][15],My_team_query.my_team[1][16],My_team_query.my_team[1][17],My_team_query.my_team[1][18],My_team_query.my_team[1][19],My_team_query.my_team[1][20],
                                My_team_query.my_team[1][21],My_team_query.my_team[1][22],My_team_query.my_team[1][23],My_team_query.my_team[1][24],My_team_query.my_team[1][25],My_team_query.my_team[1][26],My_team_query.my_team[1][27],
                                My_team_query.my_team[1][28],My_team_query.my_team[1][29],My_team_query.my_team[1][30],My_team_query.my_team[1][31],My_team_query.my_team[1][32],My_team_query.my_team[1][33],My_team_query.my_team[1][34],
                                My_team_query.my_team[1][35],My_team_query.my_team[1][36],My_team_query.my_team[1][37],My_team_query.my_team[1][38],My_team_query.my_team[1][39],My_team_query.my_team[1][40],My_team_query.my_team[1][41],
                                My_team_query.my_team[1][42],My_team_query.my_team[1][43],My_team_query.my_team[1][44],My_team_query.my_team[1][45],My_team_query.my_team[1][46],My_team_query.my_team[1][47],My_team_query.my_team[0][48])

        my_team_p3 = Player_initalizer(My_team_query.my_team[2][0],My_team_query.my_team[2][1],My_team_query.my_team[2][2],My_team_query.my_team[2][3],My_team_query.my_team[2][4],My_team_query.my_team[2][5],My_team_query.my_team[2][6],
                                My_team_query.my_team[2][7],My_team_query.my_team[2][8],My_team_query.my_team[2][9],My_team_query.my_team[2][10],My_team_query.my_team[2][11],My_team_query.my_team[2][12],My_team_query.my_team[2][13],
                                My_team_query.my_team[2][14],My_team_query.my_team[2][15],My_team_query.my_team[2][16],My_team_query.my_team[2][17],My_team_query.my_team[2][18],My_team_query.my_team[2][19],My_team_query.my_team[2][20],
                                My_team_query.my_team[2][21],My_team_query.my_team[2][22],My_team_query.my_team[2][23],My_team_query.my_team[2][24],My_team_query.my_team[2][25],My_team_query.my_team[2][26],My_team_query.my_team[2][27],
                                My_team_query.my_team[2][28],My_team_query.my_team[2][29],My_team_query.my_team[2][30],My_team_query.my_team[2][31],My_team_query.my_team[2][32],My_team_query.my_team[2][33],My_team_query.my_team[2][34],
                                My_team_query.my_team[2][35],My_team_query.my_team[2][36],My_team_query.my_team[2][37],My_team_query.my_team[2][38],My_team_query.my_team[2][39],My_team_query.my_team[2][40],My_team_query.my_team[2][41],
                                My_team_query.my_team[2][42],My_team_query.my_team[2][43],My_team_query.my_team[2][44],My_team_query.my_team[2][45],My_team_query.my_team[2][46],My_team_query.my_team[2][47],My_team_query.my_team[0][48])
        

    class Ai_team():
        ai_team_p1 = Player_initalizer(Ai_team_query.ai_team[0][0],Ai_team_query.ai_team[0][1],Ai_team_query.ai_team[0][2],Ai_team_query.ai_team[0][3],Ai_team_query.ai_team[0][4],Ai_team_query.ai_team[0][5],Ai_team_query.ai_team[0][6],
                                Ai_team_query.ai_team[0][7],Ai_team_query.ai_team[0][8],Ai_team_query.ai_team[0][9],Ai_team_query.ai_team[0][10],Ai_team_query.ai_team[0][11],Ai_team_query.ai_team[0][12],Ai_team_query.ai_team[0][13],
                                Ai_team_query.ai_team[0][14],Ai_team_query.ai_team[0][15],Ai_team_query.ai_team[0][16],Ai_team_query.ai_team[0][17],Ai_team_query.ai_team[0][18],Ai_team_query.ai_team[0][19],Ai_team_query.ai_team[0][20],
                                Ai_team_query.ai_team[0][21],Ai_team_query.ai_team[0][22],Ai_team_query.ai_team[0][23],Ai_team_query.ai_team[0][24],Ai_team_query.ai_team[0][25],Ai_team_query.ai_team[0][26],Ai_team_query.ai_team[0][27],
                                Ai_team_query.ai_team[0][28],Ai_team_query.ai_team[0][29],Ai_team_query.ai_team[0][30],Ai_team_query.ai_team[0][31],Ai_team_query.ai_team[0][32],Ai_team_query.ai_team[0][33],Ai_team_query.ai_team[0][34],
                                Ai_team_query.ai_team[0][35],Ai_team_query.ai_team[0][36],Ai_team_query.ai_team[0][37],Ai_team_query.ai_team[0][38],Ai_team_query.ai_team[0][39],Ai_team_query.ai_team[0][40],Ai_team_query.ai_team[0][41],
                                Ai_team_query.ai_team[0][42],Ai_team_query.ai_team[0][43],Ai_team_query.ai_team[0][44],Ai_team_query.ai_team[0][45],Ai_team_query.ai_team[0][46],Ai_team_query.ai_team[0][47],Ai_team_query.ai_team[0][48])
        

        ai_team_p2 = Player_initalizer(Ai_team_query.ai_team[1][0],Ai_team_query.ai_team[1][1],Ai_team_query.ai_team[1][2],Ai_team_query.ai_team[1][3],Ai_team_query.ai_team[1][4],Ai_team_query.ai_team[1][5],Ai_team_query.ai_team[1][6],
                                Ai_team_query.ai_team[1][7],Ai_team_query.ai_team[1][8],Ai_team_query.ai_team[1][9],Ai_team_query.ai_team[1][10],Ai_team_query.ai_team[1][11],Ai_team_query.ai_team[1][12],Ai_team_query.ai_team[1][13],
                                Ai_team_query.ai_team[1][14],Ai_team_query.ai_team[1][15],Ai_team_query.ai_team[1][16],Ai_team_query.ai_team[1][17],Ai_team_query.ai_team[1][18],Ai_team_query.ai_team[1][19],Ai_team_query.ai_team[1][20],
                                Ai_team_query.ai_team[1][21],Ai_team_query.ai_team[1][22],Ai_team_query.ai_team[1][23],Ai_team_query.ai_team[1][24],Ai_team_query.ai_team[1][25],Ai_team_query.ai_team[1][26],Ai_team_query.ai_team[1][27],
                                Ai_team_query.ai_team[1][28],Ai_team_query.ai_team[1][29],Ai_team_query.ai_team[1][30],Ai_team_query.ai_team[1][31],Ai_team_query.ai_team[1][32],Ai_team_query.ai_team[1][33],Ai_team_query.ai_team[1][34],
                                Ai_team_query.ai_team[1][35],Ai_team_query.ai_team[1][36],Ai_team_query.ai_team[1][37],Ai_team_query.ai_team[1][38],Ai_team_query.ai_team[1][39],Ai_team_query.ai_team[1][40],Ai_team_query.ai_team[1][41],
                                Ai_team_query.ai_team[1][42],Ai_team_query.ai_team[1][43],Ai_team_query.ai_team[1][44],Ai_team_query.ai_team[1][45],Ai_team_query.ai_team[1][46],Ai_team_query.ai_team[1][47],Ai_team_query.ai_team[0][47])
        

        ai_team_p3 = Player_initalizer(Ai_team_query.ai_team[2][0],Ai_team_query.ai_team[2][1],Ai_team_query.ai_team[2][2],Ai_team_query.ai_team[2][3],Ai_team_query.ai_team[2][4],Ai_team_query.ai_team[2][5],Ai_team_query.ai_team[2][6],
                                Ai_team_query.ai_team[2][7],Ai_team_query.ai_team[2][8],Ai_team_query.ai_team[2][9],Ai_team_query.ai_team[2][10],Ai_team_query.ai_team[2][11],Ai_team_query.ai_team[2][12],Ai_team_query.ai_team[2][13],
                                Ai_team_query.ai_team[2][14],Ai_team_query.ai_team[2][15],Ai_team_query.ai_team[2][16],Ai_team_query.ai_team[2][17],Ai_team_query.ai_team[2][18],Ai_team_query.ai_team[2][19],Ai_team_query.ai_team[2][20],
                                Ai_team_query.ai_team[2][21],Ai_team_query.ai_team[2][22],Ai_team_query.ai_team[2][23],Ai_team_query.ai_team[2][24],Ai_team_query.ai_team[2][25],Ai_team_query.ai_team[2][26],Ai_team_query.ai_team[2][27],
                                Ai_team_query.ai_team[2][28],Ai_team_query.ai_team[2][29],Ai_team_query.ai_team[2][30],Ai_team_query.ai_team[2][31],Ai_team_query.ai_team[2][32],Ai_team_query.ai_team[2][33],Ai_team_query.ai_team[2][34],
                                Ai_team_query.ai_team[2][35],Ai_team_query.ai_team[2][36],Ai_team_query.ai_team[2][37],Ai_team_query.ai_team[2][38],Ai_team_query.ai_team[2][39],Ai_team_query.ai_team[2][40],Ai_team_query.ai_team[2][41],
                                Ai_team_query.ai_team[2][42],Ai_team_query.ai_team[2][43],Ai_team_query.ai_team[2][44],Ai_team_query.ai_team[2][45],Ai_team_query.ai_team[2][46],Ai_team_query.ai_team[2][47],Ai_team_query.ai_team[0][48])



my_team_player1 = Teams.My_team.my_team_p1
my_team_player2 = Teams.My_team.my_team_p2
my_team_player3 = Teams.My_team.my_team_p3

ai_team_player1 = Teams.Ai_team.ai_team_p1
ai_team_player2 = Teams.Ai_team.ai_team_p2 
ai_team_player3 = Teams.Ai_team.ai_team_p3





'''
self,id,first_name,last_name,age,height,weight,star_rating,position,build,moral,trait,skill_set,injured,recovery_days, 
            potential,overall,offense,defense,roots,three_pointer,midrange,layup,dunk,ball_handle,speed,stamina,passing,strength,rebounding,
            interior_defense,perimeter_defense,steal,block,points,assists,rebounds,steals,blocks,turnovers,games_played,points_per_game,
            assists_per_game,steals_per_game,blocks_per_game,rebounds_per_game,turnovers_per_game,field_goal_percentage,three_point_percentage):
'''


try:
    conn.commit()
    print("executed")
except:
    print("Already executed")











