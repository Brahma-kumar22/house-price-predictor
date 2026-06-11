from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the pre-trained model
with open('house_price_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from form
    size = float(request.form['size'])
    bedrooms = int(request.form['bedrooms'])
    bathrooms = int(request.form['bathrooms'])
    # We will not use the city and budget fields in the prediction for now

    # Prepare the features for prediction (only 3 features: size, bedrooms, bathrooms)
    features = np.array([[size, bedrooms, bathrooms]])

    # Make prediction
    prediction = model.predict(features)
    return render_template('index.html', prediction_text=f'Predicted House Price: ₹{prediction[0]:,.2f}')

if __name__ == "__main__":
    app.run(debug=True)
