import pytest

from scipy import stats


@pytest.mark.parametrize("mean,sd,x,exp_pdf", [
    (0, 1., 0.5, 0.3520653267642995),
    (0.2, 1., 0.7, 0.3520653267642995),
    (0.2, 1., 0.5, 0.38138781546052414)
    ])
def test_pdf(mean: float, sd: float, x: float, exp_pdf: float):
    assert stats.norm.pdf(x, loc=mean, scale=sd) == pytest.approx(expected=exp_pdf, abs=1e-10)


@pytest.mark.parametrize("mean,sd,x,exp_cdf", [
    (0, 1., 0.5, 0.6914624612740131),
    (0.2, 1., 0.7, 0.691462461274013),
    (0.2, 1., 0.5, 0.6179114221889526)
    ])
def test_cdf(mean: float, sd: float, x: float, exp_cdf: float):
    assert stats.norm.cdf(x, loc=mean, scale=sd) == pytest.approx(expected=exp_cdf, abs=1e-10)


@pytest.mark.parametrize("mean,sd,q,exp_ppf", [
    (0, 1., 0.6914624612740131, 0.5),
    (0.2, 1., 0.691462461274013, 0.7),
    (0.2, 1., 0.6179114221889526, 0.5)
    ])
def test_ppf(mean: float, sd: float, q: float, exp_ppf: float):
    assert stats.norm.ppf(q, loc=mean, scale=sd) == pytest.approx(expected=exp_ppf, abs=1e-10)
