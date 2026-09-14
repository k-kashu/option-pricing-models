# Option Pricing & Volatility Analysis
### オプション価格決定モデルとボラティリティ分析

This repository provides Python implementations of core option pricing models (Black-Scholes, Binomial Tree, Monte Carlo) and implied volatility analysis using S&P 500 (SPY) option market data.  
（主要なオプション価格決定モデルの実装と、S&P 500 オプションデータを用いたインプライド・ボラティリティ分析を行うリポジトリです。）

> Developed as part of preparation for graduate studies in Quantitative Finance / Financial Engineering.  
> （金融工学・クオンツ分野の修士課程出願・研究準備として作成しています。）

---

## 🎯 Overview / 概要

The objective of this project is twofold:
1. **Model Convergence**: Compare numerical methods (Binomial Tree & Monte Carlo) with the Black-Scholes analytical solution.
2. **Empirical Analysis**: Extract implied volatility smiles/skews from SPY option data using the Newton-Raphson method.

（本プロジェクトの目的は以下の2点です：）
1. **モデルの収束性検証**: 二項ツリー法・モンテカルロ法がBlack-Scholes解析解へどのように収束するかを比較・検証。
2. **実証分析**: ニュートン・ラプソン法を用いてSPYオプションデータからインプライド・ボラティリティ・スマイル／スキューを抽出。

---

##  Implemented Modules / 実装モジュール一覧

### Core Engines (`src/option_pricing/`)
- **`black_scholes.py`**: Black-Scholes European option pricing & Greeks ($\Delta, \Gamma, \ Vega, \Theta, \rho$).  
  （BSモデルによる欧州型オプション価格およびギリシャ指標の算出）
- **`binomial_tree.py`**: Cox-Ross-Rubinstein (CRR) tree for European and American options.  
  （CRR二項ツリーモデルによる欧州・米州型オプション価格算出）
- **`monte_carlo.py`**: Option pricing via Geometric Brownian Motion (GBM) simulation.  
  （幾何ブラウン運動に基づくモンテカルロ・シミュレーション）
- **`implied_vol.py`**: Implied volatility solver using the Newton-Raphson method.  
  （ニュートン・ラプソン法によるインプライド・ボラティリティ逆算エンジン）

### Empirical Analysis (`notebooks/`)
- **`01_model_convergence.ipynb`**: Convergence rate analysis (Binomial steps & Monte Carlo paths vs. BSM).  
  （ステップ数・パス数に応じたBSモデルへの収束速度の可視化）
- **`02_market_data_comparison.ipynb`**: Fetching SPY option chains via `yfinance` and benchmark testing.  
  （`yfinance` を用いたSPYオプションデータの取得とモデル適合）
- **`03_implied_vol_smile.ipynb`**: Plotting volatility smiles/skews across different maturities.  
  （満期別のボラティリティ・スマイル／スキューの可視化）


## Project Architecture & Roadmap / 構成と進捗

```text
option-pricing-models/
├── src/option_pricing/       # Core Pricing Engines / 計算エンジン
│   ├── black_scholes.py      # BSM Analytical Pricing [Completed / 完了]
│   ├── binomial_tree.py      # CRR Binomial Tree Solver [Completed / 完了]
│   ├── monte_carlo.py        # GBM Monte Carlo Engine [Completed / 完了]
│   └── implied_vol.py        # Newton-Raphson IV Solver [Completed / 完了]
│
├── notebooks/                # Empirical Analysis / 実証分析・可視化
│   ├── 01_model_convergence.ipynb    # Tree & MC Convergence [In Progress / 進行中]
│   ├── 02_market_data_comparison.ipynb # SPY Option Chain Calibration [Planned / 予定]
│   └── 03_implied_vol_smile.ipynb    # Volatility Smile/Skew [Planned / 予定]
│
└── README.md                 # Project Documentation / ドキュメント
