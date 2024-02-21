import flet as ft

def main(page: ft.Page):

    class Main_menu():
        def side_menu():
            return ft.Row(
                [
                    ft.Container(  
                        expand=False,
                        width=110,
                        height=page.window_height,
                        margin=10,
                        border_radius= 10,
                        border=ft.border.all(2, ft.colors.WHITE24),
                        bgcolor=ft.colors.BLACK12,
                        alignment=ft.alignment.top_center,
                        content=ft.Container(
                            ft.Column(
                                alignment=ft.alignment.center,
                                scroll=ft.ScrollMode.AUTO,
                                controls=
                            [
                                ft.IconButton(
                                    icon=ft.icons.SPACE_DASHBOARD,
                                    icon_color=ft.colors.WHITE60, 
                                    icon_size=50,
                                    tooltip="Dashboard",
                                    on_click=lambda _: page.go("/Dashboard"),
                                ), 
                                ft.IconButton(
                                    icon=ft.icons.SCOREBOARD,
                                    icon_color=ft.colors.WHITE60,
                                    icon_size=50,
                                    tooltip="Sim Game",
                                    on_click=lambda _: page.go("/Sim Game")
                                ),
                                ft.IconButton(
                                    icon=ft.icons.CONNECT_WITHOUT_CONTACT,
                                    icon_color=ft.colors.WHITE60,
                                    icon_size=50,
                                    tooltip="Online PVP",
                                    on_click=lambda _: page.go("/Online PvP")
                                ),
                                ft.IconButton(
                                    icon = ft.icons.SPORTS_BASKETBALL,
                                    icon_color=ft.colors.WHITE60,
                                    icon_size=45,
                                    tooltip="The R.O.C",
                                    on_click=lambda _: page.go("/The Roc")
                                ),
                                ft.IconButton(
                                    icon=ft.icons.PERSON_SEARCH_ROUNDED,
                                    icon_color=ft.colors.WHITE60,
                                    icon_size=50,
                                    tooltip="Player Search",
                                    on_click=lambda _: page.go("/Player Search")
                                ),
                                ft.IconButton(
                                    icon=ft.icons.MANAGE_ACCOUNTS,
                                    icon_color=ft.colors.WHITE60,
                                    icon_size=50,
                                    tooltip="My R.O.C Team",
                                    on_click=lambda _: page.go("/MY R.O.C Team")
                                ),
                                ft.IconButton(
                                    icon=ft.icons.SETTINGS_SHARP,
                                    icon_color=ft.colors.WHITE60,
                                    icon_size=45,
                                    tooltip="Settings",
                                    on_click=lambda _: page.go("/Settings")
                                ),
                                ft.IconButton(
                                    icon=ft.icons.LOGIN,
                                    icon_color=ft.colors.WHITE60,
                                    icon_size=40,
                                    tooltip="Logout",
                                    on_click=lambda _: page.go("/"),
                                ),
                                #ACCOUNT_CIRCLE_ROUNDED
                                #icons.LIST_ALT_ROUNDED
                            ]), 
                        margin=10,)
                    ),
                ],
                expand=False     
                )

    class Dashboard():
        def dashboard():
            print(f"{page.route} Menu item clicked")
            return ft.Container(
                width=page.window_width,
                height=page.window_height,
                margin=5,
                border_radius=10,
                border=ft.border.all(2, ft.colors.WHITE24),
                alignment=ft.alignment.center,
                bgcolor=ft.colors.TRANSPARENT,
                
                content=ft.Row([
                    ft.Tabs(
                        unselected_label_color=ft.colors.WHITE54, 
                        label_color=ft.colors.WHITE,
                        indicator_color=ft.colors.WHITE,
                        height=page.window_height -50,
                        width=page.window_width -200,
                        selected_index = 0,
                        animation_duration=300,
                        expand=True,

                        tabs=[
                            ft.Tab(
                                text="HOME",
                                tab_content=ft.Text("HOME",size=20),
                                content=ft.Container(
                                    alignment=ft.alignment.center,
                                    margin=20,
                                    border_radius=15,
                                    expand=False,
                                    content=ft.Row([
                                        ft.Column([
                                            ft.Container(
                                                padding=10,
                                                bgcolor=ft.colors.WHITE38,
                                                alignment=ft.alignment.center,
                                                margin=10,
                                                border_radius=5,
                                                expand=True,
                                                ink=True,
                                                on_click=lambda e: print("Clickable with Ink clicked!"),
                                                content=ft.Text("QUICK GAME",size=60,color=ft.colors.WHITE,weight=ft.FontWeight.BOLD,expand=False,text_align=ft.TextAlign.CENTER,italic=True,max_lines=3),
                                                ),
                                            ft.Container(
                                                padding=10,
                                                bgcolor=ft.colors.WHITE38,
                                                alignment=ft.alignment.center,
                                                margin=10,
                                                border_radius=5,
                                                expand=True,
                                                ink=True,
                                                on_click=lambda e: print("Clickable with Ink clicked!"),
                                                content=ft.Text("ONLINE PVP",size=60,color=ft.colors.WHITE,weight=ft.FontWeight.BOLD,expand=False,text_align=ft.TextAlign.CENTER,italic=True,max_lines=3),
                                                ),
                                            ft.Container(
                                                padding=10,
                                                bgcolor=ft.colors.WHITE38,
                                                alignment=ft.alignment.center,
                                                margin=10,
                                                border_radius=5,
                                                expand=True,
                                                ink=True,
                                                on_click=lambda e: print("Clickable with Ink clicked!"),
                                                content=ft.Text("MY SEASON",size=60,color=ft.colors.WHITE,weight=ft.FontWeight.BOLD,expand=False,text_align=ft.TextAlign.CENTER,italic=True,max_lines=3),
                                                ),
                                        ],alignment=ft.MainAxisAlignment.CENTER,spacing=10,expand=True),
                                        
                                        ft.Column([

                                            ft.Container(
                                                width=page.window_width,  
                                                height = page.window_height/2.5,
                                                padding=10,
                                                bgcolor=ft.colors.WHITE38,
                                                alignment=ft.alignment.top_center,
                                                margin=10,
                                                border_radius=5,
                                                expand=True,
                                                content=ft.Column([
                                                ft.Container(
                                                    bgcolor=ft.colors.TRANSPARENT,
                                                    alignment=ft.alignment.center,
                                                    content=ft.Text(
                                                    "SOCIAL MEDIA",
                                                    size=20,
                                                    text_align=ft.TextAlign.CENTER,
                                                    weight=ft.FontWeight.BOLD,
                                                    color=ft.colors.WHITE,
                                                    italic=True,
                                                    ),
                                                ),
                                                ft.Container(
                                                    bgcolor=ft.colors.WHITE10,
                                                    expand=True,
                                                    margin=5,
                                                    border_radius=10
                                                    )
                                                ],alignment=ft.CrossAxisAlignment.CENTER)
                                                ),
                                                
                                        ft.Container(width=page.window_width,
                                                height = page.window_height/4,
                                                bgcolor=ft.colors.WHITE38,
                                                alignment=ft.alignment.center,
                                                margin=10,
                                                border_radius=5,
                                                expand=True),
                                        ],expand=True,spacing=5,alignment=ft.alignment.center)
                                    ],alignment=ft.alignment.center,expand=True,spacing=5),
                                )
                            ),
                            ft.Tab(
                                text="MY R.O.C",
                                tab_content=ft.Text("THE R.O.C",size=20),
                                content=ft.Text("MY R.O.C")
                            ),
                            ft.Tab(
                                text="ROSTER",
                                tab_content=ft.Text("ROSTER",size=20),
                                content=ft.Text("ROSTER")
                            ),
                            ft.Tab(
                                text="STATS",
                                tab_content=ft.Text("STATS",size=20),
                                content=ft.Text("STATS")
                            ),
                            ft.Tab(
                                text="SETTINGS",
                                tab_content=ft.Text("SETTINGS",size=20),
                                content=ft.Text("SETTINGS")
                            ),
                            ft.Tab(
                                text="ACCOUNT",
                                tab_content=ft.Text("ACCOUNT",size=20),
                                content=ft.Text("ACCOUNT")
                            ),]
                            ,)]) ,expand=True
                            )
                            
                

    page.add(Dashboard.dashboard())

ft.app(target=main)