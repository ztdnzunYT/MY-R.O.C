import flet as ft
from Player_database_connector import*
import time

class new_or_load_management():
    def is_database_tables_created():
        mycursor.execute("SELECT name FROM sqlite_schema WHERE TYPE='tables'")
        databases = mycursor.fetchall()
        print(databases)
        return databases
        '''
        if (len() of variable assigned to fetch tables in database == 0):
            return ft.outlinedbutton(text=“New Game”) 
        else: 
            return ft.outlinedbutton(text=“load game”)  
        '''



def main(page: ft.Page):
    
    page.title = "MY R.O.C MANAGER"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_frameless = False


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
                                alignment=ft.alignment.top_center,
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
        
        def default_menu_backdrop():
            return ft.Container(
                width=page.window_width,
                height=page.window_height,
                margin=5,
                border_radius=10,
                border=ft.border.all(2, ft.colors.WHITE24),
                alignment=ft.alignment.center,
                bgcolor=ft.colors.BLACK12,
                content=(ft.Text(
                    "MY R.O.C",
                    size=50,
                    color=ft.colors.with_opacity(0.5,ft.colors.WHITE),
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                    )),
                expand=True)
                
        def management_window():
            return ft.Container(
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
                            spacing=15,
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                ), 
                expand=True,
                alignment=ft.alignment.center
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
                bgcolor=ft.colors.BLACK12,
                content=(ft.Text(
                    "Dashboard",
                    size=50,
                    color=ft.colors.with_opacity(0.5,ft.colors.WHITE),
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                    )),
                expand=True)

    class Sim_game():
        def sim_game():
            print(f"{page.route} Menu item clicked")
            return ft.Container(
                width=page.window_width,
                height=page.window_height,
                margin=5,
                border_radius=10,
                border=ft.border.all(2, ft.colors.WHITE24),
                alignment=ft.alignment.center,
                bgcolor=ft.colors.BLACK12,
                content=(ft.Text(
                    "Sim Game",
                    size=50,
                    color=ft.colors.with_opacity(0.5,ft.colors.WHITE),
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                    )),
                expand=True)
        

    class Player_search():
        table = ft.DataTable(
            column_spacing=80,
            data_row_max_height=60,
            show_bottom_border=True,
            
            columns=[
                ft.DataColumn(ft.Text(f"Row #")),
                ft.DataColumn(ft.Text(f"Icon",text_align=ft.TextAlign.CENTER)),
                ft.DataColumn(ft.Text(f"None")),
                ft.DataColumn(ft.Text(f"None")),
                ft.DataColumn(ft.Text(f"None")),
                ft.DataColumn(ft.Text(f"None")),
                ft.DataColumn(ft.Text(f"None")),
                ft.DataColumn(ft.Text(f"None")),
                ft.DataColumn(ft.Text(f"None")),
                ft.DataColumn(ft.Text(f"None")),
                ft.DataColumn(ft.Text(f"None")),
                ft.DataColumn(ft.Text(f"None")),
                ft.DataColumn(ft.Text(f"None")),
                ft.DataColumn(ft.Text(f"None")),
                ft.DataColumn(ft.Text(f"None")),
                ft.DataColumn(ft.Text(f"None")),
            ],
            rows=[
                #color=ft.colors.with_opacity(0.3,ft.colors.WHITE),
            ],
        )

        def add_player():
            new_row = ft.DataRow(
                #color=ft.colors.with_opacity(0.3,ft.colors.WHITE),
                cells=[
                    ft.DataCell(ft.Text(f"N/A",text_align=ft.TextAlign.CENTER)),
                    ft.DataCell(ft.CircleAvatar(content=ft.Text("PL",text_align=ft.TextAlign.CENTER,size=20),bgcolor=ft.colors.ERROR_CONTAINER,radius=20)),  #For grounds could be vector icons
                    ft.DataCell(ft.CupertinoCheckbox()),
                    ft.DataCell(ft.Text(f"N/A")),
                    ft.DataCell(ft.Text(f"N/A")),
                    ft.DataCell(ft.Text(f"N/A")),
                    ft.DataCell(ft.Text(f"N/A")),
                    ft.DataCell(ft.Text(f"N/A")),
                    ft.DataCell(ft.Text(f"N/A")),
                    ft.DataCell(ft.Text(f"N/A")),
                    ft.DataCell(ft.Text(f"N/A")),
                    ft.DataCell(ft.Text(f"N/A")),
                    ft.DataCell(ft.Text(f"N/A")),
                    ft.DataCell(ft.Text(f"N/A")),
                    ft.DataCell(ft.Text(f"N/A")),
                    ft.DataCell(ft.Text(f"N/A")),
                    ft.DataCell(ft.Text(f"N/A")),
                ]
            )
            Player_search.table.rows.append(new_row)
            page.update()

        #Way to delete all the rows to be able to make a new list with filters
        def delete_player():
            for i in range(len(Player_search.table.rows)):
                Player_search.table.rows.pop()
                page.update()
                time.sleep(.001)
        
        def add_multiple():
                for i in range(250):
                    Player_search.add_player()

        def player_search_menu():  
            print(f"{page.route} Menu item clicked")
            return ft.Container(
                width=page.window_width,
                height=page.window_height,
                margin=10,
                border_radius=10,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.with_opacity(0.1,ft.colors.WHITE),
                expand=True,
                content=ft.Row([
                    ft.Container(
                        padding=10,
                        expand=True,
                        border_radius=10,
                        content=ft.Row(
                            [
                                ft.Column(
                                    [Player_search.table,
                                    ft.FilledTonalButton(text="Delete players",on_click=lambda e: Player_search.delete_player()),
                                    ft.FilledTonalButton(text="Add player",on_click=lambda e: Player_search.add_multiple())],
                                    scroll=ft.ScrollMode.AUTO,alignment=ft.alignment.center,on_scroll_interval=.1
                                ),
                            ],
                            scroll=ft.ScrollMode.AUTO,alignment=ft.alignment.center
                            ),
                        alignment=ft.alignment.top_center
                    )
                ],
                expand=True,
                alignment=ft.MainAxisAlignment.CENTER
                )
            )   
        

    class Online_pvp():
        def online_pvp():
            print(f"{page.route} Menu item clicked")
            return ft.Container(
                width=page.window_width,
                height=page.window_height,
                margin=5,
                border_radius=10,
                border=ft.border.all(2, ft.colors.WHITE24),
                alignment=ft.alignment.center,
                bgcolor=ft.colors.BLACK12,
                content=(ft.Text(
                    "Online PvP",
                    size=50,
                    color=ft.colors.with_opacity(0.5,ft.colors.WHITE),
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                    )),
                expand=True)


    class My_ROC_Team():
        def my_roc_team():
            print(f"{page.route} Menu item clicked")
            return ft.Container(
                width=page.window_width,
                height=page.window_height,
                margin=5,
                border_radius=10,
                border=ft.border.all(2, ft.colors.WHITE24),
                alignment=ft.alignment.center,
                bgcolor=ft.colors.BLACK12,
                content=(ft.Text(
                    "MY R.O.C Team",
                    size=50,
                    color=ft.colors.with_opacity(0.5,ft.colors.WHITE),
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                    )),
                expand=True)

    class Settings():
        def settings():
            print(f"{page.route} Menu item clicked")
            return ft.Container(
                width=page.window_width,
                height=page.window_height,
                margin=5,
                border_radius=10,
                border=ft.border.all(2, ft.colors.WHITE24),
                alignment=ft.alignment.center,
                bgcolor=ft.colors.BLACK12,
                content=(ft.Text(
                    "Settings",
                    size=50,
                    color=ft.colors.with_opacity(0.5,ft.colors.WHITE),
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                    )),
                expand=True)
    


  
    


    def route_change(route):
        page.update
        page.views.clear()
        page.views.append(

        ft.View(
            "/",
            [   
                ft.Row ([
                ft.Row(alignment="top_left", spacing=25, controls=[Main_menu.management_window()],expand=True), #Main_dashboard
                ],
                expand=True)
            ],
            
        )

        )
        if page.route == "/Dashboard":
            page.views.append(
                ft.View(
                    "/Dashboard",
                    [
                        ft.Row ([ 
                        ft.Row(alignment="top_left", spacing=25, controls=[Main_menu.side_menu(),Dashboard.dashboard()],expand=True),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/Dashboard")),
                        ],expand=True)
                    ]
                )
            )
        
        if page.route == "/Sim Game":
            page.views.append(
                ft.View(
                    "/Sim Game",
                    [
                        ft.Row ([ 
                        ft.Row(alignment="top_let", spacing=25, controls=[Main_menu.side_menu(),Sim_game.sim_game()],expand=True),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                        ],expand=True)
                    ],
                )
            )

        if page.route == "/Online PvP":
            page.views.append(
                ft.View(
                    "/Online PvP",
                    [
                        ft.Row ([ 
                        ft.Row(alignment="top_let", spacing=25, controls=[Main_menu.side_menu(),Online_pvp.online_pvp()],expand=True),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                        ],expand=True)
                    ],
                )
            )
        
        if page.route == "/Player Search":
            page.views.append(
                ft.View(
                    "/Player Search",
                    [
                        ft.Row ([ 
                        ft.Row(alignment="top_let", spacing=25, controls=[Main_menu.side_menu(),Player_search.player_search_menu()],expand=True),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                        ],expand=True)
                    ],
                )
            )
        if page.route == "/MY R.O.C Team":
            page.views.append(
                ft.View(
                    "/MY R.O.C Team",         
                    [
                        ft.Row ([ 
                        ft.Row(alignment="top_let", spacing=25, controls=[Main_menu.side_menu(),My_ROC_Team.my_roc_team()],expand=True),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                        ],expand=True)
                    ],
                )
            )
        if page.route == "/Settings":
            page.views.append(
                ft.View(
                    "/Settings",
                    [
                        ft.Row ([ 
                        ft.Row(alignment="top_let", spacing=25, controls=[Main_menu.side_menu(),Settings.settings()],expand=True),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                        ],expand=True)
                    ],
                )
            )
            
    def page_resive(e):
        page.go(f"'{page.route}'")
       

    page.update()
    page.on_route_change = route_change

    page.go(page.route)
    


ft.app(target=main)
