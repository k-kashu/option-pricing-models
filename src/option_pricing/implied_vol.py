import sys
from pathlib import Path
import numpy as np
from scipy.stats import norm

# プロジェクトルート (src フォルダの親ディレクトリ) を検索パスに追加
project_root = str(Path(__file__).resolve().parent.parent)
if project_root not in sys.path:
    sys.path.append(project_root)

from option_pricing.black_scholes import BlackScholesModel


class ImpliedVolatilitySolver:
    """
    Implied Volatility Solver using Newton-Raphson Algorithm.
    """
    def __init__(self, S: float, K: float, T: float, r: float):
        self.S = S
        self.K = K
        self.T = T
        self.r = r

    def _vega(self, sigma: float) -> float:
        """BSモデルのVega (ボラティリティに対する感応度) を計算"""
        d1 = (np.log(self.S / self.K) + (self.r + 0.5 * sigma ** 2) * self.T) / (sigma * np.sqrt(self.T))
        return self.S * norm.pdf(d1) * np.sqrt(self.T)

    def calculate_iv(self, market_price: float, option_type: str = "call", tol: float = 1e-5, max_iter: int = 100) -> float:
        """
        Newton-Raphson法によるIVの逆算
        ---------------------------------
        market_price : float : 市場のオプション価格
        option_type  : str   : "call" または "put"
        tol          : float : 収束判定の許容誤差
        max_iter     : int   : 最大反復回数
        """
        # 初期値 sigma0 = 20%
        sigma = 0.20
        
        for _ in range(max_iter):
            bs = BlackScholesModel(self.S, self.K, self.T, self.r, sigma)
            price = bs.call_price() if option_type.lower() == "call" else bs.put_price()
            
            diff = price - market_price
            if abs(diff) < tol:
                return sigma
            
            vega = self._vega(sigma)
            if vega < 1e-8:
                break
                
            # ニュートン・ラプソン法の更新式: sigma_new = sigma - diff / vega
            sigma = sigma - diff / vega

        return np.nan  # 収束しなかった場合は NaN を返す


if __name__ == "__main__":
    # テスト: BSモデルで σ=0.25 (25%) とした時のCall価格 (12.7516) から、逆に25%を導出できるか検証
    solver = ImpliedVolatilitySolver(S=100.0, K=100.0, T=1.0, r=0.05)
    target_price = 12.7516
    estimated_iv = solver.calculate_iv(market_price=target_price, option_type="call")
    print(f"Target Price: {target_price}")
    print(f"Estimated IV: {estimated_iv:.4f} (Expected: 0.2500)")