import pytest

from scipy import stats


@pytest.mark.parametrize("a,loc,scale,x,exp_pdf", [
    (1., 0, 1., 0.5, 0.6065306597126334),
    (1., 0.2, 1., 0.7, 0.6065306597126334),
    (1., 0.2, 1., 0.5, 0.7408182206817179),
    (1.1, 0, 1., 0.5, 0.5948522183564979),
    (1.1, 0.2, 1., 0.7, 0.5948522183564979),
    (1.1, 0.2, 1., 0.5, 0.6903719013195413),
    (0.9, 0, 1., 0.5, 0.6083155580655996),
    (0.9, 0.2, 1., 0.7, 0.6083155580655996),
    (0.9, 0.2, 1., 0.5, 0.7819386772878384),
    (0.9, 0.2, 1.2, 0.5, 0.6976286342567877)
    ])
def test_pdf(a: float, loc: float, scale: float, x: float, exp_pdf: float):
    assert stats.gamma.pdf(x, a=a, loc=loc, scale=scale) == pytest.approx(expected=exp_pdf, abs=1e-10)


@pytest.mark.parametrize("a,loc,scale,x,exp_cdf", [
    (1., 0, 1., 0.5, 0.3934693402873666),
    (1., 0.2, 1., 0.7, 0.39346934028736646),
    (1., 0.2, 1., 0.5, 0.2591817793182821),
    (1.1, 0, 1., 0.5, 0.3465502275336354),
    (1.1, 0.2, 1., 0.7, 0.3465502275336354),
    (1.1, 0.2, 1., 0.5, 0.21798608841049288),
    (0.9, 0, 1., 0.5, 0.4444064959610267),
    (0.9, 0.2, 1., 0.7, 0.4444064959610267),
    (0.9, 0.2, 1., 0.5, 0.3064068791124165),
    (0.9, 0.2, 1.2, 0.5, 0.26595645375601923)
    ])
def test_cdf(a: float, loc: float, scale: float, x: float, exp_cdf: float):
    assert stats.gamma.cdf(x, a=a, loc=loc, scale=scale) == pytest.approx(expected=exp_cdf, abs=1e-10)


@pytest.mark.parametrize("a,loc,scale,q,exp_ppf", [
    (1., 0, 1., 0.3934693402873666, 0.5),
    (1., 0.2, 1., 0.39346934028736646, 0.7),
    (1., 0.2, 1., 0.2591817793182821, 0.5),
    (1.1, 0, 1., 0.3465502275336354, 0.5),
    (1.1, 0.2, 1., 0.3465502275336354, 0.7),
    (1.1, 0.2, 1., 0.21798608841049288, 0.5),
    (0.9, 0, 1., 0.4444064959610267, 0.5),
    (0.9, 0.2, 1., 0.4444064959610267, 0.7),
    (0.9, 0.2, 1., 0.3064068791124165, 0.5),
    (0.9, 0.2, 1.2, 0.26595645375601923, 0.5)
    ])
def test_ppf(a: float, loc: float, scale: float, q: float, exp_ppf: float):
    assert stats.gamma.ppf(q, a=a, loc=loc, scale=scale) == pytest.approx(expected=exp_ppf, abs=1e-10)
