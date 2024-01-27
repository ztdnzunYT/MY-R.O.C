import flet as ft
from Player_database_connector import*

def main(page: ft.Page):
    page.horizontal_alignment=ft.MainAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    
    page.add(
        ft.Container(
            width=page.width,
            height=page.height,
            margin=5,
            border_radius=10,
            border=ft.border.all(2, ft.colors.WHITE24),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.BLACK12,
            content=ft.Column([

                ft.OutlinedButton(
                ),

    
                ]),expand=True
            ),
           ),
    
    


    page.__on_page_change_event = print("event")


ft.app(target=main) 