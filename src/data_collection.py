import requests
import pandas as pd
import time
import os

INDICATORS = {
    "NY.GDP.MKTP.KD.ZG": "gdp_growth",
    "FP.CPI.TOTL.ZG": "inflation",
    "SL.UEM.TOTL.ZS": "unemployment",
    "GC.DOD.TOTL.GD.ZS": "govt_debt_pct_gdp",
    "NE.TRD.GNFS.ZS": "trade_pct_gdp",
    "NY.GDP.PCAP.KD": "gdp_per_capita"
}

def fetch_indicator(indicator_code, indicator_name):
    url = f"https://api.worldbank.org/v2/country/all/indicator/{indicator_code}"
    params = {"format": "json", "per_page": 20000, "mrv": 24}
    response = requests.get(url, params=params)
    data = response.json()
    if len(data) < 2 or not data[1]:
        return pd.DataFrame()
    records = []
    for entry in data[1]:
        if entry["value"] is not None and entry["countryiso3code"]:
            records.append({
                "country_code": entry["countryiso3code"],
                "country_name": entry["country"]["value"],
                "year": int(entry["date"]),
                indicator_name: entry["value"]
            })
    return pd.DataFrame(records)

def collect_all():
    dfs = []
    for code, name in INDICATORS.items():
        print(f"Fetching: {name}")
        df = fetch_indicator(code, name)
        dfs.append(df)
        time.sleep(1)
    merged = dfs[0]
    for df in dfs[1:]:
        merged = pd.merge(merged, df, on=["country_code", "country_name", "year"], how="outer")
    os.makedirs("data/raw", exist_ok=True)
    merged.to_csv("data/raw/world_bank_raw.csv", index=False)
    print(f"Saved {len(merged)} rows to data/raw/world_bank_raw.csv")
    return merged

if __name__ == "__main__":
    collect_all()