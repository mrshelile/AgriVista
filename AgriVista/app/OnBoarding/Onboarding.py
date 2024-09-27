import flet as ft
from constants.colors import * 

def Onboarding(page:ft.Page):
    intro = "Boost your farm with yield predictions, climate insights, and market insights!"
    # intro +="climate insights and market insights"
    text_intro = ft.Text(intro,style=ft.TextStyle(
        size=20,
        weight=ft.FontWeight.W_600,
    ))
    text_intro =ft.Container(
        content=text_intro,
        width=300,
        margin=ft.margin.only(left=40)
    )
    img = ft.Image(
        fit=ft.ImageFit.COVER,
        src=f'https://i.ibb.co/cTj1vqv/farming-concept-with-farmer-harvest-23-2148438599.png')
    img = ft.Container(
        content=img,
        margin=ft.margin.only(left=20),
        width=330 ,
        height=380   
    )
    return [
        ft.Container(
        height=90,    
        ),
        text_intro,
        ft.Container(height=10),
        img,
        ft.Row(
            controls=[
            ft.Container(width=90),
            ft.ElevatedButton(
            style=ft.ButtonStyle(
                bgcolor=ft.colors.WHITE,
                shape=ft.StadiumBorder(),
            ),
            text="Continue here!",
            icon="park_rounded",
            icon_color="green400",
            on_click=lambda e: page.go("/gatherFeatures")
        ),
            ]
        )
        ]