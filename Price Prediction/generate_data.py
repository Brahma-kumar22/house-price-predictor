import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic data
num_samples = 1000
sizes = np.random.randint(500, 3500, size=num_samples)  # Size in square feet
bedrooms = np.random.randint(1, 6, size=num_samples)      # Number of bedrooms
bathrooms = np.random.randint(1, 4, size=num_samples)     # Number of bathrooms
prices = sizes * 10000 + bedrooms * 500000 + bathrooms * 300000 + np.random.randint(200000, 500000, size=num_samples)

# Create a DataFrame
data = pd.DataFrame({
    'size': sizes,
    'bedrooms': bedrooms,
    'bathrooms': bathrooms,
    'price': prices
})

# Save the dataset to a CSV file
data.to_csv('house_prices.csv', index=False)
print("Dataset created: house_prices.csv")
