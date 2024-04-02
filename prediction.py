import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def train_model(data):
    # Split the data into features and target variable
    X = data.drop(columns=['Rank'])
    y = data['Rank']

    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize dictionary to store trained models and evaluation metrics
    models = {}

    # Train Random Forest model
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    rf_y_pred = rf_model.predict(X_test)
    models['Random Forest'] = {'model': rf_model, 'mse': mean_squared_error(y_test, rf_y_pred)}

    # Train Linear Regression model
    lr_model = LinearRegression()
    lr_model.fit(X_train, y_train)
    lr_y_pred = lr_model.predict(X_test)
    models['Linear Regression'] = {'model': lr_model, 'mse': mean_squared_error(y_test, lr_y_pred)}

    return models

import pandas as pd

def predict_rank(models, input_data):
    results = {'Algorithm Used': [], 'Predicted Rank': [], 'Mean Squared Error': []}
    for name, model_data in models.items():
        model = model_data['model']
        predicted_rank = model.predict(input_data)[0]
        predicted_rank = np.clip(predicted_rank, 1, 100)
        mse = model_data['mse']
        results['Algorithm Used'].append(name)
        results['Predicted Rank'].append(predicted_rank)
        results['Mean Squared Error'].append(mse)
    result_df = pd.DataFrame(results)
    return result_df


def load_dataset(file_path):
    # Load dataset
    data = pd.read_csv(file_path)
    return data
