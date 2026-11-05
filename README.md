# On-Chain Analytics Dashboard

Lightweight blockchain analytics dashboard using publicly available or authorized data sources.

## Features

- Network activity metrics
- Transaction visualizations (extend with Plotly)
- Wallet data exploration
- Historical trends
- Clear source attribution

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
```

Output written to `output/analytics.json`. Extend to generate HTML/Plotly charts.

## Data Sources

Current implementation uses demonstration data. Replace with public APIs (Etherscan, Alchemy, etc.) and attribute them.
