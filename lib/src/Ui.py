import flet as ft
import random
import time
import math
import Player_database_connector as pdc
from Player_database_reset_manager import database_manager as Dbm
from Player_db_creator import create_all_tables
from Player_creator import run as pc_run 
from Test_simgame import Game_sim, Game_stats, start_sim
from Player_team_initializer import My_team_query , my_team_player1 , my_team_player2 , my_team_player3


def main(page: ft.Page):
    page.title = "MY R.O.C MANAGER"
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    print(page.width,page.height)
    page.window_frameless = False
    page.window_width=1050
    page.window_height = 690
    page.window_min_height=690
    page.window_min_width=1000
    page.window_center()


    page.on_window_event = page.update()

    class new_or_load_management:

        
        new_management_button = ft.Container(
            content=ft.TextButton(
            text="New Management",
            disabled=False,
            on_click=lambda e: new_or_load_management.new_management()
            )
        )
        load_management_button = ft.Container(
            content=ft.TextButton(
            text="Load Management",
            on_click=lambda e: new_or_load_management.load_management()
            )
        )

        if My_team_query.my_team == []:
            load_management_button.disabled = True
        else:
            load_management_button.disabled = False

        def new_management():
            Dbm.reset_all()
            Player_search.table.rows.clear()  #improves player search menu smooth loading
            create_all_tables()
            print("Database info reset")
            pc_run()
            return page.go("/Dashboard")
            
        
        def load_management():
            return page.go("/Dashboard")
        

    class Main_menu:
        def side_menu():
            return ft.Row(
                [
                    ft.Container(  
                        expand=False,
                        width=110,
                        height=page.window_height,
                        margin=10,
                        border_radius= 10,
                        border=ft.border.all(2, ft.colors.WHITE24),
                        bgcolor=ft.colors.BACKGROUND,
                        alignment=ft.alignment.top_center,
                        content=ft.Container(
                            ft.Column(
                                alignment=ft.alignment.center,
                                scroll=ft.ScrollMode.AUTO,
                                controls=
                            [
                                ft.IconButton(
                                    icon=ft.icons.SPACE_DASHBOARD,
                                    icon_color=ft.colors.WHITE60, 
                                    icon_size=50,
                                    tooltip="Dashboard",
                                    on_click=lambda _: page.go("/Dashboard"),
                                ), 
                                ft.IconButton(
                                    icon=ft.icons.SCOREBOARD,
                                    icon_color=ft.colors.WHITE60,
                                    icon_size=50,
                                    tooltip="Sim Game",
                                    on_click=lambda _: page.go("/Sim Game")
                                ),
                                ft.IconButton(
                                    icon=ft.icons.CONNECT_WITHOUT_CONTACT,
                                    icon_color=ft.colors.WHITE60,
                                    icon_size=50,
                                    tooltip="Online PVP",
                                    on_click=lambda _: page.go("/Online PvP")
                                ),
                                ft.IconButton(
                                    icon = ft.icons.SPORTS_BASKETBALL,
                                    icon_color=ft.colors.WHITE60,
                                    icon_size=45,
                                    tooltip="The R.O.C",
                                    on_click=lambda _: page.go("/The Roc")
                                ),
                                ft.IconButton(
                                    icon=ft.icons.PERSON_SEARCH_ROUNDED,
                                    icon_color=ft.colors.WHITE60,
                                    icon_size=50,
                                    tooltip="Player Search",
                                    on_click=lambda _: page.go("/Player Search")
                                ),
                                ft.IconButton(
                                    icon=ft.icons.MANAGE_ACCOUNTS,
                                    icon_color=ft.colors.WHITE60,
                                    icon_size=50,
                                    tooltip="My R.O.C Team",
                                    on_click=lambda _: page.go("/MY R.O.C Team")
                                ),
                                ft.IconButton(
                                    icon=ft.icons.SETTINGS_SHARP,
                                    icon_color=ft.colors.WHITE60,
                                    icon_size=45,
                                    tooltip="Settings",
                                    on_click=lambda _: page.go("/Settings")
                                ),
                                ft.IconButton(
                                    icon=ft.icons.LOGIN,
                                    icon_color=ft.colors.WHITE60,
                                    icon_size=40,
                                    tooltip="Logout",
                                    on_click=lambda _: page.go("/"),
                                ),
                                #ACCOUNT_CIRCLE_ROUNDED
                                #icons.LIST_ALT_ROUNDED
                            ]), 
                        margin=10,)
                    ),
                ],
                expand=False     
                )
     
        
        def default_menu_backdrop():
            return ft.Container(
                width=page.window_width,
                height=page.window_height,
                margin=5,
                border_radius=10,
                border=ft.border.all(2, ft.colors.WHITE24),
                alignment=ft.alignment.center,
                bgcolor=ft.colors.WHITE12,
                content=(ft.Text(
                    "MY R.O.C",
                    size=50,
                    color=ft.colors.with_opacity(0.5,ft.colors.WHITE),
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                    )),
                expand=True)
                
        def management_window():
            return ft.Container(
                margin=5,
                border_radius=10,
                border=ft.border.all(2, ft.colors.WHITE24),
                bgcolor=ft.colors.BLACK12,
                content=ft.Container(
                    width=300,
                    height=300,
                    bgcolor=ft.colors.WHITE12,
                    border_radius=20,
                    alignment=ft.alignment.center,
                    content=
                        ft.Column([
                            ft.Text("MY R.O.C",size=50,weight=ft.FontWeight.BOLD),
                            ft.Container(
                                width=160,
                                height=30,
                                bgcolor=ft.colors.TRANSPARENT,
                                alignment=ft.alignment.center,
                                content=(
                                    new_or_load_management.new_management_button
                                )
                            ),
                            ft.Container(
                                width=160,
                                height=30,
                                bgcolor=ft.colors.TRANSPARENT,
                                alignment=ft.alignment.center,
                                content=(
                                    new_or_load_management.load_management_button
                                )
                            ),
                            
                            ],
                            spacing=15,
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                ), 
                expand=True,
                alignment=ft.alignment.center
            )
        
            
    class Dashboard:
        def dashboard():
            print(f"{page.route} Menu item clicked")
            return ft.Container(
                width=page.window_width,
                height=page.window_height,
                margin=10,
                border_radius=10,
                border=ft.border.all(2, ft.colors.WHITE24),
                alignment=ft.alignment.center,
                bgcolor=ft.colors.TRANSPARENT,
                content=ft.Row([
                    ft.Tabs(
                        unselected_label_color=ft.colors.WHITE54, 
                        label_color=ft.colors.WHITE,
                        indicator_color=ft.colors.WHITE,
                        height=page.window_height -50,
                        width=page.window_width -200,
                        selected_index = 0,
                        animation_duration=400,
                        expand=True,

                        tabs=[
                            ft.Tab(
                                text="HOME",
                                tab_content=ft.Text("HOME",size=20),
                                content=ft.Container(
                                    alignment=ft.alignment.center,
                                    margin=20,
                                    border_radius=15,
                                    expand=True,
                                    content=ft.Row([
                                        ft.Column([
                                            ft.Container(
                                                padding=10,
                                                bgcolor=ft.colors.WHITE38,
                                                alignment=ft.alignment.center,
                                                margin=5,
                                                border_radius=5,
                                                expand=True,
                                                ink=True,
                                                on_click=lambda _: page.go("/Sim Game"),
                                                content=
                                                    ft.Stack([
                                                        ft.Text("SIM GAME",size=50,color=ft.colors.BLACK,weight=ft.FontWeight.BOLD,expand=False,text_align=ft.TextAlign.CENTER,italic=True,max_lines=3),
                                                        ft.Text("SIM GAME",size=50,color=ft.colors.WHITE,weight=ft.FontWeight.BOLD,expand=False,text_align=ft.TextAlign.CENTER,italic=True,max_lines=3),
                                                    ])
                                                ),
                                            ft.Container(
                                                padding=10,
                                                bgcolor=ft.colors.WHITE38,
                                                alignment=ft.alignment.center,
                                                margin=5,
                                                border_radius=5,
                                                expand=True,
                                                ink=True,
                                                on_click=lambda _: page.go("/Online PvP"),
                                                content=ft.Text("ONLINE PVP",size=50,color=ft.colors.WHITE,weight=ft.FontWeight.BOLD,expand=False,text_align=ft.TextAlign.CENTER,italic=True,max_lines=3),
                                                ),
                                            ft.Container(
                                                padding=10,
                                                bgcolor=ft.colors.WHITE38,
                                                alignment=ft.alignment.center,
                                                margin=5,
                                                border_radius=5,
                                                expand=True,
                                                ink=True,
                                                on_click=lambda e: print("Clickable with Ink clicked!"),
                                                content=ft.Text("MY SEASON",size=50,color=ft.colors.WHITE,weight=ft.FontWeight.BOLD,expand=False,text_align=ft.TextAlign.CENTER,italic=True,max_lines=3),
                                                ),
                                        ],alignment=ft.MainAxisAlignment.CENTER,spacing=10,expand=True),
                                        
                                        ft.Column([
                                            ft.Container(
                                                width=page.window_width,  
                                                height = page.window_height/2.5,
                                                padding=10,
                                                bgcolor=ft.colors.WHITE38,
                                                alignment=ft.alignment.top_center,
                                                margin=5,
                                                border_radius=5,
                                                expand=True,
                                                content=ft.Column([
                                                ft.Container(
                                                    bgcolor=ft.colors.TRANSPARENT,
                                                    alignment=ft.alignment.center,
                                                    content=ft.Text(
                                                    "SOCIAL MEDIA",
                                                    size=20,
                                                    text_align=ft.TextAlign.CENTER,
                                                    weight=ft.FontWeight.BOLD,
                                                    color=ft.colors.WHITE,
                                                    italic=True,
                                                    ),
                                                ),
                                                ft.Container(
                                                    bgcolor=ft.colors.BLACK45,
                                                    expand=True,
                                                    margin=3,
                                                    border_radius=5,
                                                    border=ft.border.all(3, color=ft.colors.BLACK12),
                                                    )
                                                ],alignment=ft.CrossAxisAlignment.CENTER)
                                                ),
                                                
                                        ft.Container(width=page.window_width,
                                            height = page.window_height/5,
                                            bgcolor=ft.colors.WHITE38,
                                            alignment=ft.alignment.center,
                                            margin=5,
                                            border_radius=5,
                                            content=ft.Text("USER PROFILE",size=40,color=ft.colors.WHITE,weight=ft.FontWeight.BOLD,expand=False,text_align=ft.TextAlign.CENTER,italic=True,max_lines=3),
                                            expand=False),

                                        ],expand=True,spacing=5,alignment=ft.alignment.center)
                                    ],alignment=ft.alignment.center,expand=True,spacing=5),
                                )
                            ),
                    
                            ]
                            ,)]) ,expand=True
                            )
                

    class Sim_game():
        lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        switch = ft.Switch(label=" Fullscreen",value=True,scale=.7,active_color=ft.colors.BACKGROUND)
        my_team_score_display =  ft.Text(text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.W_500,value=0,size=15)
        ai_team_score_display =  ft.Text(text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.W_500,value=0,size=15)
        game_speed_slider = ft.Slider(value=1,min=0.04,max=2.5,divisions=3,width=300,active_color=ft.colors.WHITE70,label=" Gamespeed: {value}% ",
                                        on_change=lambda e: print((e.control.value)))
        
        class Players(ft.Container):
            court_min_max_width = [60,240]
            court_min_max_height = [10,205]    
            def __init__(self,shape,bgcolor,bottom,left,player_info):
                super().__init__()
                self.player_size = 40 #default vlaues
                self.player_speed = 500 
                self.width = self.player_size
                self.height = self.player_size
                self.animate_position = self.player_speed
                self.shape = shape
                self.bgcolor = bgcolor
                self.border = ft.border.all(2,ft.colors.WHITE24)
                self.alignment = ft.alignment.center
                self.bottom = bottom
                self.left = left
                self.player_info = player_info
                self.content = ft.Text(value=self.player_info.position if player_info != None else "",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.W_500,color=ft.colors.WHITE)
                self.expand = True
                

        court_player_1 = Players(ft.BoxShape.CIRCLE,ft.colors.RED,105,250,my_team_player1)    
        court_player_2 = Players(ft.BoxShape.CIRCLE,ft.colors.BLUE,180,170,my_team_player2)    
        court_player_3 = Players(ft.BoxShape.CIRCLE,ft.colors.ORANGE_600,30,130,my_team_player3)    
        court_ball = Players(ft.BoxShape.CIRCLE,ft.colors.AMBER_700,100,240,None)
        court_ball.width = 20
        court_ball.height = 20

        #court_player_1.bottom = 220
        #court_player_1.left = 100

        court_players = [court_player_1,court_player_2,court_player_3]

        court_icons = ft.Stack([court_player_1,court_player_2,court_player_3,court_ball],height=260,expand=True)

        court_picture = ft.Image( src="lib\\assets\\images\\basketball-half-court-parquet-600nw-122537710.png",width=380,height=380,scale=.9,fit=ft.ImageFit.COVER,
                                        repeat=ft.ImageRepeat.NO_REPEAT,border_radius=ft.border_radius.all(5))
        court = ft.Stack([
            ft.Container(
                width=court_picture.width,
                height=court_picture.height,
                content=(
                ft.Stack([
                    court_picture,
                    ft.Column([
                        ft.Row([
                            court_icons
                        ],
                        vertical_alignment=ft.alignment.center,alignment=ft.MainAxisAlignment.CENTER)
                    ],alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.alignment.center),
                ])
                )
            )
            ],expand=True)   
        

        court_horizontal_min_max = [70,250]
        court_vertical_min_max = [15,210]
    
        play_animation_pos = {
            "cleared the ball" : [[25,195],[215,230]],
            "checked in the ball" : [[105,105],[250,250]],  #lessen the horizontal max
            "dribbled the ball" : [[25,195],[60,240]],
            "went up for a layup" : [[75,155],[60,85]],
            "went up for a dunk" : [[95,130],[60,65]],
            "pulled up for a mid-range shot" : [[20,205],[70,175]],
            "pulled up for a three-point shot" : [[15,210],[215,250]],
            "grabbed the rebound" : [[75,155],[60,85]]
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
            #cleared the ball 
            """

        def court_resizing():
            Sim_game.court_picture.expand = True
            page.update()
        
        
        def animate_play(i):
            for play in Sim_game.play_animation_pos:
                if play in Game_sim.play_log[i]:
                    for name in Sim_game.court_players:
                        if (name.player_info.first_name and name.player_info.last_name) in Game_sim.play_log[i]:
                            name.bottom = random.randint(min(Sim_game.play_animation_pos[play][0]),max(Sim_game.play_animation_pos[play][0]))
                            name.left = random.randint(min(Sim_game.play_animation_pos[play][1]),max(Sim_game.play_animation_pos[play][1]))
                            page.update()
                            print(name.player_info.first_name,name.player_info.last_name, play)
                            time.sleep(1.3)
                            name.bottom = random.randint(min(Sim_game.court_vertical_min_max),max(Sim_game.court_vertical_min_max))
                            name.left = random.randint(min(Sim_game.court_horizontal_min_max),max(Sim_game.court_horizontal_min_max))
                            page.update()
                            time.sleep(1)

      
        def new_log_entry():
            
            my_team_score = 0
            ai_team_score = 0
            Sim_game.my_team_score_display.value = 0
            Sim_game.ai_team_score_display.value = 0
            Sim_game.my_team_score_display.color = ft.colors.WHITE
            Sim_game.ai_team_score_display.color = ft.colors.WHITE
            time.sleep(1)
            Sim_game.lv.controls.clear()
            
            
            for i in range(len(Game_sim.play_log)):
                time.sleep(round(Sim_game.game_speed_slider.value,3))
                Sim_game.lv.controls.append(ft.Text(f"{Game_sim.play_log[i]}",color=ft.colors.WHITE,weight=ft.FontWeight.W_500))
                Sim_game.animate_play(i)
                if "MY TEAM SCORE :" in Game_sim.play_log[i]:
                    my_team_score_list = []
                    for o in range(len(Game_sim.play_log[i])):
                        if (str(Game_sim.play_log[i][o])).isdigit(): 
                            my_team_score_list.append(Game_sim.play_log[i][o])
                            if len(my_team_score_list) == 1:
                                my_team_score = (my_team_score_list[0])
                            else:
                                my_team_score = (my_team_score_list[0] + my_team_score_list[1])
                    Sim_game.my_team_score_display.value = my_team_score
                if int(my_team_score) >= Game_stats.wining_score:
                    Sim_game.my_team_score_display.color = ft.colors.LIGHT_GREEN_ACCENT_400
                    Sim_game.ai_team_score_display.color = ft.colors.RED
                if "AI SCORE :" in Game_sim.play_log[i]:
                    ai_team_score_list = []
                    for o in range(len(Game_sim.play_log[i])):
                        if (str(Game_sim.play_log[i][o])).isdigit(): 
                            ai_team_score_list.append(Game_sim.play_log[i][o])
                            if len(ai_team_score_list) == 1 :
                                ai_team_score = (ai_team_score_list[0])
                            else:
                                ai_team_score = (ai_team_score_list[0] + ai_team_score_list[1])
                    Sim_game.ai_team_score_display.value = ai_team_score
                if int(ai_team_score) >= Game_stats.wining_score:
                    Sim_game.ai_team_score_display.color = ft.colors.LIGHT_GREEN_ACCENT_400
                    Sim_game.my_team_score_display.color = ft.colors.RED

                page.update()
            Game_sim.play_log.clear()
            start_sim()
            
      
        
        def sim_game():
            Sim_game.court_resizing()
            
            print(f"{page.route} Menu item clicked")
            return ft.Container(
                width=page.window_width,
                height=page.window_height,
                margin=10,
                border_radius=10,
                border=ft.border.all(2, ft.colors.WHITE24),
                alignment=ft.alignment.center,
                bgcolor=ft.colors.BACKGROUND,
                content=(
                    ft.Row(
                    [
                        ft.Container(
                            width=page.window_width,
                            height=page.window_height,
                            margin=20,
                            border_radius=5,
                            bgcolor=ft.colors.ERROR_CONTAINER,
                            alignment=ft.alignment.top_center,
                            content=(
                                ft.Column(
                                    [
                                        ft.Stack([
                                            
                                            ft.Row([
                                                ft.Container(
                                                    margin=ft.margin.only(top=10,left=10),
                                                    content=(
                                                        Sim_game.switch
                                                    )
                                                )
                                            ],vertical_alignment=ft.alignment.center),
                                            ft.Row([
                                                ft.Container(                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                                                    alignment=ft.alignment.center,
                                                    bgcolor=ft.colors.BLACK26,
                                                    width=100,
                                                    height=30,
                                                    margin=ft.margin.only(top=15),
                                                    border_radius=2,
                                                    content=
                                                    ft.Stack([
                                                        ft.Container(
                                                            margin=ft.margin.only(top=5,right=50),
                                                            content=
                                                            ft.Row([
                                                                Sim_game.my_team_score_display,
                                                            ],alignment=ft.MainAxisAlignment.CENTER,spacing=37,vertical_alignment=ft.alignment.center),
                                                        ),
                                                        ft.Container(
                                                            margin=ft.margin.only(top=5,left=50),
                                                            content=
                                                            ft.Row([
                                                                Sim_game.ai_team_score_display,
                                                            ],alignment=ft.MainAxisAlignment.CENTER,spacing=37,vertical_alignment=ft.alignment.center),
                                                        ),
                                                        ft.Container(
                                                            alignment=ft.alignment.center,
                                                            content=
                                                            ft.VerticalDivider(
                                                                thickness=2,
                                                                opacity=.5,
                                                                color=ft.colors.WHITE,
                                                            ),
                                                        )
                                                    ])
                                                ),    
                                                
                                            ],vertical_alignment=ft.alignment.center,alignment=ft.MainAxisAlignment.CENTER)    
                                        ]), 

                                        ft.Container(
                                            width=page.window_width,
                                            height=page.window_height/2.7,
                                            border_radius=2,
                                            margin=ft.margin.only(top=5,bottom=0,right=30,left=30),
                                            bgcolor=ft.colors.BACKGROUND,
                                            border=ft.border.all(2,ft.colors.BLACK26),
                                            alignment=ft.alignment.center,
                                            content=(
                                                Sim_game.court
                                            )
                                        ),
                                    ft.Row([
                                        Sim_game.game_speed_slider,
                                    ],alignment=ft.MainAxisAlignment.CENTER),


                                    ft.Row([
                                        ft.SegmentedButton(
                                            selected={"1"},
                                            selected_icon=ft.Icon(ft.icons.ARROW_RIGHT_ROUNDED,size=25),
                                            style=ft.ButtonStyle(bgcolor=ft.colors.BLACK26,padding=13,color=ft.colors.WHITE,side=ft.border.all(1,ft.colors.BLACK)),
                                            allow_multiple_selection=False,
                                         
                                            segments=[
                                                ft.Segment(
                                                    value="1",
                                                    label=ft.Text("Play style 1"),
                                                    ),
                                                ft.Segment(
                                                    value="2",
                                                    label=ft.Text("Play style 2"),
                                                    ),
                                                ft.Segment(                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
                                                    value="3",
                                                    label=ft.Text("Play style 3"),
                                                    ),
                                                ],
                                            )
                                    ],alignment=ft.MainAxisAlignment.CENTER),

                                    ft.Container(
                                        width=page.window_width,
                                        height=page.window_height,
                                        border_radius=10,
                                        margin=ft.margin.only(top=10,bottom=20,right=30,left=30),
                                        bgcolor=ft.colors.BLACK26,
                                        alignment=ft.alignment.center_left,
                                        expand=True,
                                        content=(
                                            ft.Row([
                                                ft.Container(
                                                height=page.window_height,
                                                alignment=ft.alignment.center,
                                                border_radius=5,
                                                bgcolor=ft.colors.WHITE24,
                                                margin=ft.margin.only(left=10,top=10,bottom=10,right=-5),
                                                expand=True,
                                                content=(
                                                    ft.Column([
                                                        ft.Row([
                                                            ft.Text("MY TEAM",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE,size=17,expand=True),
                                                        ],alignment=ft.MainAxisAlignment.CENTER,expand=True),
                                                        ft.Divider(color=ft.colors.BLACK38,thickness=2),
                                                        ft.Row([
                                                            ft.Text("AI TEAM 1",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE,size=17)
                                                        ],alignment=ft.MainAxisAlignment.CENTER,expand=True)

                                                    ],spacing=0,expand=True,alignment=ft.MainAxisAlignment.CENTER)
                                                    )
                                                ),
                                                ft.VerticalDivider(
                                                    thickness=3
                                                ),
                                                ft.Container(
                                                height=140,
                                                margin=ft.margin.only(top=0,bottom=0,right=20,left=0),
                                                alignment=ft.alignment.center,
                                                bgcolor=ft.colors.TRANSPARENT,
                                                expand=True,
                                                content=(
                                                    ft.ElevatedButton( text="Start Sim",icon=ft.icons.PLAY_ARROW_ROUNDED, style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=30,)
                                                                            ,padding=15),tooltip="Click to start sim",color=ft.colors.WHITE,bgcolor=ft.colors.WHITE30,on_click=lambda e: Sim_game.new_log_entry())
                                                )
                                                )
                                            ])
                                        )                                        
                                    ),  
                                    ],horizontal_alignment=ft.alignment.center) 
                                ),
                            expand=True
                        ),

                        ft.Container(
                            width=page.window_width/3.6,
                            height=page.window_height,
                            margin= ft.margin.only(left=-10,top=20,right=15,bottom=20),
                            border_radius=5,
                            bgcolor=ft.colors.WHITE38,
                            alignment=ft.alignment.center,
                            content=(                                
                                ft.Container(
                                    width=page.width,
                                    height=page.height,
                                    margin=ft.margin.only(top=10,bottom=10,left=15,right=15),
                                    alignment=ft.alignment.center,
                                    border=ft.border.all(2,ft.colors.BLACK12),
                                    bgcolor=ft.colors.BLACK38,
                                    content=ft.Container(
                                        ft.Column([
                                            ft.Row([
                                                ft.Container(
                                                    margin=ft.margin.only(top=10,bottom=-10),
                                                    alignment=ft.alignment.center,
                                                    content=(
                                                        ft.Text("GAME LOG",text_align=ft.TextAlign.CENTER,size=15,weight=ft.FontWeight.W_500,color=ft.colors.WHITE)
                                                    )
                                                ),
                                            ],alignment=ft.MainAxisAlignment.CENTER,vertical_alignment=ft.alignment.center),
                                            ft.Divider(color=ft.colors.BLACK26,thickness=2),
                                            Sim_game.lv
                                        ],alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.alignment.center)
                                    )
                                )
                            )    
                        ),

                    ], alignment=ft.MainAxisAlignment.CENTER,
                
                    )
                    
                    
                    ),
                expand=True)
        
    class The_Roc:
        def the_Roc():
            print(f"{page.route} Menu item clicked")
            return ft.Container(
            width=page.window_width,
            height=page.window_height,
            margin=10,
            border_radius=10,
            border=ft.border.all(2, ft.colors.WHITE24),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.BLACK12,
            content=(ft.Text(
                "The R.O.C",
                size=50,
                color=ft.colors.with_opacity(0.5,ft.colors.WHITE),
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER,
                )),
            expand=True)

    class Player_search:

        def player_inserter():
            pdc.mycursor.execute("SELECT * FROM player_hub")
            player_list = pdc.mycursor.fetchall()
            return player_list

        table = ft.DataTable(
            column_spacing=50,
            data_row_max_height=60,
            show_bottom_border=True,
            show_checkbox_column=False,
            columns=[
                ft.DataColumn(ft.Text(f"Id",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE),tooltip="Player row id"),
                ft.DataColumn(ft.Text(f"",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"First name",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Last name",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Age",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Height",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Weight",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"★ Rating",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Position",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Build",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Moral",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Trait",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Team name",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Skill set",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE),tooltip="Players with specific skill sets\ncan recieve attribute boosts"),
                ft.DataColumn(ft.Text(f"Injured",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Recovery days",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Potential",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Overall",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Offense",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Defense",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Roots",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Three pointer",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Midrange",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Layup",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Dunk",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Ball handle",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Speed",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Stamina",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Passing",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Strength",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Rebounding",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Interior defense",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Perimeter defense",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Steal",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Block",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Points",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Assists",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Rebounds",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Steals",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Blocks",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Turnovers",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Games played",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Points per game",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Assists per game",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Steals per game",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Blocks per game",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Rebounds per game",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Turnovers per game",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Field goal %",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Three point %",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f""))
            ],
            rows=[],
                #color=ft.colors.with_opacity(0.3,ft.colors.WHITE),
            )              

        def add_player(player_info):
            new_row = ft.DataRow(
                on_select_changed="",
                #color=ft.colors.with_opacity(0.3,ft.colors.WHITE),
                cells=[
                ]
            )
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info[0]}")))
            new_row.cells.append(ft.DataCell(ft.CircleAvatar(content=ft.Text(f"{str(player_info[1][0])}{str(player_info[2][0])}",text_align=ft.TextAlign.CENTER,size=20),
                                                             bgcolor=ft.colors.GREY_900,radius=20,color=ft.colors.WHITE70)))
            for i in range(49):
                if  i > 0 and i != 6:
                    new_row.cells.append(ft.DataCell(ft.Text(f"{player_info[i]}")))
                if i == 5:
                 (ft.DataCell(ft.Text(f"{player_info[i-1]} ft")))
                if i == 6: 
                 (ft.DataCell(ft.Text(f"{player_info[i-1]} lb")))
                if i == 6:
                    new_row.cells.append(ft.DataCell(ft.Text(f"{(int(player_info[i]) * "★")}")))
                if i == 15:
                 (ft.DataCell(ft.Text(f"{player_info[i-1]} dys")))
                if i == 16:
                 (ft.DataCell(ft.Text(f"{player_info[i-1]} pot")))
                if i == 17:
                 (ft.DataCell(ft.Text(f"{player_info[i-1]} ovr")))
                if i == 18:
                 (ft.DataCell(ft.Text(f"{player_info[i-1]} off")))
                if i == 19:
                 (ft.DataCell(ft.Text(f"{player_info[i-1]} def")))
                if i == 21:
                 (ft.DataCell(ft.Text(f"{player_info[i-1]} three")))
                if i == 22:
                 (ft.DataCell(ft.Text(f"{player_info[i-1]} midr")))
                if i == 23:
                 (ft.DataCell(ft.Text(f"{player_info[i-1]} lay")))
                if i == 24:
                 (ft.DataCell(ft.Text(f"{player_info[i-1]} dnk")))
                if i == 25:
                 (ft.DataCell(ft.Text(f"{player_info[i-1]} handle")))
                if i == 26:
                 (ft.DataCell(ft.Text(f"{player_info[i-1]} speed")))
                if i == 27:
                 (ft.DataCell(ft.Text(f"{player_info[i-1]} stam")))
                if i == 28:
                 (ft.DataCell(ft.Text(f"{player_info[i-1]} passing")))
                if i == 29:
                 (ft.DataCell(ft.Text(f"{player_info[i-1]} strength")))
                if i == 30:
                 (ft.DataCell(ft.Text(f"{player_info[i-1]} rebound")))
                if i == 31:
                 (ft.DataCell(ft.Text(f"{player_info[i-1]} int d")))
                if i == 32:
                 (ft.DataCell(ft.Text(f"{player_info[i-1]} per d")))
                if i == 33:
                 (ft.DataCell(ft.Text(f"{player_info[i-1]} stl")))
                if i == 34:
                 (ft.DataCell(ft.Text(f"{player_info[i-1]} blk")))
                if i == 35:
                 (ft.DataCell(ft.Text(f"{player_info[i-1]} pts")))
                if i == 36:
                 (ft.DataCell(ft.Text(f"{player_info[i-1]} asts")))
                if i == 37:
                 (ft.DataCell(ft.Text(f"{player_info[i-1]} rebs")))
                if i == 38:
                 (ft.DataCell(ft.Text(f"{player_info[i-1]} stls")))
                if i == 39:
                 (ft.DataCell(ft.Text(f"{player_info[i-1]} blks")))
                if i == 40:
                 (ft.DataCell(ft.Text(f"{player_info[i-1]} trnvrs")))
                if i == 41:
                 (ft.DataCell(ft.Text(f"{player_info[i-1]} games played")))
                if i == 42:
                 (ft.DataCell(ft.Text(f"{player_info[i-1]} ppg")))
                if i == 43:
                 (ft.DataCell(ft.Text(f"{player_info[i-1]} apg")))
                if i == 44:
                 (ft.DataCell(ft.Text(f"{player_info[i-1]} spg")))
                if i == 45:
                 (ft.DataCell(ft.Text(f"{player_info[i-1]} bpg")))
                if i == 46:
                 (ft.DataCell(ft.Text(f"{player_info[i-1]} rpg")))
                if i == 47:
                 (ft.DataCell(ft.Text(f"{player_info[i-1]} tpg")))
                if i == 48:
                 (ft.DataCell(ft.Text(f"{player_info[i-1]} fg%")))
                if i == 49:
                 (ft.DataCell(ft.Text(f"{player_info[i-1]} 3pt%")))
                
                 #NOTE TO SELF. MIGHT NEED TO ADD THIS FOR THE ATTRIBUTE AND PERCENTS IN FUTURE 
                
                    # AS WELL AS ADD STACK IN ORDER TO SEE THE SPECIFIC COLUMN NAMES WHILE SCROLLING 
            new_row.cells.append(ft.DataCell(ft.CupertinoCheckbox()))
            Player_search.table.rows.append(new_row)
            page.update()
           
        #Way to delete all the rows to be able to make a new list with filters
        def delete_player():
            print("player deleted")
            for i in range(len(Player_search.table.rows)):
                Player_search.table.rows.pop()
                page.update()
        
        def add_multiple():
            for i in range(50):
                Player_search.add_player(Player_search.player_inserter()[i])

        def player_search_menu():  
            print(f"{page.route} Menu item clicked")
            Player_search.table.rows.clear() #Deletes all of player search 

            return ft.Container(
                width=page.window_width,
                height=page.window_height,
                margin=10,
                border_radius=10,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.with_opacity(0.1,ft.colors.WHITE),
                expand=True,
                content=ft.Row([
                    ft.Container(
                        padding=10,
                        expand=True,
                        border_radius=10,
                        content=ft.Row(
                            [
                                ft.Column([
                                        ft.Row([
                                            ft.FilledTonalButton(text="Search players",on_click=lambda e: Player_search.add_multiple()),
                                            ft.FilledTonalButton(text="Clear search",on_click=lambda e: Player_search.delete_player())
                                            ]),
                                        Player_search.table,
                                    ],scroll=ft.ScrollMode.AUTO,alignment=ft.alignment.center,on_scroll_interval=.1
                                ),
                            ],
                            scroll=ft.ScrollMode.AUTO,alignment=ft.alignment.center
                            ),
                        alignment=ft.alignment.top_center
                    )
                ],
                expand=True,
                alignment=ft.MainAxisAlignment.CENTER
                )
            )   
        

    class Online_pvp:
        def online_pvp():
            print(f"{page.route} Menu item clicked")
            return ft.Container(
                width=page.window_width,
                height=page.window_height,
                margin=10,
                border_radius=10,
                border=ft.border.all(2, ft.colors.WHITE24),
                alignment=ft.alignment.center,
                bgcolor=ft.colors.BLACK12,
                content=(ft.Text(
                    "Online PvP",
                    size=50,
                    color=ft.colors.with_opacity(0.5,ft.colors.WHITE),
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                    )),
                expand=True)

    class My_ROC_Team:
        

        def player_inserter():
            pdc.mycursor.execute("SELECT * FROM my_team")
            my_team = pdc.mycursor.fetchall()
            return my_team

        class My_team_stats(ft.Row):
            def __init__(self,content):
                super().__init__()
                self.content = content
                self.controls = ft.Container(
                    alignment=ft.alignment.top_center,
                    content=self.content),
                self.vertical_alignment = ft.alignment.top_center,
                self.alignment = ft.MainAxisAlignment.CENTER

        upgrade_points = ft.Text(value=0)
        

        class Stat_upgrader(ft.Container):
            
            class Sliders:
                layup = ft.Slider(active_color=ft.colors.WHITE,value=0,min=0,max=100,divisions=5,disabled=True,expand=True,)
                dunk = ft.Slider(value=0,min=0,max=100,divisions=5,disabled=True,expand=True)
                mid_range = ft.Slider(value=0,min=0,max=100,divisions=5,disabled=True,expand=True)
                three = ft.Slider(value=0,min=0,max=100,divisions=5,disabled=True,expand=True)
                handles = ft.Slider(value=0,min=0,max=100,divisions=5,disabled=True,expand=True)
                passing = ft.Slider(value=0,min=0,max=100,divisions=5,disabled=True,expand=True)
                steal = ft.Slider(value=0,min=0,max=100,divisions=5,disabled=True,expand=True)
                block = ft.Slider(value=0,min=0,max=100,divisions=5,disabled=True,expand=True)
                rebounding = ft.Slider(value=0,min=0,max=100,divisions=5,disabled=True,expand=True)
                interior_defense = ft.Slider(value=0,min=0,max=100,divisions=5,disabled=True,expand=True)
                perimeter_defense = ft.Slider(value=0,min=0,max=100,divisions=5,disabled=True,expand=True)
                speed = ft.Slider(value=0,min=0,max=100,divisions=5,disabled=True,expand=True)
                stamina = ft.Slider(value=0,min=0,max=100,divisions=5,disabled=True,expand=True)
                strength = ft.Slider(value=0,min=0,max=100,divisions=5,disabled=True,expand=True)

                
                

            def __init__(self,stat_name,slider):
                super().__init__()
                self.margin = ft.margin.only(left=30,right=30)
                self.stat_name = stat_name
                self.slider = slider
                self.content = My_ROC_Team.Stat_upgrader.build(self)
                self.alignment = ft.alignment.center
            def build(self):
                self.stat_label = ft.Text(value=self.stat_name,text_align=ft.TextAlign.CENTER,tooltip=f"Determines success chance of {str(self.stat_name).lower()}",color=ft.colors.WHITE)
                self.stat_increaser_button = ft.IconButton(ft.icons.ADD,on_click=lambda e: stat_increaser())
                def stat_increaser():
                    self.slider.value = self.slider.value + 20 
                    page.update()
                return ft.Row([self.stat_label,self.slider,self.stat_increaser_button],alignment=ft.MainAxisAlignment.CENTER,vertical_alignment=ft.alignment.center)

        team_online_wins_losses = ft.Text("Wins | Losses",text_align=ft.alignment.center,size=15,expand=True,color=ft.colors.WHITE)
        team_online_win_percent = ft.Text("Win percentage 0%",text_align=ft.alignment.center,size=15,color=ft.colors.WHITE)
        team_mvp = ft.Text("MVP",text_align=ft.alignment.center,size=15,color=ft.colors.WHITE)
        team_online_play_style = ft.Text("Playstyle",text_align=ft.alignment.center,size=15,color=ft.colors.WHITE) 
        team_online_games_played = ft.Text("Games played",text_align=ft.alignment.center,size=15,color=ft.colors.WHITE)
        team_online_points_scored = ft.Text("Carrer online points",text_align=ft.alignment.center,size=15,color=ft.colors.WHITE)
        sim_games_wins_losses =  ft.Text("Wins | Losses",text_align=ft.alignment.center,size=15,expand=True,color=ft.colors.WHITE)
        sim_games_win_percent = ft.Text("Win percentage 0%",text_align=ft.alignment.center,size=15,color=ft.colors.WHITE)
        sim_games_played =  ft.Text("Games played",text_align=ft.alignment.center,size=15,color=ft.colors.WHITE)
        sim_games_points_scored =  ft.Text("Carrer offline points",text_align=ft.alignment.center,size=15,color=ft.colors.WHITE)

        #team_performance_graph = 

        team_name = ft.Text("MY TEAM",text_align=ft.TextAlign.CENTER,expand=True,size=25,weight=ft.FontWeight.W_500)
        players = [my_team_player1,my_team_player2,my_team_player3]

        table = ft.DataTable(
            column_spacing=50,
            data_row_max_height=65,
            show_bottom_border=False,
            show_checkbox_column=False,
            bgcolor=ft.colors.BLACK12,
            columns=[
                ft.DataColumn(ft.Text(f"Id",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE),tooltip="Player row id"),
                ft.DataColumn(ft.Text(f"",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"First name",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Last name",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Age",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Height",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Weight",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"★ Rating",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Position",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Build",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Moral",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Trait",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Team name",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Skill set",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE),tooltip="Players with specific skill sets\ncan recieve attribute boosts"),
                ft.DataColumn(ft.Text(f"Injured",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Recovery days",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Potential",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Overall",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Offense",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Defense",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Roots",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Three pointer",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Midrange",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Layup",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Dunk",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Ball handle",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Speed",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Stamina",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Passing",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Strength",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Rebounding",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Interior defense",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Perimeter defense",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Steal",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Block",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Points",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Assists",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Rebounds",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Steals",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Blocks",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Turnovers",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Games played",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Points per game",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Assists per game",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Steals per game",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Blocks per game",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Rebounds per game",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Turnovers per game",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Field goal %",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f"Three point %",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,color=ft.colors.WHITE)),
                ft.DataColumn(ft.Text(f""))
            ],
            rows=[
                #color=ft.colors.with_opacity(0.3,ft.colors.WHITE),
            ],
        )   
      
        def stat_updater(player_info):
            My_ROC_Team.Stat_upgrader.Sliders.layup.value = player_info.layup
            My_ROC_Team.Stat_upgrader.Sliders.dunk.value = player_info.dunk
            My_ROC_Team.Stat_upgrader.Sliders.mid_range.value = player_info.midrange
            My_ROC_Team.Stat_upgrader.Sliders.three.value = player_info.three_pointer
            My_ROC_Team.Stat_upgrader.Sliders.handles.value = player_info.ball_handle
            My_ROC_Team.Stat_upgrader.Sliders.passing.value = player_info.passing
            My_ROC_Team.Stat_upgrader.Sliders.steal.value = player_info.steal
            My_ROC_Team.Stat_upgrader.Sliders.block.value = player_info.block
            My_ROC_Team.Stat_upgrader.Sliders.rebounding.value = player_info.rebounding
            My_ROC_Team.Stat_upgrader.Sliders.interior_defense.value = player_info.interior_defense
            My_ROC_Team.Stat_upgrader.Sliders.perimeter_defense.value = player_info.perimeter_defense
            My_ROC_Team.Stat_upgrader.Sliders.speed.value = player_info.speed
            My_ROC_Team.Stat_upgrader.Sliders.stamina.value = player_info.stamina
            My_ROC_Team.Stat_upgrader.Sliders.strength.value = player_info.strength
            My_ROC_Team.piechart.finishing.value = player_info.layup + player_info.dunk
            My_ROC_Team.piechart.shooting.value = player_info.midrange + player_info.three_pointer
            My_ROC_Team.piechart.playmaking.value = player_info.passing + player_info.ball_handle
            My_ROC_Team.piechart.defense.value = player_info.steal + player_info.block + player_info.rebounding + player_info.interior_defense + player_info.perimeter_defense
            My_ROC_Team.piechart.physicals.value = player_info.speed + player_info.stamina + player_info.strength
            page.update()
        
        def add_player(player_info):
            new_row = ft.DataRow(cells=[ ],on_select_changed=lambda e: My_ROC_Team.stat_updater(player_info))
            my_team_player1.rebounding
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.id}",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.CircleAvatar(content=ft.Text(f"{str(player_info.first_name[0])}{str(player_info.last_name[0])}",text_align=ft.TextAlign.CENTER,size=20),bgcolor=ft.colors.GREY_800,radius=20,color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.first_name}",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.last_name}",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.age}",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.height} ft",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.weight} lb",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{(player_info.star_rating * "★")}",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.position}",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.build}",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.moral}",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.trait}",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.team_name}",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.skill_set}",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.injured}",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.recovery_days} dys",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.potential} pot",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.overall} ovr",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.offense} off",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.defense} def",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.roots} roots",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.three_pointer} three",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.midrange} midr",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.layup} lay",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.dunk} dnk",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.ball_handle} handle",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.speed} speed",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.stamina} stam",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.passing} pass",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.strength} strength",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.rebounding} rebound",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.interior_defense} int d",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.perimeter_defense} per d",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.steal} stl",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.block} blk",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.points} pts",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.assists} asts",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.rebounds} rebs",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.steals} stls",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.blocks} blks",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.turnovers} trnvrs",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.games_played} games played",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.points_per_game} ppg",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.assists_per_game} apg",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.steals_per_game} spg",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.blocks_per_game} bpg",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.rebounds_per_game} rpg",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.turnovers_per_game} tpg",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.field_goal_percentage} fg%",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info.three_point_percentage} 3pt%",color=ft.colors.WHITE)))
            new_row.cells.append(ft.DataCell(ft.CupertinoCheckbox())) 
            new_row.cells.append(ft.DataCell(ft.Text(f"")))    
                 #NOTE TO SELF. MIGHT NEED TO ADD THIS FOR THE ATTRIBUTE AND PERCENTS IN FUTURE 
                    # AS WELL AS ADD STACK IN ORDER TO SEE THE SPECIFIC COLUMN NAMES WHILE SCROLLING 
            My_ROC_Team.table.rows.append(new_row)
            page.update()
        
        def add_multiple():
            for i in range(len(My_ROC_Team.players)):
                My_ROC_Team.add_player(My_ROC_Team.players[i])

        class piechart:

            normal_radius = 80
            normal_title_style = ft.TextStyle(size=15, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD)

            finishing = ft.PieChartSection(
                value=25,
                title="Finishing",
                title_style = normal_title_style,
                color=ft.colors.BLUE,
                radius=normal_radius,
            )
            shooting = ft.PieChartSection(
                value=25,
                title="Shooting",
                title_style = normal_title_style,
                color=ft.colors.LIGHT_GREEN_ACCENT_400,
                radius=normal_radius,
            )
            playmaking = ft.PieChartSection(
                value=25,
                title="Playmaking",
                title_style = normal_title_style,
                color=ft.colors.ORANGE,
                radius=normal_radius,
            )
            defense = ft.PieChartSection(
                value=25,
                title="Defense",
                title_style = normal_title_style,
                color=ft.colors.RED,
                radius=normal_radius,
            )    
            physicals = ft.PieChartSection(
                value=25,
                title="Physicals",
                title_style = normal_title_style,
                color=ft.colors.PURPLE,
                radius=normal_radius,
            )

            chart = ft.PieChart(
                sections=[
                defense,
                playmaking,
                finishing,
                shooting,
                physicals
                ],sections_space=0,
                center_space_radius=60,
                expand=True
            )

        def my_roc_team():
            My_ROC_Team.table.rows.clear()
            My_ROC_Team.player_inserter()
            My_ROC_Team.add_multiple()
            print(f"{page.route} Menu item clicked")
            return ft.Container(
                border_radius=10,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.with_opacity(0.3,ft.colors.WHITE),
                expand=True,
                content=
                    ft.Column([
                        ft.Row([
                            ft.Container(
                                width=150,
                                height=page.height,
                                bgcolor=ft.colors.with_opacity(0.57,ft.colors.TRANSPARENT),
                                border=ft.border.only(right=ft.border.BorderSide(2.5,color=ft.colors.with_opacity(0.1,ft.colors.WHITE))),
                                content=ft.Column([
                                            ft.Row([
                                                ft.Container(
                                                    alignment=ft.alignment.center,
                                                    margin=ft.margin.only(top=10,bottom=-8.5),
                                                    content=My_ROC_Team.team_name),
                                            ],vertical_alignment=ft.alignment.top_center,alignment=ft.MainAxisAlignment.CENTER),
                                            ft.Divider(thickness=.3,color=ft.colors.with_opacity(.4,ft.colors.WHITE)),
                                            My_ROC_Team.My_team_stats(ft.Text("Online team stats",text_align=ft.alignment.center,size=15)),
                                            ft.Divider(thickness=.3,color=ft.colors.with_opacity(.4,ft.colors.WHITE)),
                                            My_ROC_Team.My_team_stats(My_ROC_Team.team_online_wins_losses),
                                            ft.Divider(thickness=.3,color=ft.colors.with_opacity(.4,ft.colors.WHITE)),
                                            My_ROC_Team.My_team_stats(My_ROC_Team.team_online_win_percent),
                                            ft.Divider(thickness=.3,color=ft.colors.with_opacity(.4,ft.colors.WHITE)),
                                            My_ROC_Team.My_team_stats(My_ROC_Team.team_mvp),
                                            ft.Divider(thickness=.3,color=ft.colors.with_opacity(.4,ft.colors.WHITE)),
                                            My_ROC_Team.My_team_stats(My_ROC_Team.team_online_play_style),
                                            ft.Divider(thickness=.3,color=ft.colors.with_opacity(.4,ft.colors.WHITE)),
                                            My_ROC_Team.My_team_stats(My_ROC_Team.team_online_games_played),
                                            ft.Divider(thickness=.3,color=ft.colors.with_opacity(.4,ft.colors.WHITE)),
                                            My_ROC_Team.My_team_stats(My_ROC_Team.team_online_points_scored),
                                            ft.Divider(thickness=.3,color=ft.colors.with_opacity(.4,ft.colors.WHITE)),

                                            # graph

                                            My_ROC_Team.My_team_stats(ft.Text("Offline team stats",text_align=ft.alignment.center,size=15)),
                                            ft.Divider(thickness=.3,color=ft.colors.with_opacity(.4,ft.colors.WHITE)),
                                            My_ROC_Team.My_team_stats(My_ROC_Team.sim_games_wins_losses),
                                            ft.Divider(thickness=.3,color=ft.colors.with_opacity(.4,ft.colors.WHITE)),
                                            My_ROC_Team.My_team_stats(My_ROC_Team.sim_games_win_percent),
                                            ft.Divider(thickness=.3,color=ft.colors.with_opacity(.4,ft.colors.WHITE)),
                                            My_ROC_Team.My_team_stats(My_ROC_Team.sim_games_played),
                                            ft.Divider(thickness=.3,color=ft.colors.with_opacity(.4,ft.colors.WHITE)),
                                            My_ROC_Team.My_team_stats(My_ROC_Team.sim_games_points_scored),
                                            ft.Divider(thickness=.3,color=ft.colors.with_opacity(.4,ft.colors.WHITE)),
                                            My_ROC_Team.My_team_stats(ft.Text("")),
                                            ft.Divider(thickness=.3,color=ft.colors.TRANSPARENT),
                                        ],alignment=ft.alignment.center,horizontal_alignment=ft.alignment.center,scroll=ft.ScrollMode.AUTO,expand=True)
                                ),

                            ft.Container(
                         
                                expand=True,
                  
                                content=(
                                    ft.Column([
                                        ft.Row([
                                            ft.Container( 
                                                expand=True,
                                                bgcolor=ft.colors.with_opacity(.6,ft.colors.GREY_400),
                                                content=ft.Column([
                                                    ft.Row([
                                                       My_ROC_Team.table

                                                       ],scroll=ft.ScrollMode.AUTO,
                                                    ), 

                                                    ft.Row([
                                                       ft.Container(
                                                        height=page.height,
                                                        border=ft.border.only(top=ft.BorderSide(2.5,ft.colors.with_opacity(.1,ft.colors.WHITE))),
                                                        bgcolor=ft.colors.with_opacity(0.6,ft.colors.TRANSPARENT),
                                                        expand=True,
                                                        content=(
                                                           ft.Row([
                                                           My_ROC_Team.piechart.chart],expand=True)
                                                        )
                                                    ),
                                                        
                                                        ft.Container(
                                                        height=page.height,
                                                        border=ft.border.only(top=ft.BorderSide(2.5,ft.colors.with_opacity(.1,ft.colors.WHITE))),
                                                        bgcolor=ft.colors.with_opacity(0.7,ft.colors.TRANSPARENT),
                                                        expand=True,
                                                        content=(
                                                            ft.Column([
                                                                ft.Container(height=20),
                                                                ft.Row([
                                                                ft.Text(value=f"Upgrade point remaining : {My_ROC_Team.upgrade_points.value}",text_align=ft.TextAlign.CENTER,color=ft.colors.WHITE)],alignment=ft.MainAxisAlignment.CENTER),
                                                                My_ROC_Team.Stat_upgrader("Layup",My_ROC_Team.Stat_upgrader.Sliders.layup),
                                                                My_ROC_Team.Stat_upgrader("Dunk",My_ROC_Team.Stat_upgrader.Sliders.dunk),
                                                                My_ROC_Team.Stat_upgrader("Mid\nrange",My_ROC_Team.Stat_upgrader.Sliders.mid_range),
                                                                My_ROC_Team.Stat_upgrader("Three",My_ROC_Team.Stat_upgrader.Sliders.three),
                                                                My_ROC_Team.Stat_upgrader("Handles",My_ROC_Team.Stat_upgrader.Sliders.handles),
                                                                My_ROC_Team.Stat_upgrader("Passing",My_ROC_Team.Stat_upgrader.Sliders.passing),
                                                                My_ROC_Team.Stat_upgrader("Steal",My_ROC_Team.Stat_upgrader.Sliders.steal),
                                                                My_ROC_Team.Stat_upgrader("Block",My_ROC_Team.Stat_upgrader.Sliders.block),
                                                                My_ROC_Team.Stat_upgrader("Rebound",My_ROC_Team.Stat_upgrader.Sliders.rebounding),
                                                                My_ROC_Team.Stat_upgrader("Interior\nDefense",My_ROC_Team.Stat_upgrader.Sliders.interior_defense),
                                                                My_ROC_Team.Stat_upgrader("Perimeter\nDefense",My_ROC_Team.Stat_upgrader.Sliders.perimeter_defense),
                                                                My_ROC_Team.Stat_upgrader("Speed",My_ROC_Team.Stat_upgrader.Sliders.speed),
                                                                My_ROC_Team.Stat_upgrader("Stamina",My_ROC_Team.Stat_upgrader.Sliders.stamina),
                                                                My_ROC_Team.Stat_upgrader("Strength",My_ROC_Team.Stat_upgrader.Sliders.strength),
                                                            ],spacing=0,scroll=ft.ScrollMode.AUTO,expand=True,)
                                                        )
                                                    )],expand=True,spacing=0),

                                                        

                                                ],spacing=0,expand=True)
                                            ),
                                            
                                            
                                        ],expand=True),
                                       
                                    ])

                                )
                            ),  
                        ],spacing=0,expand=True)
                    ],spacing=0)
           
            ) 
   
    class Settings:
        def settings():
            print(f"{page.route} Menu item clicked")
            return ft.Container(
                width=page.window_width,
                height=page.window_height,
                margin=10,
                border_radius=10,
                border=ft.border.all(2, ft.colors.WHITE24),
                alignment=ft.alignment.center,
                bgcolor=ft.colors.BLACK12,
                expand=True,
                content=(ft.Text(
                    "Settings",
                    size=50,
                    color=ft.colors.with_opacity(0.5,ft.colors.WHITE),
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                    )),
                )


    def route_change(route):
        page.drawer = False
        page.views.clear()
       
        page.views.append(

        ft.View(
            "/",
            [   
                ft.Row ([
                ft.Row(alignment="top_left", spacing=25, controls=[Main_menu.management_window()],expand=True),
                  #Main_dashboard
                ],
                expand=True)
            ],
            
            )
        )
        if page.route == "/Login":
            page.views.append(
                ft.View(
                    "/Login",
                    [
                        ft.Row ([ 
                        ft.Row(alignment="top_left", spacing=25, controls=[Main_menu.management_window()],expand=True),
                        ],expand=True)
                    ],  
                   
                )
            )
        
    
        if page.route == "/Dashboard":
            page.views.append(
                ft.View(
                    "/Dashboard",
                    [
                        
                        ft.Row ([ 
                        ft.Row(alignment="top_left", spacing=25, controls=[Main_menu.side_menu(),Dashboard.dashboard()],expand=True),
                        ],expand=True)
                    ],
                  

                )    
            )    
        
        if page.route == "/Sim Game":
            page.views.append(
                ft.View(
                    "/Sim Game",
                    [
                        ft.Row ([ 
                        ft.Row(alignment="top_let", spacing=25, controls=[Main_menu.side_menu(),Sim_game.sim_game()],expand=True),
                        ],expand=True)
                    ],
                     
                )
            )

        if page.route == "/Online PvP":
            page.views.append(
                ft.View(
                    "/Online PvP",
                    [
                        ft.Row ([ 
                        ft.Row(alignment="top_let", spacing=25, controls=[Main_menu.side_menu(),Online_pvp.online_pvp()],expand=True),
                        ],expand=True)
                    ],
                   
                )
            )
        if page.route == "/The Roc":
            page.views.append(
                ft.View(
                    "/The Roc",
                    [
                        ft.Row ([ 
                        ft.Row(alignment="top_left", spacing=25, controls=[Main_menu.side_menu(),The_Roc.the_Roc()],expand=True),
                        ],expand=True)
                    ],
                    
                )
            )
        
        if page.route == "/Player Search":
            page.views.append(
                ft.View(
                    "/Player Search",
                    [
                        ft.Row ([ 
                        ft.Row(alignment="top_let", spacing=25, controls=[Main_menu.side_menu(),Player_search.player_search_menu()],expand=True),
                        ],expand=True)
                    ],
                   
                )
            )
        if page.route == "/MY R.O.C Team":
            page.views.append(
                ft.View(
                    "/MY R.O.C Team",         
                    [
                        ft.Row ([ 
                        ft.Row(alignment="top_let", spacing=25, controls=[Main_menu.side_menu(),My_ROC_Team.my_roc_team()],expand=True),
                        ],expand=True)
                    ],
                    
                )
            )
        if page.route == "/Settings":
            page.views.append(
                ft.View(
                    "/Settings",
                    [
                        ft.Row ([ 
                        ft.Row(alignment="top_let", spacing=25, controls=[Main_menu.side_menu(),Settings.settings()],expand=True),
                        ],expand=True)
                    ],
                      
                )
            )
        page.update()
            
    def page_resive(e):
        page.go(f"'{page.route}'")
       
   
    print(page.route)
    page.update()
    page.on_route_change = route_change
    page.go(page.route)



ft.app(target=main)#

