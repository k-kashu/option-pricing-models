import numpy as np
from scipy.stats import norm

def bs_price(S, K, T, r, sigma, option_type = 'call'):
    """Compute the Black-Scholes price of a European option (no dividends).

    Args:
        S: spot price
        K: strike price
        T: time to maturity, in years
        r: risk-free interest rate, as a decimal
        sigma: volatility, as a decimal
        option_type: 'call' or 'put'

    Returns:
        Theoretical price of the option, as a float.

    Raises:
        ValueError: If any of S, K, T or sigma is less than or equal to 0.
        ValueError: If option_type is neither 'call' nor 'put'.

    """
    params = [("S", S), ("K", K), ("T", T), ("sigma", sigma)]
    for name, value in params:
        if value <= 0:
            raise ValueError(f"{name} must be positive, got {value}")

    d1 = (np.log(S / K) + (r + (sigma ** 2)/2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    if option_type == 'call':
        return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError(f"Unexpected value: {option_type}")

if __name__ == "__main__":
    S = 100
    K = 100
    T = 1
    r = 0.05
    sigma = 0.2
    c = bs_price(S = 100, K = 100, T = 1, r = 0.05, sigma = 0.2, option_type = 'call')
    c_2 = bs_price(S = 100, K = 100, T = 1, r = 0.05, sigma = 0.3, option_type = 'call')
    p = bs_price(S = 100, K = 100, T = 1, r = 0.05, sigma = 0.2, option_type = 'put')

    print("the price of call:", c)
    assert abs(c - 10.4506) < 1e-4, f"call price should be 10.4506, got {c}"
    print("the price of put:", p)
    assert abs(p - 5.5735) < 1e-4, f"put price should be 5.5735, got {p}"
    print("call - put:", c - p)
    assert abs((c - p) - (S - K * np.exp(-r * T))) < 1e-10, "put-call parity violated"
    print("the price of call(sigma = 0.3)", c_2)
    assert abs(c_2 - 14.2313) < 1e-4, f"call price (sigma=0.3) should be 14.2313, got {c_2}"


    try:
        bs_price(S = -100, K = 100, T = 1, r = 0.05, sigma = 0.2, option_type = 'call')
        assert False, "S = -100 should raise ValueError"
    except ValueError as e:
        print("got ValueError:",e)
    try:
        bs_price(S = 100, K = -100, T = 1, r = 0.05, sigma = 0.2, option_type = 'call')
        assert False, "K = -100 should raise ValueError"
    except ValueError as e:
        print("got ValueError:",e)
    try:
        bs_price(S = 100, K = 100, T = 0, r = 0.05, sigma = 0.2, option_type = 'call')
        assert False, "T = 0 should raise ValueError"
    except ValueError as e:
        print("got ValueError:",e)
    try:
        bs_price(S = 100, K = 100, T = 1, r = 0.05, sigma = 0, option_type = 'call')
        assert False, "sigma = 0 should raise ValueError"
    except ValueError as e:
        print("got ValueError:",e)
    try:
        bs_price(S = 100, K = 100, T = 1, r = 0.05, sigma = 0.2, option_type = 'cal')
        assert False, "invalid option_type should raise ValueError"
    except ValueError as e:
        print("got ValueError:",e)
    print("all tests passed")