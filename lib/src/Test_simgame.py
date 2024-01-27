from Player_team_initializer import *
from Player_database_connector import *
from simple_colors import*
import time 

'''
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

'''


class Game_pace():
    gamespeed = .01

class Game_difficulty():
    easy = 7
    average = 6
    medium = 5
    hard = 4
    difficulty = medium

def time_delay():
    time.sleep(Game_pace.gamespeed)


class Game_stats():
    score = 0
    layups_made = 0
    layups_missed = 0
    dunks_made = 0
    dunks_missed = 0
    three_points_made = 0  
    three_points_missed = 0
    midrange_shots_made = 0
    midrange_shots_missed = 0 
    rebounds_grabbed = 0 
    rebounds_missed = 0 
    steals = 0
    blocks = 0
    turnovers = 0

    ai_score = 0
    ai_layups_made = 0
    ai_layups_missed = 0
    ai_dunks_made = 0
    ai_dunks_missed = 0
    ai_three_points_made = 0  
    ai_three_points_missed = 0
    ai_midrange_shots_made = 0
    ai_midrange_shots_missed = 0 
    ai_rebounds_grabbed = 0 
    ai_rebounds_missed = 0 
    ai_steals = 0
    ai_blocks = 0
    ai_turnovers = 0 

    wining_score = 21
    #MIGHT MAKE A FILE FOR GAME PROPERTIES 


    def my_team_display_score():
        print(yellow(f"MY TEAM SCORE : {Game_stats.score} POINTS"))
        print()

    def ai_display_score():
        print(yellow(f"AI SCORE : {Game_stats.ai_score} POINTS"))
        print()


class Game_sim():
    team_with_ball = random.choice(Teams.all_teams)
    players = (my_team_player1, my_team_player2, my_team_player3)
    ball_holder = my_team_player1
    ball_reciver = None

    ai_players = (ai_team_player1, ai_team_player2 ,ai_team_player3)
    ai_ball_holder = ai_team_player1
    ai_ball_reciver = None

    class Offense():
        
        def check_ball():
            if Game_stats.score >= Game_stats.wining_score:
                Game_sim.gameover()
            Game_sim.ball_holder = my_team_player1
            print(f"{Game_sim.ball_holder.position} {Game_sim.ball_holder.first_name} {Game_sim.ball_holder.last_name} checked in the ball")
            time_delay()
            Game_sim.Offense.pass_ball()
     
        def clear_ball():
            Game_sim.ai_defender_picker()
            print(f"{Game_sim.ball_holder.position} {Game_sim.ball_holder.first_name} {Game_sim.ball_holder.last_name} cleared the ball")
            time_delay()
            Game_sim.Offense.pass_ball()

        def pass_ball():
            Game_sim.ball_reciver = random.choice(Game_sim.players)
            if Game_sim.ball_reciver == Game_sim.ball_holder:
                if Game_sim.ball_holder == my_team_player3:
                    Game_sim.Offense.pass_ball()
                    pass
                else:
                    print(f"{Game_sim.ball_holder.position} {Game_sim.ball_holder.first_name} {Game_sim.ball_holder.last_name} dribbled the ball")
                    time_delay()
                    if random.randint(0,Game_difficulty.difficulty)==0:
                        Game_sim.Ai_defense.steal_ball()
                    Game_sim.Offense.pass_ball()
            else:
                Game_sim.ai_defender_picker()
                print(f"{Game_sim.ball_holder.position} {Game_sim.ball_holder.first_name} {Game_sim.ball_holder.last_name} passed the ball to {Game_sim.ball_reciver.position} {Game_sim.ball_reciver.first_name} {Game_sim.ball_reciver.last_name}")
                time_delay()
                if random.randint(0,Game_difficulty.difficulty)==0:
                    Game_sim.Ai_defense.steal_ball()
                Game_sim.ball_holder = Game_sim.ball_reciver
                Game_sim.plays[random.randrange(0,len(Game_sim.plays))]()
                    
        def take_layup():
            print(f"{Game_sim.ball_holder.position} {Game_sim.ball_holder.first_name} {Game_sim.ball_holder.last_name} went up for a layup")
            time_delay()
            player_layup_percent = random.randint(0,Game_sim.ball_holder.layup)
            interior_defense_percent = random.randint(0,ai_defender.interior_defense)
            if player_layup_percent > interior_defense_percent:
                print(f"{Game_sim.ball_holder.position} {Game_sim.ball_holder.first_name} {Game_sim.ball_holder.last_name} made the layup")
                Game_stats.layups_made +=1 
                Game_stats.score +=1
                Game_stats.my_team_display_score()
                time_delay()
                Game_sim.Offense.check_ball()
            else:
                if random.randint(0,Game_difficulty.difficulty) == 0:
                    Game_sim.Defense.block_ball(player_layup_percent)
                else:
                    print(f"{Game_sim.ball_holder.position} {Game_sim.ball_holder.first_name} {Game_sim.ball_holder.last_name} missed the layup")
                    Game_stats.layups_missed +=1 
                    time_delay()
                    Game_sim.Defense.rebound_ball()

        def take_dunk():
            print(f"{Game_sim.ball_holder.position} {Game_sim.ball_holder.first_name} {Game_sim.ball_holder.last_name} went up for a dunk")
            time_delay()
            player_dunk_percent = random.randint(0,Game_sim.ball_holder.dunk)
            interior_defense_percent = random.randint(0,ai_defender.interior_defense)
            if player_dunk_percent > interior_defense_percent:
                print(f"{Game_sim.ball_holder.position} {Game_sim.ball_holder.first_name} {Game_sim.ball_holder.last_name} dunked the ball")
                Game_stats.dunks_made +=1 
                Game_stats.score +=1
                Game_stats.my_team_display_score()
                time_delay()
                Game_sim.Offense.check_ball()
            else:
                if random.randint(0,Game_difficulty.difficulty) == 0:
                    Game_sim.Defense.block_ball(player_dunk_percent)
                else:
                    print(f"{Game_sim.ball_holder.position} {Game_sim.ball_holder.first_name} {Game_sim.ball_holder.last_name} missed the dunk")
                    Game_stats.dunks_missed +=1 
                    time_delay()
                    Game_sim.Defense.rebound_ball()

        def take_three_point_shot():
            print(f"{Game_sim.ball_holder.position} {Game_sim.ball_holder.first_name} {Game_sim.ball_holder.last_name} pulled up for a three-point shot")
            time_delay()
            player_three_percent = random.randint(0,Game_sim.ball_holder.three_pointer)
            perimeter_defender_percent = random.randint(0,ai_defender.perimeter_defense)
            if player_three_percent > perimeter_defender_percent: #MADE 3 POINTER
                print(f"{Game_sim.ball_holder.position} {Game_sim.ball_holder.first_name} {Game_sim.ball_holder.last_name} scored the three-pointer")
                Game_stats.three_points_made +=1 
                Game_stats.score +=2
                Game_stats.my_team_display_score()
                time_delay()
                Game_sim.Offense.check_ball()
            else:
                if random.randint(0,Game_difficulty.difficulty) == 0:
                    Game_sim.Defense.block_ball(player_three_percent)
                else:
                    print(f"{Game_sim.ball_holder.position} {Game_sim.ball_holder.first_name} {Game_sim.ball_holder.last_name} missed the three-point shot")
                    Game_stats.three_points_missed +=1 
                    time_delay()
                    Game_sim.Defense.rebound_ball()
            
        def take_midrange_shot():
            print(f"{Game_sim.ball_holder.position} {Game_sim.ball_holder.first_name} {Game_sim.ball_holder.last_name} pulled up for a mid-range shot")
            time_delay()
            player_midrange_percent = random.randint(0,Game_sim.ball_holder.midrange)
            perimeter_defender_percent = random.randint(0,ai_defender.perimeter_defense)
            if player_midrange_percent > perimeter_defender_percent: #MADE 2 POINTER
                print(f"{Game_sim.ball_holder.position} {Game_sim.ball_holder.first_name} {Game_sim.ball_holder.last_name} scored the mid-range shot")
                Game_stats.midrange_shots_made +=1 
                Game_stats.score +=1
                Game_stats.my_team_display_score()
                time_delay()
                Game_sim.Offense.check_ball()
            else:
                if random.randint(0,Game_difficulty.difficulty) == 0:
                    Game_sim.Defense.block_ball(player_midrange_percent)
                else:
                    print(f"{Game_sim.ball_holder.position} {Game_sim.ball_holder.first_name} {Game_sim.ball_holder.last_name} missed the mid-range shot")
                    Game_stats.midrange_shots_missed +=1 
                    time_delay()
                    Game_sim.Defense.rebound_ball()          

        def create_shot():
            pass


    plays = (Offense.pass_ball,Offense.take_layup,Offense.take_dunk,Offense.take_three_point_shot,Offense.take_midrange_shot)
    rebound_plays = (Offense.pass_ball,Offense.take_layup,Offense.take_dunk)
    
    class Defense():
        def steal_ball():
            Game_sim.ai_defender_picker()
            steal_percent = random.randint(0,Game_sim.ball_holder.steal)
            ai_ball_handle = random.randint(0,ai_defender.ball_handle)
            if steal_percent > ai_ball_handle:
                print(f"{Game_sim.ball_holder.position} {Game_sim.ball_holder.first_name} {Game_sim.ball_holder.last_name} stole the ball")
                Game_sim.Ai_defense.turnover_ball()
                Game_stats.steals +=1  
                Game_stats.ai_turnovers +=1
                time_delay()
                Game_sim.Offense.pass_ball()
        
        def block_ball(action):   
            Game_sim.my_team_defender_picker()
            block = random.randint(0,my_team_defender.block)
            if block > action :
                print(f"{my_team_defender.position} {my_team_defender.first_name} {my_team_defender.last_name} blocked the ball")
                Game_stats.blocks +=1 
                Game_stats.ai_turnovers +=1
                Game_sim.Ai_defense.turnover_ball()
                time_delay()
                Game_sim.Offense.pass_ball()


        def rebound_ball():
            rebound_percent = random.randint(0,my_team_player3.rebounding)
            ai_rebound_percent = random.randint(0,ai_team_player3.rebounding)
            if rebound_percent > ai_rebound_percent: 
                Game_sim.ball_holder = my_team_player3
                print(f"{Game_sim.ball_holder.position} {Game_sim.ball_holder.first_name} {Game_sim.ball_holder.last_name} grabbed the rebound")
                Game_stats.rebounds_grabbed +=1 
                time_delay()
                Game_sim.rebound_plays[random.randrange(0,len(Game_sim.rebound_plays))]()
            else:
                print(f"{Game_sim.ball_holder.position} {Game_sim.ball_holder.first_name} {Game_sim.ball_holder.last_name} missed the rebound")
                time_delay()
                Game_stats.rebounds_missed +=1
                print(f"{Game_sim.ai_ball_holder.position} {Game_sim.ai_ball_holder.first_name} {Game_sim.ai_ball_holder.last_name} grabbed the rebound")
                time_delay()
                Game_sim.Defense.turnover_ball()
                Game_sim.Ai_offense.clear_ball()
        
        def turnover_ball():
            print()
            print(black('AI TEAMS BALL',['bold','underlined']))

        def play_inside_defense(): 
            pass
        def play_outside_defense():
            pass 
        def set_screen():
            pass

    def my_team_defender_picker():
            global my_team_defender 
            if Game_sim.ai_ball_holder == ai_team_player1:
                my_team_defender = my_team_player1
            elif Game_sim.ai_ball_holder == ai_team_player2:
                my_team_defender = my_team_player2
            elif Game_sim.ai_ball_holder == ai_team_player3:
                my_team_defender = my_team_player3




    #Ai ------------------------
    


    class Ai_offense():

        def check_ball():
            if Game_stats.ai_score >= Game_stats.wining_score:
                Game_sim.gameover()
            Game_sim.ai_ball_holder = ai_team_player1
            print(f"{Game_sim.ai_ball_holder.position} {Game_sim.ai_ball_holder.first_name} {Game_sim.ai_ball_holder.last_name} checked in the ball")
            time_delay()
            Game_sim.Ai_offense.pass_ball()

        def clear_ball():
            Game_sim.my_team_defender_picker()
            print(f"{Game_sim.ai_ball_holder.position} {Game_sim.ai_ball_holder.first_name} {Game_sim.ai_ball_holder.last_name} cleared the ball")
            time_delay()
            Game_sim.Ai_offense.pass_ball()
            #change to random ai)playy

        def pass_ball():
            Game_sim.ai_ball_reciver = random.choice(Game_sim.ai_players)
            if Game_sim.ai_ball_reciver == Game_sim.ai_ball_holder:
                if Game_sim.ai_ball_holder == ai_team_player3:
                    Game_sim.Ai_offense.pass_ball()
                    pass
                else:
                    print(f"{Game_sim.ai_ball_holder.position} {Game_sim.ai_ball_holder.first_name} {Game_sim.ai_ball_holder.last_name} dribbled the ball")
                    time_delay()
                if random.randint(0,Game_difficulty.difficulty)==0:
                    Game_sim.Defense.steal_ball()
                Game_sim.Ai_offense.pass_ball()
            else:
                Game_sim.my_team_defender_picker()
                if random.randint(0,Game_difficulty.difficulty)==0:
                    Game_sim.Defense.steal_ball()
                print(f"{Game_sim.ai_ball_holder.position} {Game_sim.ai_ball_holder.first_name} {Game_sim.ai_ball_holder.last_name} passed the ball to {Game_sim.ai_ball_reciver.position} {Game_sim.ai_ball_reciver.first_name} {Game_sim.ai_ball_reciver.last_name}")
                Game_sim.ai_ball_holder = Game_sim.ai_ball_reciver
                time_delay()
                Game_sim.ai_plays[random.randrange(0,len(Game_sim.plays))]()

        def take_layup():
            print(f"{Game_sim.ai_ball_holder.position} {Game_sim.ai_ball_holder.first_name} {Game_sim.ai_ball_holder.last_name} went up for a layup")
            time_delay()
            player_layup_percent = random.randint(0,Game_sim.ai_ball_holder.layup)
            interior_defense_percent = random.randint(0,my_team_defender.interior_defense)
            if player_layup_percent > interior_defense_percent:
                print(f"{Game_sim.ai_ball_holder.position} {Game_sim.ai_ball_holder.first_name} {Game_sim.ai_ball_holder.last_name} made the layup")
                Game_stats.ai_layups_made +=1 
                Game_stats.ai_score +=1 
                Game_stats.ai_display_score()
                time_delay()
                Game_sim.Ai_offense.check_ball()
            else:
                if random.randint(0,Game_difficulty.difficulty) == 0:
                    Game_sim.Ai_defense.block_ball(player_layup_percent)
                else:
                    print(f"{Game_sim.ai_ball_holder.position} {Game_sim.ai_ball_holder.first_name} {Game_sim.ai_ball_holder.last_name} missed the layup")
                    Game_stats.ai_layups_missed +=1 
                    time_delay()       
                    Game_sim.Ai_defense.rebound_ball()

        def take_dunk():
            print(f"{Game_sim.ai_ball_holder.position} {Game_sim.ai_ball_holder.first_name} {Game_sim.ai_ball_holder.last_name} went up for a dunk")
            time_delay()
            player_dunk_percent = random.randint(0,Game_sim.ai_ball_holder.dunk)
            interior_defense_percent = random.randint(0,my_team_defender.interior_defense)
            if player_dunk_percent > interior_defense_percent:
                print(f"{Game_sim.ai_ball_holder.position} {Game_sim.ai_ball_holder.first_name} {Game_sim.ai_ball_holder.last_name} dunked the ball")
                Game_stats.ai_dunks_made +=1 
                Game_stats.ai_score +=1
                Game_stats.ai_display_score()
                time_delay()
                Game_sim.Ai_offense.check_ball()
            else:
                if random.randint(0,Game_difficulty.difficulty) == 0:
                    Game_sim.Ai_defense.block_ball(player_dunk_percent)
                else:
                    print(f"{Game_sim.ai_ball_holder.position} {Game_sim.ai_ball_holder.first_name} {Game_sim.ai_ball_holder.last_name} missed the dunk")
                    Game_stats.ai_dunks_missed +=1 
                    time_delay()
                    Game_sim.Ai_defense.rebound_ball()
                
        def take_three_point_shot():
            print(f"{Game_sim.ai_ball_holder.position} {Game_sim.ai_ball_holder.first_name} {Game_sim.ai_ball_holder.last_name} pulled up for a three-point shot")
            time_delay()
            player_three_percent = random.randint(0,Game_sim.ai_ball_holder.three_pointer)
            perimeter_defender_percent = random.randint(0,my_team_defender.perimeter_defense)
            if player_three_percent > perimeter_defender_percent: #MADE 3 POINTER
                print(f"{Game_sim.ai_ball_holder.position} {Game_sim.ai_ball_holder.first_name} {Game_sim.ai_ball_holder.last_name} scored the three-pointer")
                Game_stats.ai_three_points_made +=1 
                Game_stats.ai_score +=2
                Game_stats.ai_display_score()
                time_delay()
                Game_sim.Ai_offense.check_ball()
            else:
                if random.randint(0,Game_difficulty.difficulty) == 0:
                    Game_sim.Ai_defense.block_ball(player_three_percent)
                else:
                    print(f"{Game_sim.ai_ball_holder.position} {Game_sim.ai_ball_holder.first_name} {Game_sim.ai_ball_holder.last_name} missed the three-point shot")
                    Game_stats.ai_three_points_missed +=1
                    time_delay()     
                    Game_sim.Ai_defense.rebound_ball()
            
    
        def take_midrange_shot():
            print(f"{Game_sim.ai_ball_holder.position} {Game_sim.ai_ball_holder.first_name} {Game_sim.ai_ball_holder.last_name} pulled up for a mid-range shot")
            time_delay()
            player_midrange_percent = random.randint(0,Game_sim.ai_ball_holder.midrange)
            perimeter_defender_percent = random.randint(0,my_team_defender.perimeter_defense)
            if player_midrange_percent > perimeter_defender_percent: #MADE 2 POINTER
                print(f"{Game_sim.ai_ball_holder.position} {Game_sim.ai_ball_holder.first_name} {Game_sim.ai_ball_holder.last_name} scored the mid-range shot")
                Game_stats.ai_midrange_shots_made +=1 
                Game_stats.ai_score +=1
                Game_stats.ai_display_score()
                time_delay()
                Game_sim.Ai_offense.check_ball()
            else:
                if random.randint(0,Game_difficulty.difficulty) == 0:
                    Game_sim.Ai_defense.block_ball(player_midrange_percent)
                else:
                    print(f"{Game_sim.ai_ball_holder.position} {Game_sim.ai_ball_holder.first_name} {Game_sim.ai_ball_holder.last_name} missed the mid-range shot")
                    Game_stats.ai_midrange_shots_missed +=1 
                    time_delay()
                    Game_sim.Ai_defense.rebound_ball()        

        def create_shot():
            print
            pass


    ai_plays = (Ai_offense.pass_ball,Ai_offense.take_layup,Ai_offense.take_dunk,Ai_offense.take_three_point_shot,Ai_offense.take_midrange_shot)
    ai_rebound_plays = (Ai_offense.pass_ball,Ai_offense.take_layup,Ai_offense.take_dunk)
    
    class Ai_defense():

        def steal_ball():
            Game_sim.my_team_defender_picker()
            ai_steal_percent = random.randint(0,Game_sim.ai_ball_holder.steal)
            ball_handle = random.randint(0,Game_sim.ball_holder.ball_handle)
            if ai_steal_percent > ball_handle:
                print(f"{Game_sim.ai_ball_holder.position} {Game_sim.ai_ball_holder.first_name} {Game_sim.ai_ball_holder.last_name} stole the ball")
                Game_sim.Defense.turnover_ball()
                Game_stats.ai_steals +=1 
                Game_stats.turnovers +=1
                time_delay()
                Game_sim.Ai_offense.pass_ball()

        def block_ball(action):   
            Game_sim.ai_defender_picker()
            block = random.randint(0,ai_defender.block)
            if block > action :
                print(f"{ai_defender.position} {ai_defender.first_name} {ai_defender.last_name} blocked the ball")
                Game_stats.ai_blocks +=1 
                Game_stats.turnovers +=1 
                Game_sim.Defense.turnover_ball()
                time_delay()
                Game_sim.Ai_offense.pass_ball()

        def rebound_ball():
            ai_rebound_percent = random.randint(0,ai_team_player3.rebounding)
            rebound_percent = random.randint(0,my_team_player3.rebounding)
            if ai_rebound_percent > rebound_percent: 
                Game_sim.ai_ball_holder = ai_team_player3
                print(f"{Game_sim.ai_ball_holder.position} {Game_sim.ai_ball_holder.first_name} {Game_sim.ai_ball_holder.last_name} grabbed the rebound")
                time_delay()
                Game_stats.ai_rebounds_grabbed +=1 
                Game_sim.ai_rebound_plays[random.randrange(0,len(Game_sim.ai_rebound_plays))]()
            
            else:
                print(f"{Game_sim.ai_ball_holder.position} {Game_sim.ai_ball_holder.first_name} {Game_sim.ai_ball_holder.last_name} missed the rebound")
                Game_stats.ai_rebounds_missed +=1
                print(f"{Game_sim.ball_holder.position} {Game_sim.ball_holder.first_name} {Game_sim.ball_holder.last_name} grabbed the rebound")
                Game_sim.Ai_defense.turnover_ball()
                Game_sim.Offense.clear_ball()
        
        def turnover_ball():
            print()
            print(black('MY TEAMS BALL',['bold','underlined']))

        def play_inside_defense():
            pass
        def play_outside_defense():
            pass 
        def set_screen(): 
            pass

    def ai_defender_picker():
            global ai_defender
            if Game_sim.ball_holder == my_team_player1:
                ai_defender = ai_team_player1
            elif Game_sim.ball_holder == my_team_player2:
                ai_defender = ai_team_player2
            elif Game_sim.ball_holder == my_team_player3:
                ai_defender = ai_team_player3
            #print(f"{defender.position} {defender.first_name} {defender.last_name} is the defender ")
        
    
    def gameover():
        if Game_stats.score >= Game_stats.wining_score:
            print(yellow(f"MY TEAM WON! {Game_stats.score}|{Game_stats.ai_score}"))
            print(yellow("-----------------"))
            quit()
        elif Game_stats.ai_score >= Game_stats.wining_score:
            print(yellow(f"AI TEAM WON! {Game_stats.ai_score}|{Game_stats.score}"))
            print(yellow("-----------------"))
            quit()
        else:
            pass

print()
print(f"AI TEAM : {random_ai_team} STAR RATING")
print("-------------")


def ball_first():
    print(yellow(f"{Game_sim.team_with_ball} : GETS BALL FIRST "))
    print()
ball_first()

time_delay()
if Game_sim.team_with_ball == Teams.my_team:
    Game_sim.Offense.check_ball()
elif Game_sim.team_with_ball == Teams.ai_team:
    Game_sim.Ai_offense.check_ball()
else:
    print("No team selected")












#Game_sim.play[random.randint(0,len(Game_sim.play)-1)]()




'''
print("--------")
print(Game_sim.Game_stats.Score)
print(Game_sim.Game_stats.layups_made)
print(Game_sim.Game_stats.layups_missed)
print(Game_sim.Game_stats.three_points_made)
print(Game_sim.Game_stats.three_points_missed)
print(Game_sim.Game_stats.rebounds_grabbed)
print(Game_sim.Game_stats.rebounds_missed)


'''








        














