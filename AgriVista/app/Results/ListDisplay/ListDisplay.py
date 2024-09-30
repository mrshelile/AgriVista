import flet as ft
from app.Results.ListDisplay.components.TopHeader import TopHeader
from app.Results.ListDisplay.components.CropInfo import CropInfo

def ListDisplay(page:ft.Page):
    body = ft.Column(
            [   ft.Container(height=40),
                TopHeader(page),
               ft.Text(
                   "Predicted Crop: Spinach",
                   color=ft.colors.BLACK,
                   size=20),
               ft.Dropdown(
                   
                    options=[
                        ft.dropdown.Option("Spinach", "Spinach"),
                        ft.dropdown.Option("Maize", "Maize"),
                        # ft.dropdown.Option("c", "Item C"),
                    ],
                    label="Choose Best Predicted Crops",
                    
                    label_style=ft.TextStyle(color=ft.colors.GREEN_500),
                    border_radius=10,
                    height=80,         
                    filled=True,
                    bgcolor=ft.colors.WHITE,
                    color=ft.colors.CYAN_500,
                    
                    prefix_icon=ft.icons.AGRICULTURE, 
                    # focused_bgcolor=ft.colors.BLUE_100,
                ),
               CropInfo(page),
               
            ]
        )
    body  = ft.Container(
        width=370,
        height=720,
        # bgcolor=ft.colors.RED_200,
        content=body
    )
    return body