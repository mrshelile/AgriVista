# from tensorflow.keras.models import load_model
# import pandas as pd
# from sklearn.preprocessing import MinMaxScaler,LabelEncoder

# class MarketModel:
#     def __init__(self):
#         data = pd.read_excel("MarketDATA.xlsx")
        
#         self.data =data[data['Date'] < '2024-11-01']
#         self.data['Date'] = pd.to_datetime(self.data['Date'])
#         self.data.set_index('Date', inplace=True)
        
#         self.model = load_model('marketlstm.keras')
    
#     def showSample(self):
#         print(self.data.tail())
        
#     def modelPredict2(self,predicted_crops:list):
#         crops= []
        
#         for crop in predicted_crops:
#             crops.append(crop[0])
        
#         encoder = LabelEncoder()
#         scaler = MinMaxScaler()
#         data = encoder.fit_transform(self.data['Crop'])
#         data1 =self.data
#         data1['Crop_encoded'] = data
#         print(data1[data1['Crop']==crops[0]].iloc[0]['Crop_encoded'])
        
#         for crop in crops:
#             crop_23_data = self.data[self.data['Crop'] == crop].drop(columns=['Crop'])
#             print(crop)
#             if len(crop_23_data) < 12:
#                 continue
#                 # raise ValueError("Not enough data to create a sequence.")
            
#             last_12_months = crop_23_data.tail(12)
#             scaled_last_12_months = scaler.fit_transform(last_12_months)
#             input_data = scaled_last_12_months.reshape((1, scaled_last_12_months.shape[0], scaled_last_12_months.shape[1]))
#             predicted_scaled = self.model.predict(input_data)
#             predicted_values = scaler.inverse_transform(predicted_scaled)
            
#             print(predicted_values)
#         # Dictionary to store encoded values for each crop
#         # Fit the encoder on the entire list of crops
        
        
#         # self.data['Crop_encoded'] = label_encoder.fit_transform(self.data['Crop'])
#         # crop_23_data = self.data[self.data['Crop_encoded'] == 23].drop(columns=['Crop'])
#         # # Check if there is enough data
#         # if len(crop_23_data) < 12:
#         #     raise ValueError("Not enough data to create a sequence.")
        
#         # # Get the last 12 months of data for this crop
#         # last_12_months = crop_23_data.tail(12)
        
#         # # Scale the last 12 months of data
#         # scaled_last_12_months = scaler.fit_transform(last_12_months)
#         # # Reshape for LSTM input (samples, time steps, features)
#         # input_data = scaled_last_12_months.reshape((1, scaled_last_12_months.shape[0], scaled_last_12_months.shape[1]))

#         # # Make prediction
#         # predicted_scaled = self.model.predict(input_data)

#         # # Inverse transform the predicted values
#         # predicted_values = scaler.inverse_transform(predicted_scaled)

#         # # predicted_values
#         # # Assuming you want the prediction for the first target variable (e.g., Market Price)
#         # predicted_value_for_first_target = predicted_values  # Adjust index as needed
#         # print(f'Predicted value for next month (Crop 23): {predicted_value_for_first_target}')

import pickle
import h5py
import pandas as pd
import os
class  MarketModel:
    def __init__(self):
        print("Current Working Directory:", os.getcwd())
        data = pd.read_excel("MarketDATA.xlsx")
        self.data = data
        self.model = None
        self.h5_filename = 'linear_regression_model.h5'
        print(self.data.tail())
    
        
    async def load_model(self):
        with h5py.File(self.h5_filename, 'r') as h5_file:
            model_data = h5_file['model'][()]
            self.model = pickle.loads(model_data)
        
        
    async def modelPredict2(self,predicted_crops:list):
        # Load the model from the file
        pass