import xgboost as xgb


class XGBoost:

    def __init__(self):
        self.model = xgb.XGBRegressor(objective='reg:squarederror', random_state=42, n_estimators=10, max_depth=5)

    def fit(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)