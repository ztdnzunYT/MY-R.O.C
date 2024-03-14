
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
    
    player_size = 40  
    player_speed = 500
    court_horizontal_range = [60,280]
    court_vertical_range = [15,200]

    court_pic = ft.Image( src="lib\\assets\\images\\basketball-half-court-parquet-600nw-122537710.png",width=380,height=380,scale=.9,fit=ft.ImageFit.COVER,
                            repeat=ft.ImageRepeat.NO_REPEAT,border_radius=ft.border_radius.all(5))


    class Player_init(ft.Container):
        player_size = 40  
        player_speed = 500
        court_horizontal_range = [60,280]
        court_vertical_range = [15,200]
        def __init__(self,height,bgcolor,info):
                super().__init__()
                self.width = player_size
                self.height = height 
                self.bgcolor = bgcolor
                self.info = info
                self.shape = ft.BoxShape.CIRCLE
                self.alignment = ft.alignment.center
                self.content = ft.Text(value=my_team_player1.position,text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.W_500,color=ft.colors.WHITE)



    p = Player_init(player_size,ft.colors.GREEN,(my_team_player1.position))



    court_player_1 = ft.Container(width=player_size,height=player_size,shape=ft.BoxShape.CIRCLE,bgcolor=ft.colors.RED,border=ft.border.all(2,ft.colors.WHITE24),animate_position=player_speed,
                                    alignment=ft.alignment.center,content=(ft.Text("PG",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.W_500,color=ft.colors.WHITE)),left=0)
    court_player_2 = ft.Container(width=player_size,height=player_size,shape=ft.BoxShape.CIRCLE,bgcolor=ft.colors.AMBER_700,border=ft.border.all(2,ft.colors.WHITE24),animate_position=player_speed,
                                    alignment=ft.alignment.center,bottom=100,left=140,content=(ft.Text("SF",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.W_500,color=ft.colors.WHITE)))
    court_player_3 = ft.Container(width=player_size,height=player_size,shape=ft.BoxShape.CIRCLE,bgcolor=ft.colors.BLUE,border=ft.border.all(2,ft.colors.WHITE24),animate_position=player_speed,
                                    alignment=ft.alignment.center,bottom=50,left=110,content=(ft.Text("C",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.W_500,color=ft.colors.WHITE)))
    court_ball = ft.Container(width=player_size/1.8,height=player_size/1.8,shape=ft.BoxShape.CIRCLE,bgcolor=ft.colors.ORANGE_600,border=ft.border.all(2,ft.colors.WHITE24),
                                animate_position=player_speed,alignment=ft.alignment.center,bottom=100,left=140)
    

    on_court_items = ft.Stack([court_player_1,court_player_2,court_player_3],height=250,expand=True)

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
    

    def play_checker(play):
         pass
        





    def run_play(e):
        
        court_player_1.bottom = random.randint(min(court_vertical_range),max(court_vertical_range))
        court_player_1.left = random.randint(min(court_horizontal_range),max(court_horizontal_range))

        for i in range(len(Game_sim.play_log)):
            print("Searching ...")
            time.sleep(.1)
            if my_team_player1.first_name and my_team_player1.last_name and "cleared the ball" in Game_sim.play_log[i]:
                print(Game_sim.play_log[i])
            
            



        page.update()
        time.sleep(.7) 

    def run_sim(e):
        start_sim()
        print(Game_sim.play_log)

    page.add(
        court,
        p,
        ft.ElevatedButton("Animate!", on_click=run_play),
        ft.ElevatedButton("Start Game", on_click=run_sim),

    )



ft.app(target=main)








 


































































