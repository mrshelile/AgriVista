# import matplotlib
# import matplotlib.pyplot as plt
# import numpy as np

# import flet as ft
# from flet.matplotlib_chart import MatplotlibChart

# # matplotlib.use("svg")

# def MarketAnalysis(page:ft.Page):
#     page.title = "Market Analysis"
#     # Data for months and crop margin performance
#     months = np.arange(1, 13)  # 12 months
#     maize_margin = np.random.uniform(20, 50, 12)  # Simulated margin for maize
#     spinach_margin = np.random.uniform(15, 35, 12)  # Simulated margin for spinach
#     wheat_margin = np.random.uniform(25, 55, 12)  # Simulated margin for wheat

#     fig, ax = plt.subplots()

#     # Plotting the data
#     ax.plot(months, maize_margin, label="Maize", color="tab:green", marker="o")
#     ax.plot(months, spinach_margin, label="Spinach", color="tab:blue", marker="o")
#     ax.plot(months, wheat_margin, label="Wheat", color="tab:orange", marker="o")

#     # Adding labels and title
#     ax.set_xlabel("Months")
#     ax.set_ylabel("Margin Performance (M)")
#     ax.set_title("Simulated Crop Margin Performance Over Months")

#     # Add a legend
#     ax.legend(title="Crops")

#     # Adding the plot to Flet page
#     page.add()
    
#     return MatplotlibChart(MatplotlibChart(fig, expand=True))
import matplotlib.pyplot as plt
import numpy as np
import flet as ft
from flet.matplotlib_chart import MatplotlibChart

def MarketAnalysis(page: ft.Page):
    page.title = "Market Analysis"
    
    # Data for months and crop margin performance
    months = np.arange(1, 13)  # 12 months
    maize_margin = np.random.uniform(20, 50, 12)  # Simulated margin for maize
    spinach_margin = np.random.uniform(15, 35, 12)  # Simulated margin for spinach
    wheat_margin = np.random.uniform(25, 55, 12)  # Simulated margin for wheat

    fig, ax = plt.subplots()

    # Plotting the data
    ax.plot(months, maize_margin, label="Maize", color="tab:green", marker="o")
    ax.plot(months, spinach_margin, label="Spinach", color="tab:blue", marker="o")
    ax.plot(months, wheat_margin, label="Wheat", color="tab:orange", marker="o")

    # Adding labels and title
    ax.set_xlabel("Months")
    ax.set_ylabel("Margin Performance (M)")
    ax.set_title("Simulated Crop Margin Performance Over Months")

    # Add a legend
    ax.legend(title="Crops")

    # Adding the plot to Flet page
    chart = MatplotlibChart(fig, expand=True)
    body = ft.Container(
        height=710,
        width=380,
        # bgcolor=ft.colors.BLUE_900
        content=ft.Column(
            [   ft.Container(height=80),
                ft.Container(
                    margin=ft.margin.only(left=30),
                    content=ft.Text("This chart shows the monthly profit trends for maize, spinach, and wheat—quick insights at a glance!"
                    ,style=ft.TextStyle(color=ft.colors.GREEN_500,weight=ft.FontWeight.W_900,size=20))
                ),chart
            ]
        )
    )
    return body