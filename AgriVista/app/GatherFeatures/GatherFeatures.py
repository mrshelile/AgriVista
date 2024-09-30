import flet as ft

def GatherFeatures(page:ft.Page):

    # logo = ft.Image(
    #             src=f"https://ibb.co/yqz2k9Z",
    #             width=100,
    #             height=100,
    #             fit=ft.ImageFit.COVER,
    #             repeat=ft.ImageRepeat.NO_REPEAT,
    #             border_radius=ft.border_radius.all(30),
    #         )
    logo = ft.Image(
                src=f"https://i.ibb.co/7K3hpfZ/logo.png",
                width=None,
                height=None,
                fit=ft.ImageFit.COVER,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(30),
            )
    logo = ft.CircleAvatar(
        content=logo,
        width=150,
        height=150,
        bgcolor=ft.colors.CYAN_500,
        )
    form = ft.Container(
                    content=ft.Text("Non clickable"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor="#DCE1E9",
                    width=None,
                    height=None,
                    border_radius=10,
                )
    
    form = ft.ListView(
        controls=[
        ft.TextField(
            prefix_icon=ft.icons.SCALE, 
            prefix_style = ft.TextStyle(bgcolor=ft.colors.CYAN_500),
            label="Enter Soil PH Level",
            label_style=ft.TextStyle(color=ft.colors.CYAN_500),
        
            text_size=15,
            height=70,
            # cursor_color=ft.colors.RED,
            # selection_color=ft.colors.YELLOW,
            color=ft.colors.CYAN_500,
            bgcolor=ft.colors.WHITE,
            filled=True,
            border=ft.InputBorder.NONE,
           
            # filled=True,
            # focused_color=ft.colors.GREEN,
            # focused_bgcolor=ft.colors.CYAN_200,
            
            border_color=ft.colors.CYAN_500,
            # focused_border_color=ft.colors.GREEN_ACCENT_400,
            # max_length=10,
            # capitalization="characters",
        ),
        ft.Container(
        height=50
        ),
        ft.Dropdown(
            options=[
                ft.dropdown.Option("Loam", "Loam"),
                ft.dropdown.Option("Sandy loam", "Sandy loam"),
                # ft.dropdown.Option("c", "Item C"),
            ],
            label="Choose Soil Type",
            
            label_style=ft.TextStyle(color=ft.colors.CYAN_500),
            # border_radius=20,
            height=80,         
            filled=True,
            border_color=ft.colors.CYAN_500,
            bgcolor=ft.colors.WHITE,
            color=ft.colors.CYAN_500,
            
            prefix_icon=ft.icons.ENERGY_SAVINGS_LEAF, 
            # focused_bgcolor=ft.colors.BLUE_100,
        ),
         ft.FilledButton(
            "Evalutate",
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=30),
            ),
            on_click=lambda e: page.go("/home")
        ),
    ])
    form = ft.Container(
        margin=ft.margin.only(left=20,top=50,right=20,bottom=30),
        # padding=ft.padding.only(left=20,top=50,right=20,bottom=90),
        border_radius=30,
        # bgcolor="#EBEEF3",
        width=270,
            content=form
    ) 
    form = ft.Card(
        margin=ft.margin.only(left=30,),
        content=form,
        color="#EBEEF3",
    )

    return [
       
        ft.Container(
          content=ft.Text(""),height=40,  
        ),
        logo,
        ft.Container(
          content=ft.Text(""),height=30,  
        ),
        form,
        
    ]