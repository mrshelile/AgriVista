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
# import flet as ft
# from app.OnBoarding import Onboarding

# def main(page: ft.Page):

#     page.title = "NavigationBar Example"
#     page.navigation_bar = ft.NavigationBar(
#         destinations=[
#             ft.NavigationBarDestination(icon=ft.icons.EXPLORE, label="Explore"),
#             ft.NavigationBarDestination(icon=ft.icons.COMMUTE, label="Commute"),
#             ft.NavigationBarDestination(
#                 icon=ft.icons.BOOKMARK_BORDER,
#                 selected_icon=ft.icons.BOOKMARK,
#                 label="Explore",
#             ),
#         ]
#     )
#     page.add(ft.Text("Body!"))

# ft.app(main)

# import flet as ft
# from app.OnBoarding.Onboarding import  Onboarding
# def main(page: ft.Page):

#     page.title = "AgriVista"

#     col = Onboarding(page)
#     page.add(col)
#     page.update()

# ft.app(main)
from app.GatherFeatures.GatherFeatures import GatherFeatures
from app.OnBoarding.Onboarding import  Onboarding
from constants.colors import *
import flet as ft

def main(page: ft.Page):
    page.title = "AgriVista"

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                Onboarding(page),   
                bgcolor=ft.colors.CYAN_700
            )
        )
    
        if page.route == "/gatherFeatures":
            page.views.append(
                ft.View(
                    "/gatherFeatures",
                    GatherFeatures(page),
                    bgcolor=ft.colors.WHITE
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(main,)