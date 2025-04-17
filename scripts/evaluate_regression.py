from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

def evaluate_regression(y_true, y_pred, label="Validation"):
    """_summary_

    Args:
        y_true (_type_): True values for the target variable.
        y_pred (_type_): Predicted values for the target variable.
        label (str, optional): _description_. The label to use in the print statements. Defaults to "Validation".
    """
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)
    
    print(f"{label} MAE:  {mae:.2f}")
    print(f"{label} RMSE: {rmse:.2f}")
    print(f"{label} R²:   {r2:.2f}")