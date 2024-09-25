import flet as ft

class OnBoarding:
    
    def __init__(self,page:ft.Page):
        self.page = page
        
    
    def Onboarding(self):
        # lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        # lv.controls.append(ft.Text("Onboarding"))
        lv = ft.Column(
            [
                ft.Text(
                    "Change the column height to see how child items wrap onto multiple columns:"
                ),
                ft.Text("middle"),
                ft.Text("Buttom")
            ]
        ),   
        return lv