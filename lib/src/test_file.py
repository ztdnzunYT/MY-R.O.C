
import flet as ft
import random
import time
from Test_simgame import Game_sim , start_sim
from Player_team_initializer import My_team_query , my_team_player1 , my_team_player2 , my_team_player3

def main(page: ft.Page):

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_min_width = 500
    page.window_min_height = 400
    
    

    

    class Sim_game: 
    
        
        class Player_init(ft.Container):
           
            def __init__(self,bgcolor,info):
                super().__init__()
                self.player_size = 40
                self.player_speed = 500
                self.width = self.player_size
                self.height = self.player_size
                self.bgcolor = bgcolor
                self.info = info
                self.shape = ft.BoxShape.CIRCLE
                self.alignment = ft.alignment.center
                self.content = ft.Text(value=self.info.position,text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.W_500,color=ft.colors.WHITE)
                self.animate_position = self.player_speed


        x = Player_init(ft.colors.RED,my_team_player1)
        y = Player_init(ft.colors.BLUE,my_team_player2)
        z = Player_init(ft.colors.ORANGE_600,my_team_player3)

        players = [x,y,z]

        court_pic = ft.Image( src="lib\\assets\\images\\basketball-half-court-parquet-600nw-122537710.png",width=380,height=380,scale=.9,fit=ft.ImageFit.COVER,
                            repeat=ft.ImageRepeat.NO_REPEAT,border_radius=ft.border_radius.all(5))
        
        on_court_items = ft.Stack([x,y,z],height=300,expand=True)

        court = ft.Stack([
            ft.Container(
                    width=court_pic.width,
                    height=court_pic.height,
                    content=(
                        ft.Stack([
                            court_pic,
                            ft.Column([
                                ft.Row([
                                    on_court_items
                                ],
                                vertical_alignment=ft.alignment.center,alignment=ft.MainAxisAlignment.CENTER)
                            ],alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.alignment.center),
                        ])
                    )
                )
            ],expand=True)   
        
        play_animation = {
        "checked in the ball" : [[105,105],[250,250]],  #lessen the horizontal max
        
        } 

        """
        "dribbled the ball" : [test.Player_init.court_horizontal_min_max,test.Player_init.court_vertical_min_max],
        "passed the ball to" : [test.Player_init.court_horizontal_min_max,test.Player_init.court_vertical_min_max],
        "went up for a layup" : [test.Player_init.court_horizontal_min_max,test.Player_init.court_vertical_min_max],
        "went up for a dunk" : [test.Player_init.court_horizontal_min_max,test.Player_init.court_vertical_min_max],
        "pulled up for a mid-range shot" : [test.Player_init.court_horizontal_min_max,test.Player_init.court_vertical_min_max],
        "pulled up for a three-point shot" : [test.Player_init.court_horizontal_min_max,test.Player_init.court_vertical_min_max],
        "grabbed the rebound" : [test.Player_init.court_horizontal_min_max,test.Player_init.court_vertical_min_max],
        "missed the rebound" : [test.Player_init.court_horizontal_min_max,test.Player_init.court_vertical_min_max],
        """
       
        court_horizontal_min_max = [60,280]
        court_vertical_min_max = [15,200] 

        print(court_vertical_min_max[0])

        def animate_play(i):
            for play in Sim_game.play_animation:
                    if play in Game_sim.play_log[i]:
                        for name in range(len(Sim_game.players)):
                            if str((Sim_game.players[name]).info.first_name) and str((Sim_game.players[name]).info.last_name) in Game_sim.play_log[i]:
                                Sim_game.players[name].bottom = random.randint(Sim_game.play_animation[play][0][0],Sim_game.play_animation[play][0][1])   #change from numbers to min and max | max(play_animation[i][0])
                                Sim_game.players[name].left = random.randint(Sim_game.play_animation[play][1][0],Sim_game.play_animation[play][1][1])
                                page.update()
                                time.sleep(2)
                                Sim_game.players[name].bottom =  random.randint(Sim_game.court_vertical_min_max[0],Sim_game.court_horizontal_min_max[1])
                                Sim_game.players[name].left = random.randint(Sim_game.court_horizontal_min_max[0],Sim_game.court_horizontal_min_max[1])
                                print(str((Sim_game.players[name]).info.first_name),str((Sim_game.players[name]).info.last_name),"Cleared the ball")
                                page.update()
                                time.sleep(2)
                            else:
                                print("Searching...")



        def run_play(e):
            
            #court_player_1.bottom = random.randint(min(court_vertical_min_max),max(court_vertical_min_max))
            #court_player_1.left = random.randint(min(court_horizontal_min_max),max(court_horizontal_min_max))


            print((Sim_game.players[0]).info.first_name,Sim_game.players[0].info.last_name)
            for i in range(len(Game_sim.play_log)):
                Sim_game.animate_play(i)

                
                    



                time.sleep(0.03)        
                    
                
            page.update()
            time.sleep(.7) 

        def run_sim(e):
            start_sim()
            print(Game_sim.play_log)

    page.add(
        Sim_game.court,
        ft.ElevatedButton("Animate!", on_click=Sim_game.run_play),
        ft.ElevatedButton("Start Game", on_click=Sim_game.run_sim),

    )



ft.app(target=main)








 


































































