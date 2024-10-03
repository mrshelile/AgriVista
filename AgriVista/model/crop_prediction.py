import h5py
import joblib
import numpy as np

class CropPrediction:
    
    def __init__(self) -> None:
        self.path1 = "crop_prediction.h5"
        self.path2 = "crop_prediction.pkl"
        self.model = None
        self.top_3_crops = None
    
    async def load_model(self):
        with h5py.File(self.path1, 'r') as hf:
            model_data = hf['random_forest'][:]
    
        # Save the buffer back to a .pkl file
        with open(self.path2, 'wb') as f:
            f.write(model_data.tobytes())
            self.model = joblib.load(self.path2)
            
    async def make_prediction(self, input_data):
        # Prepare the input data as a numpy array for prediction
        input_data = np.array(input_data)
        crop_names = self.model.classes_
        predicted_probs = self.model.predict_proba(input_data)
        probabilities = predicted_probs[0]
        top_3_indices = probabilities.argsort()[-3:][::-1]
        top_3_crops = [(crop_names[i], probabilities[i]) for i in top_3_indices]
        
        self.top_3_crops = top_3_crops

# import h5py
# import joblib
# import numpy as np
# import asyncio
# from concurrent.futures import ThreadPoolExecutor

# class CropPrediction:
    
#     def __init__(self) -> None:
#         self.path1 = "crop_prediction.h5"
#         self.path2 = "crop_prediction.pkl"
#         self.model = None
#         self.top_3_crops = None
#         self.executor = ThreadPoolExecutor()

#     async def load_model(self):
#         loop = asyncio.get_event_loop()
#         await loop.run_in_executor(self.executor, self._load_model)

#     def _load_model(self):
#         with h5py.File(self.path1, 'r') as hf:
#             model_data = hf['random_forest'][:]
        
#         # Save the buffer back to a .pkl file
#         with open(self.path2, 'wb') as f:
#             f.write(model_data.tobytes())
        
#         self.model = joblib.load(self.path2)

#     async def make_prediction(self, input_data):
#         loop = asyncio.get_event_loop()
#         self.top_3_crops = await loop.run_in_executor(self.executor, self._make_prediction, input_data)

#     def _make_prediction(self, input_data):
#         # Prepare the input data as a numpy array for prediction
#         input_data = np.array(input_data)
#         crop_names = self.model.classes_
#         predicted_probs = self.model.predict_proba(input_data)
#         probabilities = predicted_probs[0]
#         top_3_indices = probabilities.argsort()[-3:][::-1]
#         top_3_crops = [(crop_names[i], probabilities[i]) for i in top_3_indices]
        
#         return top_3_crops

# Usage example:
# async def main():
#     crop_predictor = CropPrediction()
#     await crop_predictor.load_model()
#     predictions = await crop_predictor.make_prediction(input_data)
#     print(predictions)
#
# asyncio.run(main())
