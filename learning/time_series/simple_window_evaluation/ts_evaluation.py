from datetime import timedelta
from logging import getLogger

import pandas as pd

LOG = getLogger(__name__)

class TSEvaluation:
    """Evaluation comparée de séries temporelles."""

    def reference_date_label(self) -> str:
        """"""

    def reference_tsid_label(self) -> str:
        """"""

    def reference_tsid_series_computation(self, data: pd.DataFrame) -> pd.Series:
        """"""
        return data[self.reference_tsid_label()]

    def reference_date_series_computation(self, data: pd.DataFrame) -> pd.Series:
        """"""
        return data[self.reference_date_label()]

    def reference_observation_window(self) -> (timedelta, timedelta):
        """"""

    def reference_validation_window(self) -> (timedelta, timedelta):
        """"""

    def modelisation_date_label(self) -> str:
        """"""

    def modelisation_tsid_label(self) -> str:
        """"""

    def modelisation_tsid_series_computation(self, data: pd.DataFrame) -> pd.Series:
        """"""
        return data[self.modelisation_tsid_label()]

    def modelisation_date_series_computation(self, data: pd.DataFrame) -> pd.Series:
        """"""
        return data[self.modelisation_date_label()]

    def _prepare_reference(self, raw_data: pd.DataFrame) -> pd.DataFrame:

        data = pd.DataFrame(data=raw_data, copy=True)

        # calcul des colonnes d'identifiant de série temporelle et de date
        data[self.reference_tsid_label()] = self.reference_tsid_series_computation(data)
        data[self.reference_date_label()] = self.reference_date_series_computation(data)


        return data.sort_values(by=[self.reference_tsid_label(), self.reference_date_label()],
                                axis=0,
                                ascending=True)

    def _compute_reference_windows(self, data: pd.DataFrame) -> (pd.Series, pd.Series, pd.Series, pd.Series):
        date_col = data[self.reference_date_label()]
        obs_inf, obs_sup = self.reference_observation_window()
        val_inf, val_sup = self.reference_validation_window()
        return date_col - obs_inf, date_col + obs_sup, date_col - val_inf, date_col + val_sup

    def _prepare_modelisation(self, raw_data: pd.DataFrame) -> pd.DataFrame:

        data = pd.DataFrame(data=raw_data, copy=True)

        # calcul des colonnes d'identifiant de série temporelle et de date
        data[self.modelisation_tsid_label()] = self.modelisation_tsid_series_computation(data)
        data[self.modelisation_date_label()] = self.modelisation_date_series_computation(data)

        return data.sort_values(by=[self.modelisation_tsid_label(), self.modelisation_date_label()],
                                axis=0,
                                ascending=True)

    def _by_row(self, reference_data, model_dates):
        obs = model_dates[model_dates.between(reference_data['obs_inf'], reference_data['obs_sup'])]  # 3s
        val = obs[obs.between(reference_data['val_inf'], reference_data['val_sup'])]  # 3s
        return [reference_data[self.reference_tsid_label()],
                reference_data[self.reference_date_label()],
                len(obs),
                len(val)]

    def compute(self, raw_reference: pd.DataFrame, raw_modelisation: pd.DataFrame) -> pd.DataFrame:
        LOG.debug("prepare reference data")
        reference_data = self._prepare_reference(raw_data=raw_reference)
        LOG.debug("compute reference data windows")
        obs_inf, obs_sup, val_inf, val_sup = self._compute_reference_windows(data=reference_data)
        reference_data['obs_inf'] = obs_inf
        reference_data['obs_sup'] = obs_sup
        reference_data['val_inf'] = val_inf
        reference_data['val_sup'] = val_sup

        LOG.debug("prepare modelisation data")
        modelisation_data = self._prepare_modelisation(raw_data=raw_modelisation)

        LOG.debug("process group analysis")
        l = []
        for tsid, group in reference_data.groupby(self.reference_tsid_label()):
            modelisation_dates = modelisation_data[modelisation_data[self.modelisation_tsid_label()] == tsid]
            modelisation_dates = modelisation_dates[self.modelisation_date_label()]
            l.append(group.apply(self._by_row,
                                 axis=1,
                                 result_type='expand',
                                 model_dates=modelisation_dates))
        LOG.debug("concat group results")
        return pd.concat(l)