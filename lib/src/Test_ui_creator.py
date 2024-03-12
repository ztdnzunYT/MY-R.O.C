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
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    print(page.width,page.height)
    page.window_frameless = False
    page.window_width=1050
    page.window_min_height=690
    page.window_min_width=1000
    page.window_center()

    class new_or_load_management():

        
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
        
        
        


    class Main_menu():
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
        
            
    class Dashboard():
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
        my_team_score_display =  ft.Text(text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.W_500,value=0,size=15)
        ai_team_score_display =  ft.Text(text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.W_500,value=0,size=15)
        play = Game_sim.play_choice
        game_speed_slider = ft.Slider(value=1,min=0.04,max=3,divisions=3,width=300,active_color=ft.colors.WHITE70,label=" Gamespeed: {value}% ",
                                        on_change=lambda e: print(round(e.control.value),3))
        
        player_size = 35
        player_speed = 600
        court_horizontal_range = [60,280]
        court_vertical_range = [15,200]


        image_png = ft.Image( src="lib\\assets\\images\\basketball-half-court-parquet-600nw-122537710.png",width=380,height=380,scale=.9,fit=ft.ImageFit.COVER,
                                repeat=ft.ImageRepeat.NO_REPEAT,border_radius=ft.border_radius.all(5),expand=True)

        court_player_1 = ft.Container(width=player_size,height=player_size,shape=ft.BoxShape.CIRCLE,bgcolor=ft.colors.BLUE,animate_position=player_speed,
                                      alignment=ft.alignment.center,bottom=random.randint(min(court_vertical_range),max(court_vertical_range)),left=random.randint(min(court_horizontal_range),max(court_horizontal_range)),content=(ft.Text("PG",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.W_500,color=ft.colors.WHITE)))
        court_player_2 = ft.Container(width=player_size,height=player_size,shape=ft.BoxShape.CIRCLE,bgcolor=ft.colors.AMBER_600,animate_position=player_speed,
                                      alignment=ft.alignment.center,top=random.randint(min(court_vertical_range),max(court_vertical_range)),left=random.randint(min(court_horizontal_range),max(court_horizontal_range)),content=(ft.Text("SF",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.W_500,color=ft.colors.WHITE)))
        court_player_3 = ft.Container(width=player_size,height=player_size,shape=ft.BoxShape.CIRCLE,bgcolor=ft.colors.GREEN,animate_position=player_speed,
                                      alignment=ft.alignment.center,top=random.randint(min(court_vertical_range),max(court_vertical_range)),left=random.randint(min(court_horizontal_range),max(court_horizontal_range)),content=(ft.Text("C",text_align =ft.TextAlign.CENTER,weight=ft.FontWeight.W_500,color=ft.colors.WHITE)))
        



         #,height=300)


        

        court_image = ft.Container(
            expand=True,
            content=(
                ft.Stack([
                    image_png,
                    court_player_1,
                    court_player_2,
                    court_player_3
                ])
            )
        )
        

        court = ft.Container(
            width=page.window_width,
            height=page.window_height/2.7,
            alignment=ft.alignment.center,
            content=(
                court_image
            )
        )
        
        
                
        


        def new_log_entry():
            print(Sim_game.image_png.width,Sim_game.image_png.height)
            my_team_score = 0
            ai_team_score = 0
            Sim_game.my_team_score_display.value = 0
            Sim_game.ai_team_score_display.value = 0
            Sim_game.my_team_score_display.color = ft.colors.WHITE
            Sim_game.ai_team_score_display.color = ft.colors.WHITE
            Sim_game.lv.controls.clear()
            
            for i in range(len(Sim_game.play)):
                time.sleep(round(Sim_game.game_speed_slider.value,3))
                Sim_game.lv.controls.append(ft.Text(f"{Sim_game.play[i]}",color=ft.colors.WHITE,weight=ft.FontWeight.W_500))
                if "MY TEAM SCORE :" in Sim_game.play[i]:
                    my_team_score_list = []
                    for o in range(len(Sim_game.play[i])):
                        if (str(Sim_game.play[i][o])).isdigit(): 
                            my_team_score_list.append(Sim_game.play[i][o])
                            if len(my_team_score_list) == 1:
                                my_team_score = (my_team_score_list[0])
                            else:
                                my_team_score = (my_team_score_list[0] + my_team_score_list[1])
                    Sim_game.my_team_score_display.value = my_team_score
                if int(my_team_score) >= Game_stats.wining_score:
                    Sim_game.my_team_score_display.color = ft.colors.LIGHT_GREEN_ACCENT_400
                    Sim_game.ai_team_score_display.color = ft.colors.RED
                if "AI SCORE :" in Sim_game.play[i]:
                    ai_team_score_list = []
                    for o in range(len(Sim_game.play[i])):
                        if (str(Sim_game.play[i][o])).isdigit(): 
                            ai_team_score_list.append(Sim_game.play[i][o])
                            if len(ai_team_score_list) == 1 :
                                ai_team_score = (ai_team_score_list[0])
                            else:
                                ai_team_score = (ai_team_score_list[0] + ai_team_score_list[1])
                    Sim_game.ai_team_score_display.value = ai_team_score
                if int(ai_team_score) >= Game_stats.wining_score:
                    Sim_game.ai_team_score_display.color = ft.colors.LIGHT_GREEN_ACCENT_400
                    Sim_game.my_team_score_display.color = ft.colors.RED

                page.update()
            Sim_game.play.clear()
            start_sim()
      
        
        def sim_game():
            
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
                                                        ft.Switch(label=" Fullscreen",value=True,scale=.7,active_color=ft.colors.BACKGROUND)
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
                                                ft.Stack([
                                                   Sim_game.court,
                                                   
                                                ])
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
                                        border_radius=10,
                                        margin=ft.margin.only(top=10,bottom=20,right=30,left=30),
                                        bgcolor=ft.colors.BLACK26,
                                        alignment=ft.alignment.center_left,
                                        expand=True,
                                        content=(
                                            ft.Row([
                                                ft.Container(
                                                width=page.width,
                                                height=page.height/3,
                                                margin=ft.margin.only(top=15,bottom=15,right=5,left=20),
                                                alignment=ft.alignment.center,
                                                border_radius=5,
                                                bgcolor=ft.colors.WHITE24,
                                                expand=True,
                                                content=(
                                                    ft.Column([
                                                        ft.Row([
                                                            ft.Text("MY TEAM",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,size=17,color=ft.colors.WHITE,expand=True),
                                                        ],alignment=ft.MainAxisAlignment.CENTER,expand=True),
                                                        ft.Divider(color=ft.colors.BLACK38,thickness=2),
                                                        ft.Row([
                                                            ft.Text("AI TEAM 1",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD,size=17,color=ft.colors.WHITE)
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
        
    class The_Roc():
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


    class Player_search():

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
                ft.DataColumn(ft.Text(f"Id",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD),tooltip="Player row id"),
                ft.DataColumn(ft.Text(f"",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"First name",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Last name",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Age",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Height",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Weight",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"★ Rating",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Position",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Build",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Moral",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Trait",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Team name",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Skill set",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD),tooltip="Players with specific skill sets\ncan recieve attribute boosts"),
                ft.DataColumn(ft.Text(f"Injured",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Recovery days",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Potential",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Overall",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Offense",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Defense",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Roots",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Three pointer",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Midrange",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Layup",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Dunk",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Ball handle",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Speed",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Stamina",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Passing",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Strength",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Rebounding",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Interior defense",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Perimeter defense",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Steal",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Block",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Points",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Assists",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Rebounds",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Steals",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Blocks",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Turnovers",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Games played",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Points per game",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Assists per game",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Steals per game",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Blocks per game",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Rebounds per game",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Turnovers per game",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Field goal %",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Three point %",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f""))
            ],
            rows=[
                #color=ft.colors.with_opacity(0.3,ft.colors.WHITE),
            ],
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
                if i == 5:
                    new_row.cells[i] = (ft.DataCell(ft.Text(f"{player_info[i-1]} ft")))
                if i == 6: 
                    new_row.cells[i] = (ft.DataCell(ft.Text(f"{player_info[i-1]} lb")))
                if i == 6:
                    new_row.cells.append(ft.DataCell(ft.Text(f"{(int(player_info[i]) * "★")}")))
                if i == 15:
                    new_row.cells[i] = (ft.DataCell(ft.Text(f"{player_info[i-1]} dys")))
                if i == 16:
                    new_row.cells[i] = (ft.DataCell(ft.Text(f"{player_info[i-1]} pot")))
                if i == 17:
                    new_row.cells[i] = (ft.DataCell(ft.Text(f"{player_info[i-1]} ovr")))
                if i == 18:
                    new_row.cells[i] = (ft.DataCell(ft.Text(f"{player_info[i-1]} off")))
                if i == 19:
                    new_row.cells[i] = (ft.DataCell(ft.Text(f"{player_info[i-1]} def")))
                if i == 21:
                    new_row.cells[i] = (ft.DataCell(ft.Text(f"{player_info[i-1]} three")))
                if i == 22:
                    new_row.cells[i] = (ft.DataCell(ft.Text(f"{player_info[i-1]} midr")))
                if i == 23:
                    new_row.cells[i] = (ft.DataCell(ft.Text(f"{player_info[i-1]} lay")))
                if i == 24:
                    new_row.cells[i] = (ft.DataCell(ft.Text(f"{player_info[i-1]} dnk")))
                if i == 25:
                    new_row.cells[i] = (ft.DataCell(ft.Text(f"{player_info[i-1]} handle")))
                if i == 26:
                    new_row.cells[i] = (ft.DataCell(ft.Text(f"{player_info[i-1]} speed")))
                if i == 27:
                    new_row.cells[i] = (ft.DataCell(ft.Text(f"{player_info[i-1]} stam")))
                if i == 28:
                    new_row.cells[i] = (ft.DataCell(ft.Text(f"{player_info[i-1]} passing")))
                if i == 29:
                    new_row.cells[i] = (ft.DataCell(ft.Text(f"{player_info[i-1]} strength")))
                if i == 30:
                    new_row.cells[i] = (ft.DataCell(ft.Text(f"{player_info[i-1]} rebound")))
                if i == 31:
                    new_row.cells[i] = (ft.DataCell(ft.Text(f"{player_info[i-1]} int d")))
                if i == 32:
                    new_row.cells[i] = (ft.DataCell(ft.Text(f"{player_info[i-1]} per d")))
                if i == 33:
                    new_row.cells[i] = (ft.DataCell(ft.Text(f"{player_info[i-1]} stl")))
                if i == 34:
                    new_row.cells[i] = (ft.DataCell(ft.Text(f"{player_info[i-1]} blk")))
                if i == 35:
                    new_row.cells[i] = (ft.DataCell(ft.Text(f"{player_info[i-1]} pts")))
                if i == 36:
                    new_row.cells[i] = (ft.DataCell(ft.Text(f"{player_info[i-1]} asts")))
                if i == 37:
                    new_row.cells[i] = (ft.DataCell(ft.Text(f"{player_info[i-1]} rebs")))
                if i == 38:
                    new_row.cells[i] = (ft.DataCell(ft.Text(f"{player_info[i-1]} stls")))
                if i == 39:
                    new_row.cells[i] = (ft.DataCell(ft.Text(f"{player_info[i-1]} blks")))
                if i == 40:
                    new_row.cells[i] = (ft.DataCell(ft.Text(f"{player_info[i-1]} trnvrs")))
                if i == 41:
                    new_row.cells[i] = (ft.DataCell(ft.Text(f"{player_info[i-1]} games played")))
                if i == 42:
                    new_row.cells[i] = (ft.DataCell(ft.Text(f"{player_info[i-1]} ppg")))
                if i == 43:
                    new_row.cells[i] = (ft.DataCell(ft.Text(f"{player_info[i-1]} apg")))
                if i == 44:
                    new_row.cells[i] = (ft.DataCell(ft.Text(f"{player_info[i-1]} spg")))
                if i == 45:
                    new_row.cells[i] = (ft.DataCell(ft.Text(f"{player_info[i-1]} bpg")))
                if i == 46:
                    new_row.cells[i] = (ft.DataCell(ft.Text(f"{player_info[i-1]} rpg")))
                if i == 47:
                    new_row.cells[i] = (ft.DataCell(ft.Text(f"{player_info[i-1]} tpg")))
                if i == 48:
                    new_row.cells[i] = (ft.DataCell(ft.Text(f"{player_info[i-1]} fg%")))
                if i == 49:
                    new_row.cells[i] = (ft.DataCell(ft.Text(f"{player_info[i-1]} 3pt%")))
                
                if  i > 0 and i != 6:
                    new_row.cells.append(ft.DataCell(ft.Text(f"{player_info[i]}")))
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
        

    class Online_pvp():
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


    class My_ROC_Team():
        def my_roc_team():
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
                    "MY R.O.C Team",
                    size=50,
                    color=ft.colors.with_opacity(0.5,ft.colors.WHITE),
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                    )),
                expand=True)

    class Settings():
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
                content=(ft.Text(
                    "Settings",
                    size=50,
                    color=ft.colors.with_opacity(0.5,ft.colors.WHITE),
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                    )),
                expand=True)



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
            
    def page_resive(e):
        page.go(f"'{page.route}'")
       

    page.update()
    page.on_route_change = route_change

    page.go(page.route)
    


ft.app(target=main)

