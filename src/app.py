import streamlit
import pandas
import numpy
from data import Data
from model import Model
from visualization import Visualize

streamlit.set_page_config(page_title = 'Predicción financiera', layout = 'centered')
streamlit.header('📉 Analista financiero 📈')
streamlit.write('Predice el precio de las acciones para los 5 siguientes días ✍️📊')

ticker: str = streamlit.text_input('Introduce el código de la acción (AAPL, AMZN, TSLA...)', value = 'AAPL').upper()
if streamlit.button('Iniciar predicción'):
    with streamlit.spinner('Descargando y analizando los datos...'):
        financial_data: pandas.DataFrame = Data.get_financial_data(ticker)
        if not financial_data.empty:

            # Pending to improve data processing
            financial_data = Data.process_data(financial_data)

            # Pending to implement machine learning and improve data predictions
            predictions: numpy.ndarray = Model.predict_linear_regression(financial_data)

            Visualize.next_days_predictions(predictions)
            Visualize.linear_graph(financial_data, predictions, ticker)
        else:
            streamlit.error(f'No se han encontrado datos para {ticker}')