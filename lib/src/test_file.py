
import flet as ft
import random

def main(page: ft.Page):
    page.bgcolor= ft.colors.AMBER_600


    class players:

        player_size = 40
        player_speed = 600

        c1 = ft.Container(alignment=ft.alignment.center,width=player_size, height=player_size, bgcolor="red", animate_position=player_speed,shape=ft.BoxShape.CIRCLE,content=ft.Text("PG",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.W_500))

        c2 = ft.Container(
            alignment=ft.alignment.center,width=player_size, height=player_size, bgcolor="green", top=60, left=0, animate_position=player_speed,shape=ft.BoxShape.CIRCLE,content=ft.Text("SF",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.W_500)
        )

        c3 = ft.Container(
            alignment=ft.alignment.center,width=player_size, height=player_size, bgcolor="blue", top=120, left=0, animate_position=player_speed,shape=ft.BoxShape.CIRCLE,content=ft.Text("C",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.W_500)
        )


    def animate_container(e):
        players.c1.top = random.randint(0,200)
        players.c1.left = random.randint(0,200)
        players.c2.top = random.randint(0,200)
        players.c2.left = random.randint(0,200)
        players.c3.top = random.randint(0,200)
        players.c3.left = random.randint(0,200)
        page.update()


    s = ft.Stack([players.c1, players.c2, players.c3], height=250)
    b =ft.ElevatedButton("Animate!", on_click=animate_container)

    page.add(s,b
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
