# Option Pricing & Volatility Analysis Engine

海外大学院（Master of Financial Engineering / Quantitative Finance）出願用に作成中のクオンツ・ポートフォリオです。
主要なオプション価格決定モデルの実装と、S&P 500 (SPY) 市場データを用いたインプライド・ボラティリティの分析を行っています。

## Project Overview (概要)
- **目的**: 3つの理論モデル（解析解・数値計算解）の比較検証および実市場データを用いたボラティリティ・スマイルの再現
- **主要機能**:
  - Black-Scholes-Merton モデル（解析解）
  - Cox-Ross-Rubinstein (CRR) 二項格子モデル（アメリカン/ヨーロピアン対応）
  - 幾何ブラウン運動 (GBM) に基づくモンテカルロ・シミュレーション
  - ニュートン・ラプソン法を用いたインプライド・ボラティリティ (IV) 逆算エンジン
- **開発言語・環境**: Python 3.10+, NumPy, SciPy, pandas, matplotlib, yfinance

## Project Structure & Progress (進捗状況)
- [x] **Core Pricing Engines (`src/option_pricing/`)**:
  - [x] `black_scholes.py`: BSMモデルによる価格決定とGreeks算出
  - [x] `binomial_tree.py`: CRRモデルによる価格決定と後退解析
  - [x] `monte_carlo.py`: GBMによる数値シミュレーション
  - [x] `implied_vol.py`: Newton-Raphson法によるIVソルバー
- [ ] **Empirical Analysis (`notebooks/`)**:
  - [ ] `01_model_convergence.ipynb`: 二項ツリー・モンテカルロ法のBSモデルへの収束性検証
  - [ ] `02_market_data_comparison.ipynb`: S&P 500 (SPY) オプション実データとの比較
  - [ ] `03_implied_vol_smile.ipynb`: ボラティリティ・スマイル/スキューの分析と可視化
