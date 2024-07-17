import pytest

from scipy import stats


@pytest.mark.parametrize("loc,lbda,x,exp_pdf", [
    (0, 1., 0.5, 0.6065306597126334),
    (0.2, 1., 0.7, 0.6065306597126334),
    (0.2, 1., 0.5, 0.7408182206817179)
    ])
def test_pdf(loc: float, lbda: float, x: float, exp_pdf: float):
    assert stats.expon.pdf(x, loc=loc, scale=1/lbda) == pytest.approx(expected=exp_pdf, abs=1e-10)


@pytest.mark.parametrize("loc,lbda,x,exp_cdf", [
    (0, 1., 0.5, 0.3934693402873666),
    (0.2, 1., 0.7, 0.39346934028736646),
    (0.2, 1., 0.5, 0.2591817793182821)
    ])
def test_cdf(loc: float, lbda: float, x: float, exp_cdf: float):
    assert stats.expon.cdf(x, loc=loc, scale=1/lbda) == pytest.approx(expected=exp_cdf, abs=1e-10)


@pytest.mark.parametrize("loc,lbda,q,exp_ppf", [
    (0, 1., 0.3934693402873666, 0.5),
    (0.2, 1., 0.39346934028736646, 0.7),
    (0.2, 1., 0.2591817793182821, 0.5)
    ])
def test_ppf(loc: float, lbda: float, q: float, exp_ppf: float):
    assert stats.expon.ppf(q, loc=loc, scale=1/lbda) == pytest.approx(expected=exp_ppf, abs=1e-10)
