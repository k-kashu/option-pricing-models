import numpy as np

def crr_binomial_price(S, K, T, r, sigma, n_steps, option_type = "call", american = False):
    """Compute the binomial tree price of a European or American option (no dividends).

    Args:
        S: spot price
        K: strike price
        T: time to maturity, in years
        r: risk-free interest rate, as a decimal
        sigma: volatility, as a decimal
        n_steps: the number of steps
        option_type: 'call' or 'put'
        american: True for an American option, False for a European option

    Returns:
        Theoretical price of the option, as a float.

    Raises:
        ValueError: If any of S, K, T or sigma is less than or equal to 0 or not finite.
        ValueError: If n_steps is less than 1 or not an integer.
        ValueError: If option_type is neither 'call' nor 'put'.
        ValueError: If the risk-neutral probability p is not strictly between 0 and 1 (try a larger n_steps).

    """
    params = [("S", S), ("K", K), ("T", T), ("sigma", sigma)]
    for name, value in params:
        if value <= 0 or not np.isfinite(value):
            raise ValueError(f"{name} must be positive and finite, got {value}")
    if not isinstance(n_steps,(int, np.integer)) or n_steps < 1:
        raise ValueError(f"n_steps must be an integer greater than or equal to 1, got {n_steps}")
    if option_type not in ("call", "put"):
        raise ValueError(f"option_type must be call or put, got {option_type!r}")

    dt = T / n_steps
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    p = (np.exp(r * dt) - d) / (u - d)
    if not 0 < p < 1:
        raise ValueError(f"p must be between 0 and 1 (exclusive), got {p}. Please increase n_steps.")
    disc_factor = np.exp(-r * dt)

    j = np.arange(n_steps + 1)
    S_T = S * u ** j * d ** (n_steps - j)
    if option_type == "call":
        V = np.maximum(S_T - K, 0)
    else:
        V = np.maximum(K - S_T, 0)
    for k in range(n_steps - 1, -1, -1):
        V = disc_factor * (p * V[1:] + (1 - p) * V[:-1])
        if american:
            j_k = np.arange(k + 1)
            S_k = S * u ** j_k * d ** (k - j_k)
            if option_type == "call":
                exercise_k = np.maximum(S_k - K, 0)
            else:
                exercise_k = np.maximum(K - S_k, 0)
            V = np.maximum(V, exercise_k)

    return V[0]


if __name__ == "__main__":

    call_1 = crr_binomial_price(S = 100, K = 100, T = 1, r = 0.05, sigma = 0.2, n_steps = 1)
    print("call_1:",call_1)
    assert abs(call_1 - 12.1623) < 1e-4, f"call_1 should be 12.1623, got {call_1}"
    put_1 = crr_binomial_price(S = 100, K = 100, T = 1, r = 0.05, sigma = 0.2, n_steps = 1, option_type = "put")
    print("put_1:",put_1)
    assert abs(put_1 - 7.2852) < 1e-4, f"put_1 should be 7.2852, got {put_1}"
    call_2 = crr_binomial_price(S = 100, K = 100, T = 1, r = 0.05, sigma = 0.2, n_steps = 2)
    print("call_2:",call_2)
    assert abs(call_2 - 9.5405) < 1e-4, f"call_2 should be 9.5405, got {call_2}"
    put_2 = crr_binomial_price(S = 100, K = 100, T = 1, r = 0.05, sigma = 0.2, n_steps = 2, option_type = "put")
    print("put_2:",put_2)
    assert abs(put_2 - 4.6634) < 1e-4, f"put_2 should be 4.6634, got {put_2}"

    # n=1000: compare with the convergence table (tolerance 1e-4)
    call_1000 = crr_binomial_price(S = 100, K = 100, T = 1, r = 0.05, sigma = 0.2, n_steps = 1000)
    print("call_1000:",call_1000)
    assert abs(call_1000 - 10.4486) < 1e-4, f"call_1000 should be 10.4486, got {call_1000}"
    put_1000 = crr_binomial_price(S = 100, K = 100, T = 1, r = 0.05, sigma = 0.2, n_steps = 1000, option_type = "put")
    print("put_1000:",put_1000)
    assert abs(put_1000 - 5.5715) < 1e-4, f"put_1000 should be 5.5715, got {put_1000}"

    # BS prices from black_scholes.py (benchmark: S=K=100, T=1, r=0.05, sigma=0.2)
    assert abs(call_1000 - 10.4506) < 1e-2, f"call_1000 should be within 0.01 of the BS price 10.4506, got {call_1000}"
    assert abs(put_1000 - 5.5735) < 1e-2, f"put_1000 should be within 0.01 of the BS price 5.5735, got {put_1000}"

    # American options (no dividends)
    am_put_1 = crr_binomial_price(S = 100, K = 100, T = 1, r = 0.05, sigma = 0.2, n_steps = 1, option_type = "put", american = True)
    print("am_put_1:", am_put_1)
    assert abs(am_put_1 - 7.2852) < 1e-4, f"am_put_1 should be 7.2852, got {am_put_1}"
    am_put_2 = crr_binomial_price(S = 100, K = 100, T = 1, r = 0.05, sigma = 0.2, n_steps = 2, option_type = "put", american = True)
    print("am_put_2:", am_put_2)
    assert abs(am_put_2 - 5.7377) < 1e-4, f"am_put_2 should be 5.7377, got {am_put_2}"

    am_call_1000 = crr_binomial_price(S = 100, K = 100, T = 1, r = 0.05, sigma = 0.2, n_steps = 1000, american = True)
    print("am_call_1000:", am_call_1000)
    assert abs(am_call_1000 - call_1000) < 1e-10, f"am_call_1000 should equal the European call (no dividends), got {am_call_1000} vs {call_1000}"
    am_put_1000 = crr_binomial_price(S = 100, K = 100, T = 1, r = 0.05, sigma = 0.2, n_steps = 1000, option_type = "put", american = True)
    print("am_put_1000:", am_put_1000)
    assert abs(am_put_1000 - 6.0896) < 1e-4, f"am_put_1000 should be 6.0896, got {am_put_1000}"
    assert am_put_1000 >= put_1000, f"am_put_1000 ({am_put_1000}) should be >= put_1000 ({put_1000})"

    try:
        crr_binomial_price(S = float('nan'), K = 100, T = 1, r = 0.05, sigma = 0.2, n_steps = 1)
        assert False, "S = float('nan') should raise ValueError"
    except ValueError as e:
        print("got ValueError", e)
    try:
        crr_binomial_price(S = 100, K = 100, T = 1, r = 0.05, sigma = 0.2, n_steps = 0)
        assert False, "n_steps = 0 should raise ValueError"
    except ValueError as e:
        print("got ValueError", e)
    try:
        crr_binomial_price(S = 100, K = 100, T = 1, r = 0.05, sigma = 0.2, n_steps = 1, option_type = "cal")
        assert False, "option_type = 'cal' should raise ValueError"
    except ValueError as e:
        print("got ValueError", e)
    try:
        crr_binomial_price(S = 100, K = 100, T = 1, r = 0.05, sigma = 0.01, n_steps = 1)
        assert False, "p out of range (sigma = 0.01, r = 0.05, n_steps = 1) should raise ValueError"
    except ValueError as e:
        print("got ValueError", e)

    print("all tests passed")