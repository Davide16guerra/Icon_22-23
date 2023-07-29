from sklearn.neighbors import KNeighborsRegressor

class KNN:

    def __init__(self):
        self.model = KNeighborsRegressor(n_neighbors=6)

    def fit(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)