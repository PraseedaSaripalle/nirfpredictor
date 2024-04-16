import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge

def train_model(data):
    # Split data into X and y
    X = data.drop(columns=['Rank'])
    y = data['Rank']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize models with specified parameters
    rf_model = RandomForestRegressor(n_estimators=100, max_depth=None, random_state=42)
    lr_model = LinearRegression()
    gbm_model = GradientBoostingRegressor(n_estimators=100, max_depth=3, learning_rate=0.1, random_state=42)
    svr_model = SVR(kernel='rbf')
    lasso_model = Lasso(alpha=0.1, fit_intercept=True, normalize=False, max_iter=1000, tol=0.0001, selection='cyclic')
    ridge_model = Ridge(alpha=0.1, fit_intercept=True, normalize=False, max_iter=None, tol=0.001, solver='auto')

    # Train each model
    rf_model.fit(X_train, y_train)
    lr_model.fit(X_train, y_train)
    gbm_model.fit(X_train, y_train)
    svr_model.fit(X_train, y_train)
    lasso_model.fit(X_train, y_train)
    ridge_model.fit(X_train,y_train)

    # Evaluate each model
    rf_mse = mean_squared_error(y_test, rf_model.predict(X_test))
    lr_mse = mean_squared_error(y_test, lr_model.predict(X_test))
    gbm_mse = mean_squared_error(y_test, gbm_model.predict(X_test))
    svr_mse = mean_squared_error(y_test, svr_model.predict(X_test))
    lasso_mse = mean_squared_error(y_test, lasso_model.predict(X_test))
    ridge_mse=mean_squared_error(y_test, ridge_model.predict(X_test))

    # Store models and their MSE in a dictionary
    models = {
        'Random Forest': {'model': rf_model, 'mse': rf_mse},
        'Linear Regression': {'model': lr_model, 'mse': lr_mse},
        'Gradient Boosting': {'model': gbm_model, 'mse': gbm_mse},
        'Support Vector Machine': {'model': svr_model, 'mse': svr_mse},
        'Lasso Model': {'model': lasso_model, 'mse': lasso_mse},
        'Ridge Model':{'model': ridge_model, 'mse': ridge_mse}
    }

    return models

def predict_rank(models, input_data, X_test, y_test):
    results = {'Algorithm Used': [], 'Predicted Rank': [], 'Mean Squared Error': [], 'Accuracy': []}
    for name, model_data in models.items():
        model = model_data['model']
        predicted_rank = model.predict(input_data)[0]
        predicted_rank = np.round(predicted_rank)  # Round to the nearest integer
        predicted_rank = np.clip(predicted_rank, 1, 100)  # Clip values to be within range 1-100
        mse = model_data['mse']
        accuracy = r2_score(y_test, model.predict(X_test))  # Calculate R^2 score as accuracy
        results['Algorithm Used'].append(name)
        results['Predicted Rank'].append(predicted_rank)
        results['Mean Squared Error'].append(mse)
        results['Accuracy'].append(accuracy)
    result_df = pd.DataFrame(results)
    return result_df

def load_dataset(file_path):
    # Load dataset
    data = pd.read_csv(file_path)
    return data

    
    return data
def load_dataset(file_path):
    # Load dataset
    data = pd.read_csv(file_path)
    return data
