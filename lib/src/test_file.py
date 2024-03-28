from time import sleep
import flet as ft

def main(page: ft.Page):
    pr = ft.ProgressRing(width=40, height=40, stroke_width = 1,)

    page.add(
        ft.Container(
            width=page.width,
            height=page.height,
            alignment=ft.alignment.center,
            expand=True,
            content=pr
        )
      

            
        
    )



ft.app(target=main)