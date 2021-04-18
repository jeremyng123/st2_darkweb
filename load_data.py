import pandas as pd

col = ["site", "vendor", "timestamp", "product score", "btc value", "comment"]

with open(r"Darkweb data scrape.csv", "r") as f:
    df = pd.read_csv(f, names=col)
    df = df[df["site"].isin(
        ["Apollon", "CannaHome", "Cannazon", "Cryptonia", "Empire",
         "Samsara"])]
    sorted_df = df.sort_values(by="site", ascending=True).dropna()
    sites = sorted(list(sorted_df.site.unique()))
    vendors = sorted(list(sorted_df.vendor.unique()))