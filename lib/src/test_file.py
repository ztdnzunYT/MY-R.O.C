
import flet as ft
import random

def main(page: ft.Page):
    def button_clicked(e):
        t.value = (
            f"Switch values are:  {c1.value}, {c2.value}, {c3.value}, {c4.value}."
        )
        page.update()

    t = ft.Text()
    c1 = ft.Switch(label="Unchecked switch", value=False)
    c2 = ft.Switch(label="Checked switch", value=True)
    c3 = ft.Switch(label="Disabled switch", disabled=True)
    c4 = ft.Switch(
        label="Switch with rendered label_position='left'", label_position=ft.LabelPosition.LEFT
    )
    b = ft.ElevatedButton(text="Submit")
    page.add(c1, c2, c3, c4, b, t)

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
