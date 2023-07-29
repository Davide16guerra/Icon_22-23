from sklearn.ensemble import RandomForestRegressor


class RandomForest:

    def __init__(self):
        self.model = RandomForestRegressor(random_state=42, max_depth=4, n_estimators=4)

    def fit(self, X_train, y_train):
                self.model.fit(X_train, y_train)

    def predict(self, X_test):
        y_predictions = self.model.predict(X_test)

        return y_predictions