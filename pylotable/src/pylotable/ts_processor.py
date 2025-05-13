""""""
import pandas as pd


class TSProcessor:
    """"""

    def compute(self, data):
        """"""


class PandasSeriesTSProcessor(TSProcessor):
    """"""

    def preprocess(self, data: pd.Series) -> pd.Series | pd.DataFrame:
        """"""
        return data.sort_values()

    def process(self, data: pd.Series | pd.DataFrame) -> pd.Series | pd.DataFrame:
        """"""

    def compute(self, data: pd.Series) -> pd.Series | pd.DataFrame:
        """"""
        data = self.preprocess(data=data)
        return self.process(data=data)
