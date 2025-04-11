from predict_batch import predict_from_csv

df_results = predict_from_csv("data/raw/test_FD003.txt", "data/processed/test_FD003_predictions.csv", is_raw=True)
df_results2 = predict_from_csv("data/processed/feature_engineered_FD001.csv", "data/processed/predicted_risks.csv")
