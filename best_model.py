import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
#import xgboost as xgb
from sklearn.metrics import accuracy_score, classification_report
from imblearn.over_sampling import SMOTE
import numpy as np
from sklearn.svm import SVC
from imblearn.over_sampling import RandomOverSampler
# Load the Excel data
data = pd.read_excel('Finally crop pridiction.xlsx')
data.shape

# Check for missing values and encode categorical variables
label_encoder = LabelEncoder()
data['Wind_encoded'] = label_encoder.fit_transform(data['Wind'])
data['Soil Type_encoded'] = label_encoder.fit_transform(data['Soil Type'])
data['crop_encoded'] = label_encoder.fit_transform(data['Crop'])

# Prepare features and target variable
X = data.drop(columns=['Wind', 'Soil Type', 'Crop', 'crop_encoded'])
y = data['crop_encoded']

# Data Augmentation: Noise Injection
def add_noise(X, noise_level=0.1):
    noisy_data = X.copy()
    noise = np.random.normal(0, noise_level, noisy_data.shape)
    noisy_data += noise
    return noisy_data

# Augment the dataset with noise
X_noisy = add_noise(X)
X_augmented = np.vstack((X, X_noisy))
y_augmented = np.hstack((y, y))


# Optional: Apply SMOTE to balance the classes
ros = RandomOverSampler(random_state=42)
X_ros, y_ros = ros.fit_resample(X_augmented, y_augmented)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_ros, y_ros, test_size=0.4, random_state=42)

# Train and evaluate Random Forest Classifier
print("Training Random Forest Classifier...")
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Predict on the test set
y_pred_rf = rf_model.predict(X_test)

# Calculate accuracy
accuracy_rf = accuracy_score(y_test, y_pred_rf)
print(f"Random Forest Classifier Accuracy: {accuracy_rf:.2f}")

# Optional: Print classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred_rf))
