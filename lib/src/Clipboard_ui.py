import flet as ft

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
            bgcolor=ft.colors.BLACK12,
            alignment=ft.alignment.center,
            content=ft.Container(
                width=350,
                height=470,
                border_radius=20,
                bgcolor='#7C4700',
                alignment=ft.alignment.center,
                content=ft.Container(
                    width=300,
                    height=410,
                    bgcolor=ft.colors.WHITE,
                    padding=-17,
                    alignment=ft.alignment.center,
                    content=ft.Column([
                        
                        
                    ft.Container(
                        width=80,
                        height=40,
                        col=6,
                        border_radius=ft.border_radius.only(bottom_left=20,bottom_right=20),
                        bgcolor=ft.colors.TRANSPARENT,
                        border=ft.border.all(9,color=ft.colors.GREY),
                    
                    ),
                
               ],),
            ),
            ))
    )
          





ft.app(target=main,port=4556) 