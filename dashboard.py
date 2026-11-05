#!/usr/bin/env python3
"""
On-Chain Analytics Dashboard Starter
Network activity metrics, transaction visualizations, wallet exploration,
historical trends. Uses publicly available data or demonstration datasets.
Clear source attribution required.
"""

import json
import os
from datetime import datetime, timedelta
from typing import Dict, List

def get_network_metrics(network: str = "ethereum") -> Dict:
    """Placeholder for public API data (e.g., Etherscan, CoinGecko)."""
    demos = {
        "ethereum": {"active_addresses": 500000, "daily_transactions": 1200000, "gas_avg": 20},
        "base": {"active_addresses": 150000, "daily_transactions": 400000, "gas_avg": 0.1},
        "polygon": {"active_addresses": 200000, "daily_transactions": 300000, "gas_avg": 50}
    }
    data = demos.get(network.lower(), demos["ethereum"])
    data["network"] = network
    data["source"] = "Demonstration dataset - replace with real public API (attribute source)"
    return data

def get_historical_trends(network: str = "ethereum", days: int = 7) -> List[Dict]:
    base = 1000000 if network == "ethereum" else 300000
    trends = []
    for i in range(days):
        date = (datetime.utcnow() - timedelta(days=days-i)).strftime("%Y-%m-%d")
        trends.append({
            "date": date,
            "tx_count": base + i * 10000,
            "active_addresses": int(base * 0.4) + i * 5000,
            "source": "demo"
        })
    return trends

def analyze_trends(trends: List[Dict]) -> Dict:
    """Simple trend analysis."""
    if not trends:
        return {}
    txs = [t["tx_count"] for t in trends]
    return {
        "avg_tx": sum(txs) // len(txs),
        "trend_direction": "up" if txs[-1] > txs[0] else "down",
        "change_pct": round((txs[-1] - txs[0]) / txs[0] * 100, 2) if txs[0] else 0
    }

def explore_wallet(address: str, network: str = "ethereum") -> Dict:
    return {
        "address": address,
        "network": network,
        "balance": "0.0 (demo)",
        "tx_count": 42,
        "last_activity": "demo",
        "source": "Public blockchain data (demo - use real RPC/API)"
    }

def prepare_visualization_data(metrics: Dict, trends: List[Dict]) -> Dict:
    """Prepare data structure suitable for Plotly or similar."""
    return {
        "labels": [t["date"] for t in trends],
        "tx_series": [t["tx_count"] for t in trends],
        "metrics_summary": metrics,
        "chart_type": "line"
    }

def main():
    networks = ["ethereum", "base"]
    all_reports = []
    for net in networks:
        metrics = get_network_metrics(net)
        trends = get_historical_trends(net)
        analysis = analyze_trends(trends)
        wallet = explore_wallet("0x0000000000000000000000000000000000000000", net)
        viz = prepare_visualization_data(metrics, trends)
        all_reports.append({
            "network": net,
            "metrics": metrics,
            "trends": trends,
            "analysis": analysis,
            "sample_wallet": wallet,
            "visualization": viz
        })
    
    report = {
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "networks": all_reports,
        "disclaimer": "Demo data. Use real public APIs and attribute sources clearly."
    }
    os.makedirs("output", exist_ok=True)
    with open("output/analytics.json", "w") as f:
        json.dump(report, f, indent=2)
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()
