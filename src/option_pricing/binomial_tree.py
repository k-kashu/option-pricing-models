import numpy as np

class BinomialTreeModel:
    """
    Binomial Tree (Cox-Ross-Rubinstein / CRR) Option Pricing Model.
    Supports both European and American options.
    """
    def __init__(self, S: float, K: float, T: float, r: float, sigma: float, N: int = 100):
        """
        Parameters:
        -----------
        S : float : Current stock price (原資産価格)
        K : float : Strike price (権利行使価格)
        T : float : Time to maturity in years (残存期間 [年])
        r : float : Risk-free interest rate (無リスク金利)
        sigma : float : Volatility (ボラティリティ)
        N : int : Number of time steps (分割ステップ数, デフォルト: 100)
        """
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self.N = N

        # 1ステップあたりの時間間隔
        self.dt = T / N
        # 上昇率 (u), 下落率 (d), リスク中立確率 (p) の計算 (CRR仕様)
        self.u = np.exp(sigma * np.sqrt(self.dt))
        self.d = 1.0 / self.u
        self.p = (np.exp(r * self.dt) - self.d) / (self.u - self.d)
        # 1ステップあたりの割引因子
        self.discount = np.exp(-r * self.dt)

    def call_price(self, option_type: str = "european") -> float:
        """
        Calculate Call Option Price
        option_type: "european" or "american"
        """
        # 1. 満期時点 (ステップ N) の株価一覧を作成
        # [S*u^N, S*u^(N-1)*d, ..., S*d^N]
        j = np.arange(self.N, -1, -1)
        st_prices = self.S * (self.u ** j) * (self.d ** (self.N - j))
        
        # 2. 満期時点でのコールオプションのペイオフ max(S - K, 0)
        values = np.maximum(0, st_prices - self.K)
        
        # 3. 後退解析 (Backward Induction)
        for i in range(self.N - 1, -1, -1):
            # 1ステップ前の期中株価
            j = np.arange(i, -1, -1)
            st_prices = self.S * (self.u ** j) * (self.d ** (i - j))
            
            # 期待値を割り引いた継続価値 (Continuation Value)
            values = self.discount * (self.p * values[:-1] + (1 - self.p) * values[1:])
            
            # アメリカン・オプションの場合は「途中権利行使」の価値と比較
            if option_type.lower() == "american":
                values = np.maximum(values, st_prices - self.K)
                
        return values[0]

    def put_price(self, option_type: str = "european") -> float:
        """
        Calculate Put Option Price
        option_type: "european" or "american"
        """
        j = np.arange(self.N, -1, -1)
        st_prices = self.S * (self.u ** j) * (self.d ** (self.N - j))
        
        # 満期時点でのプットオプションのペイオフ max(K - S, 0)
        values = np.maximum(0, self.K - st_prices)
        
        for i in range(self.N - 1, -1, -1):
            j = np.arange(i, -1, -1)
            st_prices = self.S * (self.u ** j) * (self.d ** (i - j))
            
            values = self.discount * (self.p * values[:-1] + (1 - self.p) * values[1:])
            
            if option_type.lower() == "american":
                values = np.maximum(values, self.K - st_prices)
                
        return values[0]

if __name__ == "__main__":
    # BSモデルと同条件でテスト (S=100, K=100, T=1年, r=5%, sigma=20%, N=1000ステップ)
    model = BinomialTreeModel(S=100.0, K=100.0, T=1.0, r=0.05, sigma=0.20, N=1000)
    print(f"European Call Price: {model.call_price('european'):.4f}")
    print(f"American Call Price: {model.call_price('american'):.4f}")
    print(f"European Put Price:  {model.put_price('european'):.4f}")
    print(f"American Put Price:  {model.put_price('american'):.4f}")