import yfinance
import pandas

class Data:
    @staticmethod
    def get_financial_data(ticker: str, period: str = '6mo') -> pandas.DataFrame:
        return pandas.DataFrame(yfinance.download(ticker, period = period))
    @staticmethod
    def get_test_data(period: str = '5y') -> pandas.DataFrame:
        return pandas.read_csv(f'src/data/test-data-{period}.csv')
    @staticmethod
    def process_data(financial_data: pandas.DataFrame) -> pandas.DataFrame:
        financial_data = financial_data.reset_index()
        financial_data['target'] = financial_data['Close'].shift(-1)
        
        # Pending aditional processing
        
        financial_data = financial_data.dropna()
        return financial_data