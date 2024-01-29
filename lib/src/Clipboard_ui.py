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
                    alignment=ft.alignment.center,
                    content=ft.Column([
                    ft.Container(
                        padding=-19,
                        width=300,
                        height=20,
                        bgcolor=ft.colors.WHITE,
                        alignment=ft.alignment.top_center,
                        content= ft.Container(
                        width=80,
                        height=40,
                        border_radius=ft.border_radius.only(bottom_left=20,bottom_right=20),
                        bgcolor=ft.colors.TRANSPARENT,
                        border=ft.border.all(9,color=ft.colors.GREY),),
            
                    ),
                    ft.Container(
                        width=300,
                        height=370,
                        bgcolor=ft.colors.TRANSPARENT,
                        alignment=ft.alignment.center,
                        content=ft.Column([
                            ft.Text("MY R.O.C",size=50,weight=ft.FontWeight.BOLD,color=ft.colors.GREY),
                            ft.Column([
                                ft.Container(
                                width=160,
                                height=30,
                                bgcolor=ft.colors.TRANSPARENT,
                                alignment=ft.alignment.center_left,
                                content=ft.TextButton(
                                    text="New Management",
                                    disabled=False,
                                    on_click=lambda _: page.go("/"),
                                    )
                            ),
                            ft.Container(
                                width=160,
                                height=30,
                                bgcolor=ft.colors.TRANSPARENT,
                                alignment=ft.alignment.center_left,
                                content=ft.TextButton(
                                    text="Load Management",
                                    disabled=False,
                                    on_click=lambda _: page.go("/Dashboard"))
                            )],
                            )],
                            spacing=60,
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                    )
                ])
            )
            ),expand=True
        )
            )

     





ft.app(target=main,port=4556) 