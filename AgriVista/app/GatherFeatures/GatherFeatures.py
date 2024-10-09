# import flet as ft
# import numpy as np
# from model.crop_prediction import CropPrediction
# from utils import Location
# from utils import ModelData
# from constants import constants
# def GatherFeatures(page:ft.Page):
#     isLoading = False
#     loading = ft.ProgressRing(width=25, 
#                               height=30,
#                               color=ft.colors.GREEN_300,
#                               stroke_width = 10)
#     loading = ft.Container(
#         margin=ft.margin.only(left=15),
#         border_radius=10,
#         content=loading
#     )
#     loading = ft.Row(
#         controls=[
#             loading,
#             ft.Container(margin=5),
#             ft.Text("Processing...",style=ft.TextStyle(color=ft.colors.GREEN_700,size=20,weight=ft.FontWeight.BOLD))
#         ]
#     )
#     async def evalutate(e):
#         # await Location.get_current_location1()
#         # print(Location.get_city_and_village())
#         city,lat,lon = await Location.get_city_and_village()
#         model_data = ModelData.ModelData(city,lat,lon,float(ph.value),int(soil_type.value))
#         await model_data.getModelData()
       
#         # input_values = np.array([[17.8,682,float(ph.value),67.4,9,1,int(soil_type.value)]])
#         # print(ph.value)
#         model = CropPrediction()
#         await model.load_model()
#         await model.make_prediction(model_data.conditions)
#         # print(model.top_3_crops)
#         if model.top_3_crops:
#             page.session.set("top_3_crops", model.top_3_crops)
#             page.go("/home")
        
#     logo = ft.Image(
#                 src=constants.logo1,
#                 width=None,
#                 height=None,
#                 fit=ft.ImageFit.COVER,
#                 repeat=ft.ImageRepeat.NO_REPEAT,
#                 border_radius=ft.border_radius.all(30),
#             )
#     logo = ft.CircleAvatar(
#         content=logo,
#         width=150,
#         height=150,
#         bgcolor=ft.colors.GREEN_300,
#         )
#     # form = ft.Container(
#     #                 content=ft.Text("Non clickable"),
#     #                 margin=10,
#     #                 padding=10,
#     #                 alignment=ft.alignment.center,
#     #                 bgcolor="#DCE1E9",
#     #                 width=None,
#     #                 height=None,
#     #                 border_radius=10,
#     #             )
#     ph =ft.TextField(
#             keyboard_type=ft.KeyboardType.NUMBER,
#             prefix_icon=ft.icons.SCALE, 
#             prefix_style = ft.TextStyle(bgcolor=ft.colors.GREEN_500),
#             label="Enter Soil PH Level",
#             label_style=ft.TextStyle(color=ft.colors.GREEN_500),
#             text_size=15,
#             height=70,
#             # cursor_color=ft.colors.RED,
#             # selection_color=ft.colors.YELLOW,
#             color=ft.colors.GREEN_200,
#             bgcolor=ft.colors.WHITE,
#             filled=True,
#             border=ft.InputBorder.NONE,
           
#             # filled=True,
#             # focused_color=ft.colors.GREEN,
#             # focused_bgcolor=ft.colors.CYAN_200,
            
#             border_color=ft.colors.CYAN_500,
#             # focused_border_color=ft.colors.GREEN_ACCENT_400,
#             # max_length=10,
#             # capitalization="characters",
#         )
#     soil_type = ft.Dropdown(
#             options=[
#                 ft.dropdown.Option(0, "Loam"),
#                 ft.dropdown.Option(1, "Sandy loam"),
#                 # ft.dropdown.Option("c", "Item C"),
#             ],
#             label="Choose Soil Type",
            
#             label_style=ft.TextStyle(color=ft.colors.GREEN_200),
#             # border_radius=20,
#             height=80,         
#             filled=True,
#             border_color=ft.colors.GREEN_500,
#             bgcolor=ft.colors.WHITE,
#             color=ft.colors.GREEN_200,
            
#             prefix_icon=ft.icons.ENERGY_SAVINGS_LEAF, 
#             # focused_bgcolor=ft.colors.BLUE_100,
#         )
#     form = ft.ListView(
#         controls=[
#         ph,
#         ft.Container(
#         height=50
#         ),
#         soil_type,
#         isLoading if loading else ft.FilledButton(
#             "Evalutate",
#             style=ft.ButtonStyle(
#                 bgcolor=ft.colors.GREEN_300,
#                 shape=ft.RoundedRectangleBorder(radius=30),
#             ),
#             on_click=evalutate
#             # on_click=lambda e: page.go("/home")
#         ),
#     ])
#     form = ft.Container(
#         margin=ft.margin.only(left=20,top=50,right=20,bottom=30),
#         # padding=ft.padding.only(left=20,top=50,right=20,bottom=90),
#         border_radius=30,
#         # bgcolor="#EBEEF3",
#         width=270,
#             content=form
#     ) 
#     form = ft.Card(
#         margin=ft.margin.only(left=30,),
#         content=form,
#         color="#EBEEF3",
#     )

#     return [
       
#         ft.Container(
#           content=ft.Text(""),height=40,  
#         ),
#         logo,
#         ft.Container(
#           content=ft.Text(""),height=30,  
#         ),
#         form,
        
#     ]

import flet as ft
import numpy as np
from model.crop_prediction import CropPrediction
from utils import Location
from utils import ModelData
from constants import constants
import asyncio
from model.marketPrediction import MarketModel

def GatherFeatures(page: ft.Page):
    isLoading = ft.Ref()  # No need to pass a type, just initialize as ft.Ref()
    isLoading.current = False  # Initialize loading state as False
    cropMarket = MarketModel()
    
# Loading spinner
    loading_spinner = ft.ProgressRing(
        width=25,
        height=30,
        color=ft.colors.GREEN_300,
        stroke_width=10
    )
    loading_spinner_container = ft.Container(
        margin=ft.margin.only(left=15),
        border_radius=10,
        content=loading_spinner
    )
    loading_row = ft.Row(
        controls=[
            loading_spinner_container,
            ft.Container(margin=5),
            ft.Text("Processing...", style=ft.TextStyle(color=ft.colors.GREEN_700, size=20, weight=ft.FontWeight.BOLD))
        ]
    )
    
 
    async def evalutate(e):
        nonlocal cropMarket
        isLoading.current = True  # Set loading state to True
        page.update()  # Trigger UI update to show loading

        await asyncio.sleep(0.1)  # Briefly yield control

        try:
            # Proceed with long-running tasks
            city, lat, lon = await Location.get_city_and_village()
            
            model_data = ModelData.ModelData(city, lat, lon, float(ph.value), int(soil_type.value))
            await model_data.getModelData()

            model = CropPrediction()
            await model.load_model()
            await model.make_prediction(model_data.conditions)
            
            await cropMarket.load_model()
            # if model.top_3_crops:
            #     page.session.set("top_3_crops", model.top_3_crops)
            #     page.go("/home")
        except Exception as e:
            print(f"Error during evaluation: {e}")
        finally:
            isLoading.current = False  # Set loading state back to False
            page.update()  # Trigger UI update to hide loading


    # Logo definition
    logo = ft.Image(
        src=constants.logo1,
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
        bgcolor=ft.colors.GREEN_300,
    )

    # Form elements
    ph = ft.TextField(
        keyboard_type=ft.KeyboardType.NUMBER,
        prefix_icon=ft.icons.SCALE,
        prefix_style=ft.TextStyle(bgcolor=ft.colors.GREEN_500),
        label="Enter Soil PH Level",
        label_style=ft.TextStyle(color=ft.colors.GREEN_500),
        text_size=15,
        height=70,
        color=ft.colors.GREEN_200,
        bgcolor=ft.colors.WHITE,
        filled=True,
        border=ft.InputBorder.NONE,
        border_color=ft.colors.CYAN_500,
    )
    
    soil_type = ft.Dropdown(
        options=[
            ft.dropdown.Option(0, "Loam"),
            ft.dropdown.Option(1, "Sandy loam"),
        ],
        label="Choose Soil Type",
        label_style=ft.TextStyle(color=ft.colors.GREEN_200),
        height=80,
        filled=True,
        border_color=ft.colors.GREEN_500,
        bgcolor=ft.colors.WHITE,
        color=ft.colors.GREEN_200,
        prefix_icon=ft.icons.ENERGY_SAVINGS_LEAF, 
    )

    # Updateable form
    def build_form():
        return ft.ListView(
            
            controls=[
                ph,
                ft.Container(height=50),
                soil_type,
                ft.Container(height=30),  # Space between fields
                loading_row if isLoading.current else ft.FilledButton(
                    "Evaluate",
                    style=ft.ButtonStyle(
                        bgcolor=ft.colors.GREEN_300,
                        shape=ft.RoundedRectangleBorder(radius=30),
                    ),
                    on_click=evalutate,
                ),
            ]
        )

    # Main form container
    form_container = ft.Container(
        margin=ft.margin.only(left=20, top=50, right=20, bottom=30),
        border_radius=30,
        width=270,
        content=build_form()  # Load the form with dynamic content
    )

    # Card container
    form_card = ft.Card(
        margin=ft.margin.only(left=30),
        content=form_container,
        color="#EBEEF3",
    )

    # Page layout
    return [
        ft.Container(content=ft.Text(""), height=40),
        logo,
        ft.Container(content=ft.Text(""), height=30),
        form_card,
    ]