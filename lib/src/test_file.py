
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
    
    

    court_pic = ft.Image( src="lib\\assets\\images\\basketball-half-court-parquet-600nw-122537710.png",width=380,height=380,scale=.9,fit=ft.ImageFit.COVER,
                            repeat=ft.ImageRepeat.NO_REPEAT,border_radius=ft.border_radius.all(5)  )

    class test: 

        class Player_init(ft.Container):
            player_size = 40  
            player_speed = 500
            court_horizontal_range = [60,280]
            court_vertical_range = [15,200]
            def __init__(self,bgcolor,info):
                    super().__init__()
                    self.width = test.Player_init.player_size
                    self.height = test.Player_init.player_size
                    self.bgcolor = bgcolor
                    self.info = info
                    self.shape = ft.BoxShape.CIRCLE
                    self.alignment = ft.alignment.center
                    self.content = ft.Text(value=self.info.position,text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.W_500,color=ft.colors.WHITE)
                    self.animate_position = test.Player_init.player_speed


    x = test.Player_init(ft.colors.RED,my_team_player1)
    y = test.Player_init(ft.colors.BLUE,my_team_player2)
    z = test.Player_init(ft.colors.ORANGE_600,my_team_player3)

    players = [x,y,z]

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
    "dribbled the ball" : [test.Player_init.court_horizontal_range,test.Player_init.court_vertical_range],
    "passed the ball to" : [test.Player_init.court_horizontal_range,test.Player_init.court_vertical_range],
    "went up for a layup" : [test.Player_init.court_horizontal_range,test.Player_init.court_vertical_range],
    "went up for a dunk" : [test.Player_init.court_horizontal_range,test.Player_init.court_vertical_range],
    "pulled up for a mid-range shot" : [test.Player_init.court_horizontal_range,test.Player_init.court_vertical_range],
    "pulled up for a three-point shot" : [test.Player_init.court_horizontal_range,test.Player_init.court_vertical_range],
    "grabbed the rebound" : [test.Player_init.court_horizontal_range,test.Player_init.court_vertical_range],
    "missed the rebound" : [test.Player_init.court_horizontal_range,test.Player_init.court_vertical_range],
    """
    
    for i in play_animation:
        print(max(play_animation[i][0]))


    def animate_play(i):
        for play in play_animation:
                if play in Game_sim.play_log[i]:
                    for name in range(len(players)):
                        if str((players[name]).info.first_name) and str((players[name]).info.last_name) in Game_sim.play_log[i]:
                            players[name].bottom = random.randint(play_animation[play][0][0],play_animation[play][0][1])   #change from numbers to min and max | max(play_animation[i][0])
                            players[name].left = random.randint(play_animation[play][1][0],play_animation[play][1][1])
                            page.update()
                            time.sleep(2)
                            players[name].bottom = random.randint(test.Player_init.court_vertical_range[0],test.Player_init.court_vertical_range[1])
                            players[name].left = random.randint(test.Player_init.court_horizontal_range[0],test.Player_init.court_horizontal_range[1])
                            print(str((players[name]).info.first_name),str((players[name]).info.last_name),"Cleared the ball")
                            page.update()
                            time.sleep(2)
                        else:
                            print("Searching...")
        

   
 



    def run_play(e):
        
        #court_player_1.bottom = random.randint(min(court_vertical_range),max(court_vertical_range))
        #court_player_1.left = random.randint(min(court_horizontal_range),max(court_horizontal_range))


        print((players[0]).info.first_name,players[0].info.last_name)
        for i in range(len(Game_sim.play_log)):
            animate_play(i)

            
                



            time.sleep(0.03)        
                
            
        page.update()
        time.sleep(.7) 

    def run_sim(e):
        start_sim()
        print(Game_sim.play_log)

    page.add(
        court,
        ft.ElevatedButton("Animate!", on_click=run_play),
        ft.ElevatedButton("Start Game", on_click=run_sim),

    )



ft.app(target=main)








 


































































