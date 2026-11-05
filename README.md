# On-Chain Analytics Dashboard

Lightweight blockchain analytics dashboard using publicly available or authorized data sources.

## Features

- Multi-network activity metrics (Ethereum, Base, Polygon demos)
- Transaction visualizations data preparation (ready for Plotly)
- Wallet data exploration
- Historical trends with simple trend analysis (direction, average, change %)
- Clear source attribution
- Basic unit tests and CI workflow

Uses real data or clearly labeled demonstration datasets.

## Installation

```bash
git clone https://github.com/demarco2016/onchain-analytics-dashboard.git
cd onchain-analytics-dashboard
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # add RPC or API keys if needed
```

## Usage

```bash
python dashboard.py
python -m unittest test_dashboard.py -v
```

Output written to `output/analytics.json`. Extend to generate HTML/Plotly charts.

## Data Sources

Current implementation uses demonstration data. Replace with public APIs (Etherscan, Alchemy, etc.) and attribute them.
