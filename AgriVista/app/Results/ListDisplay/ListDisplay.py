import flet as ft
from app.Results.ListDisplay.components.TopHeader import TopHeader
from app.Results.ListDisplay.components.CropInfo import CropInfo

cropsImage = [
    { "name": "Cabbage", "link": "https://images.pexels.com/photos/2518893/pexels-photo-2518893.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1" },
    { "name": "Spinach", "link": "https://i.ibb.co/5jwXSDf/Spinach." },
    { "name": "Carrots", "link": "https://example.com/carrots.jpg" },
    { "name": "Onions", "link": "https://example.com/onions.jpg" },
    { "name": "Tomatoes", "link": "https://example.com/tomatoes.jpg" },
    { "name": "Lettuce", "link": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.JrSTe5rMkeTSb4v1HRCscQHaEK%26pid%3DApi&f=1&ipt=bf363710638c68d06ef22f4f2c8df759046bb14944f431d3580ffd4cf6161bd7&ipo=images" },
    { "name": "Broccoli", "link": "https://example.com/broccoli.jpg" },
    { "name": "Cauliflower", "link": "https://example.com/cauliflower.jpg" },
    { "name": "Peppers", "link": "https://example.com/peppers.jpg" },
    { "name": "Eggplant", "link": "https://example.com/eggplant.jpg" },
    { "name": "Zucchini", "link": "https://example.com/zucchini.jpg" },
    { "name": "Pumpkin", "link": "https://example.com/pumpkin.jpg" },
    { "name": "Squash", "link": "https://example.com/squash.jpg" },
    { "name": "Radishes", "link": "https://example.com/radishes.jpg" },
    { "name": "Beets", "link": "https://example.com/beets.jpg" },
    { "name": "Turnips", "link": "https://example.com/turnips.jpg" },
    { "name": "Kale", "link": "https://example.com/kale.jpg" },
    { "name": "Swiss Chard", "link": "https://example.com/swiss_chard.jpg" },
    { "name": "Celery", "link": "https://example.com/celery.jpg" },
    { "name": "Leeks", "link": "https://example.com/leeks.jpg" },
    { "name": "Artichokes", "link": "https://example.com/artichokes.jpg" },
    { "name": "Asparagus", "link": "https://example.com/asparagus.jpg" },
    { "name": "Bok Choy", "link": "https://example.com/bok_choy.jpg" },
    { "name": "Brussels Sprouts", "link": "https://example.com/brussels_sprouts.jpg" },
    { "name": "Collard Greens", "link": "https://example.com/collard_greens.jpg" },
    { "name": "Endive", "link": "https://example.com/endive.jpg" },
    { "name": "Fennel", "link": "https://example.com/fennel.jpg" },
    { "name": "Garlic", "link": "https://example.com/garlic.jpg" },
    { "name": "Horseradish", "link": "https://example.com/horseradish.jpg" },
    { "name": "Jicama", "link": "https://example.com/jicama.jpg" },
    { "name": "Kohlrabi", "link": "https://example.com/kohlrabi.jpg" },
    { "name": "Okra", "link": "https://example.com/okra.jpg" },
    { "name": "Parsnips", "link": "https://example.com/parsnips.jpg" },
    { "name": "Rutabaga", "link": "https://example.com/rutabaga.jpg" },
    { "name": "Scallions", "link": "https://example.com/scallions.jpg" },
    { "name": "Shallots", "link": "https://example.com/shallots.jpg" },
    { "name": "Snow Peas", "link": "https://example.com/snow_peas.jpg" },
    { "name": "Snap Peas", "link": "https://example.com/snap_peas.jpg" },
    { "name": "Watercress", "link": "https://example.com/watercress.jpg" },
    { "name": "Arugula", "link": "https://example.com/arugula.jpg" },
    { "name": "Mustard Greens", "link": "https://example.com/mustard_greens.jpg" },
    { "name": "Purslane", "link": "https://example.com/purslane.jpg" },
    { "name": "Sorrel", "link": "https://example.com/sorrel.jpg" },
    { "name": "Tatsoi", "link": "https://example.com/tatsoi.jpg" },
    { "name": "Mizuna", "link": "https://example.com/mizuna.jpg" },
    { "name": "Mibuna", "link": "https://example.com/mibuna.jpg" },
    { "name": "Celtuce", "link": "https://example.com/celtuce.jpg" },
    { "name": "Chinese Broccoli", "link": "https://example.com/chinese_broccoli.jpg" },
    { "name": "Chinese Cabbage", "link": "https://example.com/chinese_cabbage.jpg" },
    { "name": "Napa Cabbage", "link": "https://example.com/napa_cabbage.jpg" },
    { "name": "Amaranth Greens", "link": "https://example.com/amaranth_greens.jpg" },
    { "name": "Malabar Spinach", "link": "https://example.com/malabar_spinach.jpg" },
    { "name": "New Zealand Spinach", "link": "https://example.com/new_zealand_spinach.jpg" },
    { "name": "Water Spinach", "link": "https://example.com/water_spinach.jpg" },
    { "name": "Sweet Corn", "link": "https://example.com/sweet_corn.jpg" },
    { "name": "Cereals", "link": "https://example.com/cereals.jpg" },
    { "name": "Maize", "link": "https://example.com/maize.jpg" },
    { "name": "Sorghum", "link": "https://example.com/sorghum.jpg" },
    { "name": "Wheat", "link": "https://example.com/wheat.jpg" },
    { "name": "Barley", "link": "https://example.com/barley.jpg" },
    { "name": "Millet", "link": "https://example.com/millet.jpg" },
    { "name": "Oats", "link": "https://example.com/oats.jpg" },
    { "name": "Rye", "link": "https://example.com/rye.jpg" },
    { "name": "Triticale", "link": "https://example.com/triticale.jpg" },
    { "name": "Quinoa", "link": "https://example.com/quinoa.jpg" },
    { "name": "Amaranth", "link": "https://example.com/amaranth.jpg" },
    { "name": "Buckwheat", "link": "https://example.com/buckwheat.jpg" },
    { "name": "Spelt", "link": "https://example.com/spelt.jpg" },
    { "name": "Teff", "link": "https://example.com/teff.jpg" },
    { "name": "Fonio", "link": "https://example.com/fonio.jpg" },
    { "name": "Kañiwa", "link": "https://example.com/kañiwa.jpg" },
    { "name": "Job’s Tears", "link": "https://example.com/jobs_tears.jpg" },
    { "name": "Wild Rice", "link": "https://example.com/wild_rice.jpg" },
    { "name": "Einkorn", "link": "https://example.com/einkorn.jpg" },
    { "name": "Legumes", "link": "https://example.com/legumes.jpg" },
    { "name": "Beans", "link": "https://example.com/beans.jpg" },
    { "name": "Peas", "link": "https://example.com/peas.jpg" },
    { "name": "Lentils", "link": "https://example.com/lentils.jpg" },
    { "name": "Chickpeas", "link": "https://example.com/chickpeas.jpg" },
    { "name": "Soybeans", "link": "https://example.com/soybeans.jpg" },
    { "name": "Cowpeas", "link": "https://example.com/cowpeas.jpg" },
    { "name": "Pigeon Peas", "link": "https://example.com/pigeon_peas.jpg" },
    { "name": "Lupins", "link": "https://example.com/lupins.jpg" },
    { "name": "Mung Beans", "link": "https://example.com/mung_beans.jpg" },
    { "name": "Black Beans", "link": "https://example.com/black_beans.jpg" },
    { "name": "Navy Beans", "link": "https://example.com/navy_beans.jpg" },
    { "name": "Kidney Beans", "link": "https://example.com/kidney_beans.jpg" },
    { "name": "Fava Beans", "link": "https://example.com/fava_beans.jpg" },
    { "name": "Split Peas", "link": "https://example.com/split_peas.jpg" },
    {
        "name":"Basil",
        "link":"https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.S2iyIgFg4wLmM64kn-TGwwAAAA%26pid%3DApi&f=1&ipt=1566f669c41fe1d5f3d7a3d78266360d69df4ceeabddffe06f3a347962fe455e&ipo=images"
    }
]


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
    print(merged_result)
    body = ft.Column(
            [   ft.Container(height=30),
                TopHeader(page,merged_result[0]['link']),
               ft.Text(
                #    "Predicted Crop: Spinach",
                    f"Predicted Crop: {merged_result[0]['name']}",
                   color=ft.colors.BLACK,
                   size=20),
                    #    ft.dropdown.Option("Spinach", "Spinach"),
                    #     ft.dropdown.Option("Maize", "Maize"),
               ft.Dropdown(
                   
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
               CropInfo(page,margin=10,changes=merged_result[0]['probability']),
               
            ]
        )
    body  = ft.Container(
        width=370,
        height=720,
        # bgcolor=ft.colors.RED_200,
        content=body
    )
    return body