import flet as ft

def main(page: ft.Page):
    page.title = "Player Search"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    table = ft.DataTable(
        column_spacing = 50,

        columns=[
            ft.DataColumn(ft.Text("Name",weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Age",weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Height",weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Weight",weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Build",weight=ft.FontWeight.BOLD)),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("NULL")),
                    ft.DataCell(ft.Text("NULL")),
                    ft.DataCell(ft.Text("NULL")),
                    ft.DataCell(ft.Text("NULL")),
                    ft.DataCell(ft.Text("NULL")),
                ]
            )
        ]
    )

    row = ft.Row(
        
        [
            ft.Container(
                width=500,
                height=500,
                border_radius=10,
                bgcolor=ft.colors.with_opacity(0.1,ft.colors.WHITE),
                alignment=ft.alignment.top_center,
                content=ft.Column([table],scroll=ft.ScrollMode.ALWAYS)),
        ],
        scroll=ft.ScrollMode.ALWAYS
    )
    page.add(row)


    def new_row(e):
        nr = ft.DataRow(
            cells=[
                ft.DataCell(ft.Text("NULL")),
                ft.DataCell(ft.Text("NULL")),
                ft.DataCell(ft.Text("NULL")),
                ft.DataCell(ft.Text("NULL")),
                ft.DataCell(ft.Text("NULL")),
            ]
        )
        
        table.rows.append(nr)
        page.update()
        print("page update")

    add_row = ft.ElevatedButton(text="Button",on_click=new_row,data=0)
    page.add(add_row)

    upload_url = page.get_upload_url("dir/Player_search_list_example.py", 60)
    page.launch_url(upload_url)
   
ft.app(target=main, upload_dir="uploads")
    















'''
    table=ft.DataTable(
        border=ft.border.all(2, "red"),
        show_bottom_border=True,
        #columns 里必须添加 DataColumn 类型的控件
        columns=[
                ft.DataColumn(ft.Text("HELLO 1")),
                ft.DataColumn(ft.Text("BYE 2")),
                ft.DataColumn(ft.Text("SAMPLE COLUMN 3")),
                ft.DataColumn(ft.Text("DUMMY COLUMN 4")),
                ft.DataColumn(ft.Text("HELLO COLUMNS 5")),
                ft.DataColumn(ft.Text("BYE COLUMNS 6")),
                ft.DataColumn(ft.Text("OKAY COLUMNS 7")),ft.DataColumn(ft.Text("I LOVE COLUMNS 8")),
                ft.DataColumn(ft.Text("COLUMNS FOR SCROLLING 9"), numeric=True),
            ],
        #rows 里必须添加 DataRow 类型的控件
        #DataRow 
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("John 1")),
                    ft.DataCell(ft.Text("John 2")),
                    ft.DataCell(ft.Text("John 3")),
                    ft.DataCell(ft.Text("John 4")),
                    ft.DataCell(ft.Text("John 5")),
                    ft.DataCell(ft.Text("John 6")),
                    ft.DataCell(ft.Text("John 7")),
                    ft.DataCell(ft.Text("John 8")),
                    ft.DataCell(ft.Text("John 9")),
                    ])
            ]
        )
    
    cv = ft.Column([table])
    rv = ft.Row([cv],scroll=True,expand=1,vertical_alignment=ft.CrossAxisAlignment.START)
    page.add(rv)





    def button_clicked(e):
        b=ft.DataRow(
                cells=[  
                    ft.DataCell(ft.Text("John 1")),
                    ft.DataCell(ft.Text("John 2")),
                    ft.DataCell(ft.Text("John 3")),
                    ft.DataCell(ft.Text("John 4")),
                    ft.DataCell(ft.Text("John 5")),
                    ft.DataCell(ft.Text("John 6")),
                    ft.DataCell(ft.Text("John 7")),
                    ft.DataCell(ft.Text("John 8")),
                    ft.DataCell(ft.Text("John 9")),
                    ])

        table.rows.append(b)
        page.update()
        print("按钮被点击")
    add_row = ft.ElevatedButton(text="添加一行数据",on_click=button_clicked,data=0)
    page.add(add_row)
'''