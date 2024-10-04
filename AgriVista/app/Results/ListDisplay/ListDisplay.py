import flet as ft
from app.Results.ListDisplay.components.TopHeader import TopHeader
from app.Results.ListDisplay.components.CropInfo import CropInfo
from constants.crops import cropsImage
from app.Results.ListDisplay.components.CropInfo import buildChanges
from constants import constants

def ListDisplay(page:ft.Page,values):
    cleaned_data = []
    for item, value in values:
        # Check if the item contains parentheses
        if '(' in item and ')' in item:
            # Extract the part before the parentheses
            cleaned_item = item.split(' (')[0]
        else:
            cleaned_item = item  # Keep the original name if no parentheses

        cleaned_data.append((cleaned_item, value))
    crops_dict = {crop['name']: crop['link'] for crop in cropsImage}
    merged_result = []
    for name, probability in cleaned_data:
        if name in crops_dict:
            merged_result.append({
                "name": name,
                "link": crops_dict[name],
                "probability": probability*100
            })
    
    selected_crop =  merged_result[0]    
    def onSelected(e):
        nonlocal selected_crop
        for crop in merged_result:
        
            if crop['name'].lower() == e.data.lower():
                selected_crop = crop
                break
        # print(selected_crop)
        crop_name.value ="Predicted Crop:" + e.data
        top.content = ft.Image(
            fit=ft.ImageFit.COVER,
            src=selected_crop['link'])
        
        print(cropInfo.content.controls[0])
        cropInfo.content.controls[1] = buildChanges(
            value=selected_crop['probability']
            )
        page.update()
        
    crop_name = ft.Text(
                #    "Predicted Crop: Spinach",
                    f"Predicted Crop: {selected_crop['name']}",
                   color=ft.colors.BLACK,
                   size=20) 
    # top = TopHeader(page,selected_crop['link'])
    top = ft.Container(
        # image_src="",
        # bgcolor=ft.colors.BLUE_300,
        width=350,
        height=300,
        border_radius=ft.border_radius.only(40,40,0,0),
        content=ft.Image(
            fit=ft.ImageFit.COVER,
            src=selected_crop['link'])
        )
    cropInfo =  CropInfo(page,margin=10,changes=merged_result[0]['probability'])
    body = ft.Column(
            [   ft.Container(height=30),
                top,
               crop_name,
                    #    ft.dropdown.Option("Spinach", "Spinach"),
                    #     ft.dropdown.Option("Maize", "Maize"),
               ft.Dropdown(
                    on_change=onSelected,
                    options=[ft.dropdown.Option(crop['name'],crop['name']) for crop in merged_result],
                    
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
              cropInfo,
               
            ]
        )
    body  = ft.Container(
        width=370,
        height=720,
        # bgcolor=ft.colors.RED_200,
        content=body
    )
    return body