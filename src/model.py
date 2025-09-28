# from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
import numpy
import pandas

class Model:
    # model = None
    @staticmethod
    def predict_linear_regression(financial_data: pandas.DataFrame, days: int = 5) -> numpy.ndarray:
        financial_data['day'] = numpy.arange(len(financial_data))
        model = LinearRegression().fit(
            financial_data[['day']],
            financial_data['Close']
        )
        last_day = financial_data['day'].iloc[-1]
        next_days: numpy.ndarray = numpy.arange(last_day + 1, last_day + days + 1).reshape(-1, 1)
        predictions: numpy.ndarray = model.predict(next_days)
        return predictions.flatten()
    @staticmethod
    def predict_random_forest(financial_data: pandas.DataFrame, days: int = 5) -> pandas.DataFrame:
        # financial_data = financial_data.reset_index()
        # last_close: float = financial_data['Close'].iloc[-1]
        # next_dates = pandas.date_range(financial_data['Date'].iloc[-1], periods=days, freq='D')

        # for date in next_dates:
        #     pass
        pass
        return financial_data
    @staticmethod
    def train_model():
        pass    
    @staticmethod
    def get_model_score():
        pass