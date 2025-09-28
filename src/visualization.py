import streamlit
from matplotlib import pyplot
import numpy
import pandas

class Visualize:
    @staticmethod
    def next_days_predictions(predictions: numpy.ndarray, days: int = 5):
        dates = numpy.arange(
            numpy.datetime64('today'),
            numpy.datetime64('today') + numpy.timedelta64(days, 'D'), 
            numpy.timedelta64(1, 'D')
        )
        streamlit.subheader('📅 Predicción para los próximos 5 días:')
        streamlit.table(pandas.DataFrame({
            'Fecha': [str(date) for date in dates],
            'Valor estimado (USD)': [f'${value:.2f}' for value in predictions]
        }))
    @staticmethod
    def linear_graph(financial_data: pandas.DataFrame, predictions: numpy.ndarray, ticker: str):
        figure, axis = pyplot.subplots(figsize=(10, 4))
        pyplot.title(f'Precio de cierre de {ticker}')
        axis.set_ylabel('Precio (USD)')
        axis.set_xlabel('Fecha')
        axis.grid(True)
        prediction_dates = pandas.date_range(
            financial_data['Date'].iloc[-1] + numpy.timedelta64(0, 'D'),
            periods=len(predictions)
        )
        pyplot.plot(financial_data['Date'], financial_data['Close'], label='Histórico')
        pyplot.plot(prediction_dates, predictions, label='Predicción')
        axis.legend()
        streamlit.pyplot(figure)
    @staticmethod
    def bar_graph(financial_data: pandas.DataFrame, predictions: numpy.ndarray):
        pass