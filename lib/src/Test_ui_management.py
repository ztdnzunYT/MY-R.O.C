import flet as ft
from Player_database_connector import*

def main(page: ft.Page):
    page.horizontal_alignment=ft.MainAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    
    def management_window():
        return ft.Container(
            width=page.width,
            height=page.height,
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
                            alignment=ft.alignment.center_left,
                            content=ft.TextButton(text="New Management",disabled=False,)
                        ),
                        ft.Container(
                            width=160,
                            height=30,
                            bgcolor=ft.colors.TRANSPARENT,
                            alignment=ft.alignment.center_left,
                            content=ft.TextButton(text="Load Management",disabled=False)
                        )],
                        spacing=15,
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
            ), 
            expand=True,
            alignment=ft.alignment.center
            )



        
    page.add(management_window())
           
    
    


    page.__on_page_change_event = print("event")


ft.app(target=main) 