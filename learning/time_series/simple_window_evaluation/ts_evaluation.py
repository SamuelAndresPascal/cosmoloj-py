from logging import getLogger

import pandas as pd

LOG = getLogger(__name__)

class TSEvaluation:
    """Evaluation comparée de séries temporelles."""

    def reference_time_label(self) -> str:
        """"""

    def reference_tsid_label(self) -> str:
        """"""

    def reference_tsid_series_computation(self, data: pd.DataFrame) -> pd.Series:
        """"""
        return data[self.reference_tsid_label()]

    def reference_date_series_computation(self, data: pd.DataFrame) -> pd.Series:
        """"""
        return data[self.reference_time_label()]

    def modelisation_time_label(self) -> str:
        """"""

    def modelisation_tsid_label(self) -> str:
        """"""

    def modelisation_tsid_series_computation(self, data: pd.DataFrame) -> pd.Series:
        """"""
        return data[self.modelisation_tsid_label()]

    def modelisation_date_series_computation(self, data: pd.DataFrame) -> pd.Series:
        """"""
        return data[self.modelisation_time_label()]

    def _prepare_reference(self, data: pd.DataFrame) -> pd.DataFrame:

        # calcul des colonnes d'identifiant de série temporelle et de date
        data[self.reference_tsid_label()] = self.reference_tsid_series_computation(data)
        data[self.reference_time_label()] = self.reference_date_series_computation(data)


        return data.sort_values(by=[self.reference_tsid_label(), self.reference_time_label()],
                                axis=0,
                                ascending=True)

    def preprocess_reference(self, data: pd.DataFrame) -> pd.DataFrame:
        return data

    def preprocess_modelisation(self, data: pd.DataFrame) -> pd.DataFrame | pd.Series:
        return data

    def preprocess_modelisation_ts(self, data: pd.DataFrame) -> pd.DataFrame | pd.Series:
        return data[self.modelisation_time_label()]

    def _prepare_modelisation(self, data: pd.DataFrame) -> pd.DataFrame:

        # calcul des colonnes d'identifiant de série temporelle et de date
        data[self.modelisation_tsid_label()] = self.modelisation_tsid_series_computation(data)
        data[self.modelisation_time_label()] = self.modelisation_date_series_computation(data)

        return data.sort_values(by=[self.modelisation_tsid_label(), self.modelisation_time_label()],
                                axis=0,
                                ascending=True)


    def process_ts(self, reference_data: pd.Series, modelisation_data: pd.DataFrame | pd.Series):
        return {
            self.reference_tsid_label(): reference_data[self.reference_tsid_label()],
            self.reference_time_label(): reference_data[self.reference_time_label()]
        }

    def compute(self, raw_reference: pd.DataFrame, raw_modelisation: pd.DataFrame) -> list[pd.DataFrame]:
        LOG.debug("prepare reference data")
        reference_data = self._prepare_reference(data=raw_reference)
        LOG.debug("preprocess reference data")
        reference_data = self.preprocess_reference(data=reference_data)

        LOG.debug("prepare modelisation data")
        modelisation_data = self._prepare_modelisation(data=raw_modelisation)
        LOG.debug("preprocess modelisation data")
        modelisation_data = self.preprocess_modelisation(data=modelisation_data)

        LOG.debug("process group analysis")
        l = []
        for tsid, reference_ts in reference_data.groupby(self.reference_tsid_label()):
            modelisation_ts = self.preprocess_modelisation_ts(
                data=modelisation_data[modelisation_data[self.modelisation_tsid_label()] == tsid])
            l.append(reference_ts.apply(self.process_ts,
                                        axis=1,
                                        result_type='expand',
                                        modelisation_data=modelisation_ts))
        LOG.debug("end of processing")
        return l