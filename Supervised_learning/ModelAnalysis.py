from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, median_absolute_error
import matplotlib.pyplot as plt
import seaborn as snp


class ModelAnalisis:

    def __init__(self):
        pass

    def mean_squared_error(self, y_test, y_pred):
        return mean_squared_error(y_test, y_pred)

    def mean_absolute_error(self, y_test, y_pred):
        return mean_absolute_error(y_test, y_pred)

    def median_absolute_error(self, y_test, y_pred):
        return median_absolute_error(y_test, y_pred)

    def r2_score(self, y_test, y_pred):
        return r2_score(y_test, y_pred)

    def scatter_plot(self, y_test, y_pred):
        residuals = y_pred - y_test
        snp.scatterplot(x=y_test, y=residuals)
        plt.show()
