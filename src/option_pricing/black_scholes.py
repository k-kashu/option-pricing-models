import numpy as np
from scipy.stats import norm

class BlackScholesModel:
    """
    Black-Scholes-Merton Option Pricing Model for European Options.
    """
    def __init__(self, S: float, K: float, T: float, r: float, sigma: float):
        """
        Parameters:
        -----------
        S : float : Current stock price (原資産価格)
        K : float : Strike price (権利行使価格)
        T : float : Time to maturity in years (残存期間 [年])
        r : float : Risk-free interest rate (無リスク金利)
        sigma : float : Volatility of the underlying asset (ボラティリティ)
        """
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma

    def _d1(self) -> float:
        return (np.log(self.S / self.K) + (self.r + 0.5 * self.sigma ** 2) * self.T) / (self.sigma * np.sqrt(self.T))

    def _d2(self) -> float:
        return self._d1() - self.sigma * np.sqrt(self.T)

    def call_price(self) -> float:
        """Calculate European Call Option Price"""
        d1 = self._d1()
        d2 = self._d2()
        return self.S * norm.cdf(d1) - self.K * np.exp(-self.r * self.T) * norm.cdf(d2)

    def put_price(self) -> float:
        """Calculate European Put Option Price"""
        d1 = self._d1()
        d2 = self._d2()
        return self.K * np.exp(-self.r * self.T) * norm.cdf(-d2) - self.S * norm.cdf(-d1)

if __name__ == "__main__":
    # 動作確認用テスト (S=100, K=100, T=1年, r=5%, sigma=20%)
    model = BlackScholesModel(S=100.0, K=100.0, T=1.0, r=0.05, sigma=0.20)
    print(f"Call Price: {model.call_price():.4f}")
    print(f"Put Price:  {model.put_price():.4f}")