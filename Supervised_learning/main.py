import csv
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import ModelAnalysis
import pandas as pd

import RandomForest
import XGBoost
import KNN


def categorical_feature_encoding(dataset):
    # Effettua il one-hot encoding
    onehot_encoder = OneHotEncoder(sparse_output=False)
    return onehot_encoder.fit_transform(dataset)


# legge dati da file .csv
Xdata = []
ydata = []
with open('..\Datasets\ds_salaries_usd+clusters.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        Xrow = row[:2] + row[3:]
        Xdata.append(Xrow)

        yrow = row[2]
        ydata.append(float(yrow))

    file.close()

# codifica feature categoriche
df = pd.DataFrame(Xdata)
encoded_Xdata = categorical_feature_encoding(df)

# trasformazione dataset e target in matrici numpy
X = np.array(encoded_Xdata)
y = np.array(ydata)

# divisione in train e test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# addestramento e predizioni della random forest
rf = RandomForest.RandomForest()
rf.fit(X_train, y_train)
y_rf_prediction = rf.predict(X_test)

# valutazione prestazioni random forest
ma = ModelAnalysis.ModelAnalisis()
print("Random forest parameters:")
print("MSE: ", ma.mean_squared_error(y_test, y_rf_prediction))
print("MAE: ", ma.mean_absolute_error(y_test, y_rf_prediction))
print("MdAE: ", ma.median_absolute_error(y_test, y_rf_prediction))
print("R2-score: ", ma.r2_score(y_test, y_rf_prediction))
# ma.scatter_plot(y_test, y_rf_prediction)

# addestramento e predizioni del XGBoost
xgb = XGBoost.XGBoost()
xgb.fit(X_train, y_train)
y_xgb_prediction = xgb.predict(X_test)

# valutazione prestazioni XGBoost
print("\nXGBoost parameters:")
print("MSE: ", ma.mean_squared_error(y_test, y_xgb_prediction))
print("MAE: ", ma.mean_absolute_error(y_test, y_xgb_prediction))
print("MdAE: ", ma.median_absolute_error(y_test, y_xgb_prediction))
print("R2-score: ", ma.r2_score(y_test, y_xgb_prediction))
# ma.scatter_plot(y_test, y_xgb_prediction)

# addestramento e predizioni KNN
knn = KNN.KNN()
knn.fit(X_train, y_train)
y_knn_prediction = knn.predict(X_test)

# valutazione prestazioni KNN
print("\nKNN parameters:")
print("MSE: ", ma.mean_squared_error(y_test, y_knn_prediction))
print("MAE: ", ma.mean_absolute_error(y_test, y_knn_prediction))
print("MdAE: ", ma.median_absolute_error(y_test, y_knn_prediction))
print("R2-score: ", ma.r2_score(y_test, y_knn_prediction))
# ma.scatter_plot(y_test, y_knn_prediction)
