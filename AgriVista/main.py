# # import flet as ft


# # def main(page: ft.Page):
# #     page.title = "Flet counter example"
# #     page.vertical_alignment = ft.MainAxisAlignment.CENTER

# #     txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

# #     def minus_click(e):
# #         txt_number.value = str(int(txt_number.value) - 1)
# #         page.update()

# #     def plus_click(e):
# #         txt_number.value = str(int(txt_number.value) + 1)
# #         page.update()

# #     page.add(
# #         ft.Row(
# #             [
# #                 ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
# #                 txt_number,
# #                 ft.IconButton(ft.icons.ADD, on_click=plus_click),
# #             ],
# #             alignment=ft.MainAxisAlignment.CENTER,
# #         )
# #     )


# # ft.app(main)
# # import flet as ft
# # from app.OnBoarding import Onboarding

# # def main(page: ft.Page):

# #     page.title = "NavigationBar Example"
# #     page.navigation_bar = ft.NavigationBar(
# #         destinations=[
# #             ft.NavigationBarDestination(icon=ft.icons.EXPLORE, label="Explore"),
# #             ft.NavigationBarDestination(icon=ft.icons.COMMUTE, label="Commute"),
# #             ft.NavigationBarDestination(
# #                 icon=ft.icons.BOOKMARK_BORDER,
# #                 selected_icon=ft.icons.BOOKMARK,
# #                 label="Explore",
# #             ),
# #         ]
# #     )
# #     page.add(ft.Text("Body!"))

# # ft.app(main)

# # import flet as ft
# # from app.OnBoarding.Onboarding import  Onboarding
# # def main(page: ft.Page):

# #     page.title = "AgriVista"

# #     col = Onboarding(page)
# #     page.add(col)
# #     page.update()

# # ft.app(main)
# from app.GatherFeatures.GatherFeatures import GatherFeatures
# from app.OnBoarding.Onboarding import  Onboarding
# from constants.colors import *
# from app.home.home import home
# import flet as ft

# def main(page: ft.Page):
#     page.title = "AgriVista"

#     def route_change(route):
#         page.views.clear()
#         page.views.append(
#             ft.View(
#                 "/",
#                 Onboarding(page),   
#                 bgcolor=ft.colors.CYAN_700
#             )
#         )
     
#         if page.route == "/gatherFeatures":
#             page.views.append(
#                 ft.View(
#                     "/gatherFeatures",
#                     GatherFeatures(page),
#                     bgcolor=ft.colors.WHITE
#                 )
#             )
#         if page.route == "/home":
#             page.views.append(
#                 ft.View(
#                     "/home",
#                     home(page),
#                     bgcolor=ft.colors.WHITE
#                 )
#             )
#         page.update()

#     def view_pop(view):
#         page.views.pop()
#         top_view = page.views[-1]
#         page.go(top_view.route)

#     page.on_route_change = route_change
#     page.on_view_pop = view_pop
#     page.go(page.route)

# ft.app(main,)

# import flet as ft
# import h5py
# import joblib
# import numpy as np

# # Load the serialized RandomForestClassifier model from the .h5 file
# def load_model():
#     with h5py.File('crop_prediction.h5', 'r') as hf:
#         model_data = hf['random_forest'][:]
    
#     # Save the buffer back to a .pkl file
#     with open('crop_prediction.pkl', 'wb') as f:
#         f.write(model_data.tobytes())
    
#     # Load the model using joblib
#     return joblib.load('crop_prediction.pkl')

# # Function to make predictions
# def make_prediction(model, input_data):
#     # Prepare the input data as a numpy array for prediction
#     input_data = np.array(input_data).reshape(1, -1)
#     prediction = model.predict(input_data)
#     return prediction[0]

# # Flet app UI and logic
# def main(page: ft.Page):
#     page.title = "Random Forest Classifier Prediction"
    
#     # Load the model
#     model = load_model()
    
#     # TextField for user input
#     input_fields = []
#     for i in range(5):  # Assuming 5 features for the model input
#         input_field = ft.TextField(label=f"Feature {i+1}", width=200)
#         input_fields.append(input_field)
    
#     # Label to display the result
#     result_label = ft.Text(value="", color=ft.colors.BLACK)
    
#     # Function to handle the predict button click
#     def predict_click(e):
#         try:
#             # Get inputs from user and convert to a list of floats
#             # input_data = [float(field.value) for field in input_fields]
#             input_data = [[21.3,444,7.9,47.6,6,2,2]]
#             # Call the prediction function
#             prediction = make_prediction(model, input_data)
            
#             # Display the result
#             result_label.value = f"Prediction: {prediction}"
#             result_label.update()
#         except ValueError:
#             result_label.value = "Invalid input! Please enter numeric values."
#             result_label.update()
    
#     # Predict button
#     predict_button = ft.ElevatedButton(text="Predict", on_click=predict_click)
    
#     # Add components to the page
#     page.add(
#         ft.Column(
#             [
#                 ft.Text("Enter feature values for prediction:", size=20),
#                 *input_fields,  # Unpack the input fields
#                 predict_button,
#                 result_label,
#             ],
#             alignment=ft.MainAxisAlignment.CENTER,
#             horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#         )
#     )

# ft.app(target=main)
    
