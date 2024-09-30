import flet as ft

def CropInfo(page:ft.Page):
    width = 180
    height = 230
    body = ft.Row(
        [   
            
            ft.Container(
                border_radius=15,
                width=width,
                height=height,
                bgcolor=ft.colors.GREEN_400,
                content=ft.Column(
                    [   ft.Container(height=10),
                        ft.Container(
                            margin=ft.margin.only(left=20),
                            content=ft.Text("Estimate Margin",size=18),
                            ),
                        ft.Container(
                            height=120,
                            margin=ft.margin.only(left=15),
                            content=ft.Image('https://i.ibb.co/MC1ZDfg/sad.png'),
                            ),
                       ft.Container(
                            margin=ft.margin.only(left=20),
                            content=ft.Text("40%",size=18),
                            ),
                    ]
                )
                ),
            ft.Container(
                border_radius=15,
                width=width,
                height=height,
                bgcolor=ft.colors.GREEN_400,
                content=ft.Column(
                    [   ft.Container(height=10),
                        ft.Container(
                            margin=ft.margin.only(left=20),
                            content=ft.Text("Chances",size=18),
                            ),
                        ft.Container(
                            height=120,
                            margin=ft.margin.only(left=15),
                            content=ft.Image('https://i.ibb.co/MC1ZDfg/sad.png'),
                            ),
                       ft.Container(
                            margin=ft.margin.only(left=20),
                            content=ft.Text("20%",size=18),
                            ),
                    ]
                )
                ),
        ]
    )
    body = ft.Container(
        content=body,
        # bgcolor=ft.colors.GREEN_200,
        width=370,
    )
    return body