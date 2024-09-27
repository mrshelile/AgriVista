# import flet as ft

# def home(page:ft.Page):
#     page_number= 1
    
#     def nav_selected(number):
#         nonlocal page_number
#         page_number = number
#         page.update()

#     buttons = ft.Row(
#         controls=[
#             ft.Container(
#             on_click=lambda e:nav_selected(),
#             # bgcolor=ft.colors.CYAN_200 if page_number ==1 else None,
#             margin=ft.margin.only(left=10),
#             padding=ft.padding.all(6),
#             border_radius=5,
#             content=
#             ft.Row(controls=[
#                 ft.CircleAvatar(
#                     bgcolor=ft.colors.BLACK45,
#                     content=
#                     ft.Icon(ft.icons.HOME_ROUNDED,size=40,color=ft.colors.WHITE)),
#                     ft.Text(f"Home",style=ft.TextStyle(color=ft.colors.WHITE60,
#                     weight=ft.FontWeight.W_900)
#                         )
#                 ]),
#             ),
#             ft.Container(
#             on_click=lambda e:nav_selected(2),  
#             # bgcolor=ft.colors.CYAN_200 if page_number ==2 else None,  
#             margin=ft.margin.only(left=40),
#             content=
#             ft.Row(controls=[
#                 ft.CircleAvatar(
#                     bgcolor=ft.colors.BLACK45,
#                     content=
#                     ft.Icon(ft.icons.TRENDING_UP,size=40,color=ft.colors.WHITE)),
#                     ft.Text("Trends",style=ft.TextStyle(color=ft.colors.WHITE60,
#                     weight=ft.FontWeight.W_900)
#                         )
#                 ]),
#             ),
#             ft.Container(
#             on_click=lambda e:nav_selected(3),   
#             margin=ft.margin.only(left=20),
#             # bgcolor=ft.colors.CYAN_200 if page_number ==3 else None,
#             content=
#             ft.Row(controls=[
#                 ft.CircleAvatar(
#                     bgcolor=ft.colors.BLACK45,
#                     content=
#                     ft.Icon(ft.icons.HOME_ROUNDED,size=40,color=ft.colors.WHITE)),
#                     ft.Text("Other",style=ft.TextStyle(color=ft.colors.WHITE60,
#                     weight=ft.FontWeight.W_900)
#                         )
#                 ]),
#             ),
#         ]
#     )
#     buttons = ft.Container(
#         margin=ft.margin.only(top=730,left=-9,right=-9),
#         bgcolor=ft.colors.GREEN_400,
#         # width=1000,
#         height=70,
#         content=buttons
#     )
#     body = ft.Stack(
#         controls=[
#             buttons,
#         ]
#     )
#     return [
#       body,
#     ]

import flet as ft

def home(page: ft.Page):
    page_number = 1
    
    def nav_selected(number):
        nonlocal page_number
        page_number = number
        update_button_colors()  # Update button colors when navigation is selected
        page.update()

    def update_button_colors():
        # Update the background color of each button based on the selected page
        for idx, button in enumerate(buttons):
            button.bgcolor = ft.colors.CYAN_200 if page_number == idx + 1 else None

    # Create buttons
    buttons = [
        ft.Container(
            on_click=lambda e: nav_selected(1),
            margin=ft.margin.only(left=10),
            padding=ft.padding.all(3),
            bgcolor=ft.colors.CYAN_200,
            border_radius=5,
            content=ft.Row(controls=[
                ft.CircleAvatar(
                    bgcolor=ft.colors.BLACK45,
                    content=ft.Icon(ft.icons.HOME_ROUNDED, size=40, color=ft.colors.WHITE)
                ),
                ft.Text("Home", style=ft.TextStyle(color=ft.colors.WHITE60, weight=ft.FontWeight.W_900))
            ])
        ),
        ft.Container(
            on_click=lambda e: nav_selected(2),
            margin=ft.margin.only(left=30),

            padding=ft.padding.all(6),
            border_radius=5,
            content=ft.Row(controls=[
                ft.CircleAvatar(
                    bgcolor=ft.colors.BLACK45,
                    content=ft.Icon(ft.icons.TRENDING_UP, size=40, color=ft.colors.WHITE)
                ),
                ft.Text("Trends", style=ft.TextStyle(color=ft.colors.WHITE60, weight=ft.FontWeight.W_900))
            ])
        ),
        ft.Container(
            on_click=lambda e: nav_selected(3),
            margin=ft.margin.only(left=20),
            padding=ft.padding.all(6),
            border_radius=5,
            content=ft.Row(controls=[
                ft.CircleAvatar(
                    bgcolor=ft.colors.BLACK45,
                    content=ft.Icon(ft.icons.HOME_ROUNDED, size=40, color=ft.colors.WHITE)
                ),
                ft.Text("Other", style=ft.TextStyle(color=ft.colors.WHITE60, weight=ft.FontWeight.W_900))
            ])
        ),
    ]

    # Create bottom navigation
    bottomNav = ft.Row(controls=buttons)
    bottomNav = ft.Container(
        margin=ft.margin.only(top=730, left=-9, right=-9),
        bgcolor=ft.colors.GREEN_400,
        height=70,
        content=bottomNav
    )
    screens =[
        ft.Text("Home"),
        ft.Text("Trends"),
        ft.Text("Other")
    ]
    body = ft.Stack(
        controls=[
            ft.Container(
                height=727,
                content=screens[page_number-1]
                ),
            bottomNav,
        ]
        )
    return [body]
