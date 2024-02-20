import flet as ft

def main(page: ft.Page):

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
                content=ft.Row([
                    ft.Tabs(
                        unselected_label_color=ft.colors.WHITE60, 
                        label_color=ft.colors.WHITE,
                        overlay_color=ft.colors.TRANSPARENT,
                        indicator_color=ft.colors.WHITE,
                        height=page.window_height -100,
                        width=page.window_width -100,
                        selected_index = 0,
                        animation_duration=300,

                        tabs=[
                            ft.Tab(
                                text="HOME",
                                tab_content=ft.Text("HOME",size=20),
                                content=ft.Container(
                                    alignment=ft.alignment.center,
                                    margin=10,
                                    border_radius=15,
                                    expand=0,
                                )
                            ),
                            ft.Tab(
                                text="MY R.O.C",
                                tab_content=ft.Text("MY R.O.C",size=20),
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
                            )]
                            ,)
                            ]) ,expand=True
            )
                            
                    
    
            


    page.add(Dashboard.dashboard())

ft.app(target=main)