import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
import pickle

# Load the dataset
data = pd.read_csv('house_prices.csv')

# Features and target variable
X = data[['size', 'bedrooms', 'bathrooms']]  # Features
y = data['price']                             # Target variable

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = XGBRegressor()
model.fit(X_train, y_train)

# Save the model
with open('house_price_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved as house_price_model.pkl")
