# Option Pricing & Volatility Analysis Engine
### オプション価格決定モデルおよびボラティリティ分析エンジン

An end-to-end quantitative finance portfolio implementing analytical and numerical option pricing models, alongside implied volatility analysis on real market data (S&P 500 / SPY).  
（主要なオプション価格決定モデルの解析解・数値解の実装、および S&P 500 オプション実データを用いたインプライド・ボラティリティ分析を行うクオンツ・ポートフォリオです。）

> **Note / 補足**: Developed as part of academic preparation for Master's applications in Quantitative Finance / Financial Engineering (MFE).  
> （海外大学院の金融工学・クオンツ・ファイナンス修士課程［MFE / MSc in Quantitative Finance］出願用に作成中のプロジェクトです。）

---

## Project Overview / プロジェクト概要
- **Objective / 目的**: Implement core option pricing engines from scratch and analyze numerical convergence against the Black-Scholes analytical solution, followed by empirical volatility smile/skew extraction using market data.  
  （基幹となるオプション価格決定エンジンを一から実装し、解析解への数値的収束性を検証。さらに実市場データを用いたボラティリティ・スマイル／スキューの抽出を行います。）
- **Key Features / 主要機能**:
  - **Black-Scholes-Merton Model**: Closed-form analytical solution and Greeks calculation ($\Delta, \Gamma, \ Vega, \Theta, \rho$).  
    （BSMモデルによる解析解およびギリシャ指標の算出）
  - **Cox-Ross-Rubinstein (CRR) Binomial Tree**: Multi-period lattice solver supporting both European and American options.  
    （CRR二項格子モデルによる多段階価格決定／ヨーロピアン・アメリカン両対応）
  - **Monte Carlo Simulation**: Stochastic path generation under Geometric Brownian Motion (GBM) with vectorized NumPy operations.  
    （幾何ブラウン運動に基づくモンテカルロ法／NumPyベクトル化処理）
  - **Implied Volatility Solver**: Newton-Raphson numerical optimization engine for extracting market implied volatility.  
    （ニュートン・ラプソン法を用いたIV逆算エンジン）
- **Tech Stack / 技術スタック**: Python 3.10+, NumPy, SciPy, pandas, Matplotlib, yfinance.

---

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
