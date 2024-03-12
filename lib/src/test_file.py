
import flet as ft
import random

def main(page: ft.Page):
    page.bgcolor= ft.colors.BACKGROUND


    class players:

        player_size = 35
        player_speed = 600

        c1 = ft.Container(alignment=ft.alignment.center,width=player_size, height=player_size, bgcolor="red", animate_position=player_speed,shape=ft.BoxShape.CIRCLE,content=ft.Text("PG",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.W_500))

        c2 = ft.Container(
            alignment=ft.alignment.center,width=player_size, height=player_size, bgcolor="green", bottom=-100, left=0, animate_position=player_speed,shape=ft.BoxShape.CIRCLE,content=ft.Text("SF",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.W_500)
        )

        c3 = ft.Container(
            alignment=ft.alignment.center,width=player_size, height=player_size, bgcolor="blue", bottom=-100, left=0, animate_position=player_speed,shape=ft.BoxShape.CIRCLE,content=ft.Text("C",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.W_500)
        )

    s = ft.Stack([players.c1, players.c2, players.c3], height=240,width=240)

    court_pic = ft.Image(
        src="lib\\assets\\images\\basketball-half-court-parquet-600nw-122537710.png",
        width=380,
        height=380,
        scale=.9,
        fit=ft.ImageFit.COVER,
        repeat=ft.ImageRepeat.NO_REPEAT,
        border_radius=ft.border_radius.all(5),
    )

    court_container = ft.Container(
        width=page.window_width,
        height=page.window_height/2.7,
        border_radius=2,
        margin=ft.margin.only(top=5,bottom=0,right=30,left=30),
        bgcolor=ft.colors.BACKGROUND,
        border=ft.border.all(2,ft.colors.BLACK26),
        alignment=ft.alignment.center,
        
        content=(
            ft.Stack([
                court_pic,
                s
            ])
        )
        
    )




    court = ft.Container(
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
                                    ft.Row([
                                        ft.Container(
                                            alignment=ft.alignment.center,
                                            bgcolor=ft.colors.BLACK26,
                                            width=100,
                                            height=30,
                                            margin=ft.margin.only(top=15),
                                            border_radius=2,
                                            content=ft.Container(
                                                content=
                                                ft.Stack([
                                                    ft.Container(
                                                        margin=ft.margin.only(top=5,right=50),
                                                        content=
                                                        ft.Row([
                                      
                                                        ],alignment=ft.MainAxisAlignment.CENTER,spacing=37,vertical_alignment=ft.alignment.center),
                                                    ),
                                                    ft.Container(
                                                        margin=ft.margin.only(top=5,left=50),
                                                        content=
                                                        ft.Row([
                                        
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
                                            )
                                            ),  
                                        ],vertical_alignment=ft.alignment.center,alignment=ft.MainAxisAlignment.CENTER
                                        ),

                                        court_container,

               

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
                
                                        ],alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.alignment.center)
                                    )
                                )
                            )    
                        ),

                    ], alignment=ft.MainAxisAlignment.CENTER,
                
                    )
                    
                    
                    ),
                expand=True)
    



    def animate_container(e):
        print(court_container.height)
        players.c1.bottom = random.randint(0,int(court_container.height-60))
        players.c1.left = random.randint(0,200)
        players.c2.bottom = random.randint(0,int(court_container.height-60))
        players.c2.left = random.randint(0,200)
        players.c3.bottom = random.randint(0,int(court_container.height-60))
        players.c3.left = random.randint(0,200)
        
        page.update()


    
    b =ft.ElevatedButton("Animate!", on_click=animate_container)

    page.add(court,b
    )

ft.app(target=main)


















































































"""
        c1 = ft.Container(width=50, height=50, bgcolor="red", animate_position=1000)

        c2 = ft.Container(
            width=50, height=50, bgcolor="green", top=60, left=0, animate_position=500
        )

        c3 = ft.Container(
            width=50, height=50, bgcolor="blue", top=120, left=0, animate_position=1000
        )

        def animate_container(e):
            c1.top = 20
            c1.left = 200
            c2.top = 100
            c2.left = 40
            c3.top = 180
            c3.left = 100
            page.update()

        page.add(
            court,
            ft.Stack([c1, c2, c3], height=250),
            ft.ElevatedButton("Animate!", on_click=animate_container),
        )
    """
