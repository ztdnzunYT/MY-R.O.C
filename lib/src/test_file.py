import flet as ft

def main(page: ft.Page):
    page.title = "Basic elevated buttons"
    page.add(
        ft.ElevatedButton(text="Elevated button",bgcolor=ft.colors.GREY_800,color=ft.colors.WHITE),
        ft.ElevatedButton("Disabled button", disabled=True,bgcolor=ft.colors.BLACK38),
    )

ft.app(target=main)