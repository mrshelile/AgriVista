# import flet as ft


# def main(page: ft.Page):
#     page.title = "Flet counter example"
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER

#     txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

#     def minus_click(e):
#         txt_number.value = str(int(txt_number.value) - 1)
#         page.update()

#     def plus_click(e):
#         txt_number.value = str(int(txt_number.value) + 1)
#         page.update()

#     page.add(
#         ft.Row(
#             [
#                 ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
#                 txt_number,
#                 ft.IconButton(ft.icons.ADD, on_click=plus_click),
#             ],
#             alignment=ft.MainAxisAlignment.CENTER,
#         )
#     )


# ft.app(main)
import flet as ft

def main(page: ft.Page):

    page.title = "NavigationBar Example"
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.EXPLORE, label="Explore"),
            ft.NavigationBarDestination(icon=ft.icons.COMMUTE, label="Commute"),
            ft.NavigationBarDestination(
                icon=ft.icons.BOOKMARK_BORDER,
                selected_icon=ft.icons.BOOKMARK,
                label="Explore",
            ),
        ]
    )
    page.add(ft.Text("Body!"))

ft.app(main)