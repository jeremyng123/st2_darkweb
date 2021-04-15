from soup_scrape import *
import pandas as pd

col = ["site", "vendor", "timestamp", "product score", "btc value", "comment"]
RECON1 = "http://recon222tttn4ob7ujdhbn3s4gjre7netvzybuvbq2bcqwltkiqinhad.onion/"
RECON2 = "http://reconponydonugup.onion"
KILOS = "http://dnmugu4755642434.onion"
WIKIURL = "http://wikitjerrta4qgz4.onion"

# with open(r"Darkweb data scrape.csv", "r") as f:
#     df = pd.read_csv(f, names=col)
#     df = df[df["site"].isin(
#         ["Apollon", "CannaHome", "Cannazon", "Cryptonia", "Empire",
#          "Samsara"])]
#     sorted_df = df.sort_values(by="site", ascending=True).dropna()
#     sites = sorted(list(sorted_df.site.unique()))
#     vendors = sorted(list(sorted_df.vendor.unique()))


def startScraping(url):
    res = getRequest(url)
    soup = getSoup(res)
    print(soup.prettify())


startScraping(RECON1)
# print(vendors)