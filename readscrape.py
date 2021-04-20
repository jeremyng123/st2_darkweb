import pandas as pd
import re  # regex

marijuana = [
    'bhang', 'bomb chron', 'bud', 'cheeba', 'chronic', 'dank', 'ditch weed',
    'endo', 'fire', 'flower', 'ganja', 'the good', 'green', 'herb',
    'hippe lettuce', 'hybrid', 'indica', 'kaya', 'killer bud',
    'laughing grass', 'mary jane', 'medical', 'mids', 'mota', 'nug',
    'pakololo', 'purps', 'reefer', 'sativa', 'sensimilla', 'sticky icky',
    'sungrown', 'tea', 'tree', 'treefer', 'wacky tobacky', 'yerba'
]

data = pd.read_csv("kilos_scrape.csv")
# print(data)
vendor = {}
for i, j in data.iterrows():
    vendor[j["vendor"]] = 0
    if j["items_sold"] == ' ':
        continue
    for weed in marijuana:
        vendor[j["vendor"]] += len(
            re.findall(weed, j["items_sold"], re.IGNORECASE))
numOfMarijuanVendor = 0
vendors = []
itemsSoldByVendor = []
for k, v in vendor.items():
    if v != 0:
        # print(k, v)
        vendors.append(k)
        itemsSoldByVendor.append(v)
        numOfMarijuanVendor += 1
print(
    f"[INFO]: There are {numOfMarijuanVendor} marijuana/weed/cannabis vendors")

topvendor = ""
top = 0
for i in itemsSoldByVendor:
    if i > top:
        top = i
topvendor = vendors[top]
print(
    f"[INFO]: The vendor that has the most marijuana listed - {top} - is {topvendor}"
)
