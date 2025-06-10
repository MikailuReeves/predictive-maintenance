# CMAPSS Remaining Useful Life (RUL) Prediction

This project leverages the NASA CMAPSS FD001 dataset to predict the Remaining Useful Life (RUL) of aircraft engines.

---

## 📦 Dataset

- **Dataset:** NASA CMAPSS FD001 subset
- **Features:** 3 operational settings and 21 sensor measurements (some dropped for noise)
- **Target:** Remaining Useful Life (RUL), capped at 125 for stability
- **Splitting:** By engine IDs (no data leakage)

---

## 📊 Notebooks Overview

### 01_data_analysis_and_preprocessing.ipynb
- Loads and cleans CMAPSS FD001 data
- Drops non-informative features
- Adds RUL target per engine cycle
- Visualizes target skew (left-skewed RUL, motivating penalty-focused modeling)

### 02_model_regression_random_forest.ipynb
- Implements a Random Forest baseline model
- Uses standard RMSE as the evaluation metric
- Shows collapse of predictions towards the target mean

### 03_model_classification_xgboost.ipynb
- Builds two XGBoost models:
  - **Standard Model:** `"reg:squarederror"` objective, underpredicts due to skew
  - **Custom Model:** Asymmetric loss penalizing overestimation (safer RUL predictions)
- Visualizes residuals and RUL distributions
- Shows the tradeoff: higher RMSE for custom model, but better risk alignment
---

## 🧩 Planned Next Steps

- [ ] Implement sliding window data transformation for LSTM training.  
- [ ] Build an LSTM model to capture temporal sensor degradation trends.  
- [ ] Visualize LSTM predictions in Power BI dashboards for intuitive analysis.  
- [ ] Explore quantile regression or ensemble blending for robust predictions.

---
# Sources
[CMAPSS Jet Engine Simulated Data](https://data.nasa.gov/dataset/cmapss-jet-engine-simulated-data) 
