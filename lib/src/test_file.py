import flet as ft

def main(page: ft.Page):



    normal_radius = 100
    normal_title_style = ft.TextStyle(size=20, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD)

    finishing = ft.PieChartSection(
        value=25,
        title="Finishing",
        title_style = normal_title_style,
        color=ft.colors.BLUE,
       
    )
    shooting = ft.PieChartSection(
        value=25,
        title="Shooting",
        title_style = normal_title_style,
        color=ft.colors.LIGHT_GREEN_ACCENT_400,

    )
    playmaking = ft.PieChartSection(
        value=25,
        title="Playmaking",
        title_style = normal_title_style,
        color=ft.colors.ORANGE,

    )
    defense = ft.PieChartSection(
        value=25,
        title="Defense",
        title_style = normal_title_style,
        color=ft.colors.RED,
    
    )    

    chart = ft.PieChart(
        sections=[
        defense,
        playmaking,
        finishing,
        shooting,
        ],sections_space=0,
        center_space_radius=100,
        expand=True
    )

    


    page.add(
        chart)

ft.app(main)