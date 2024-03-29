import flet as ft

def main(page: ft.Page):
    page.title = "AlertDialog examples"




    ad = ft.AlertDialog(
           modal=True,
           open=False,
           title=ft.Text("Please Confirm"),
           content=ft.Text("Are you sure you want to permanently delete your management?\nDoing so will close the program"),
           actions=(
              ft.TextButton("Yes"),
              ft.TextButton("No"),
           ),
           actions_alignment=ft.MainAxisAlignment.END
        )

    def show():
        page.dialog = ad
        ad.open = True
        page.update()




    page.add(
       ft.FilledButton("button",on_click=lambda e:show())
        
    )

ft.app(target=main)