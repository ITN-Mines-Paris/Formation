# Python Standard Library
import json

# Third-Party Libraries
import pandas as pd
import requests

# Get the URL of the CSV file from the references.json file
with open("../bibliography/references.json", encoding="utf-8") as references:
    bibliography = json.load(references)
    for item in bibliography:
        if item["id"] == "auto_mpg_9":
            auto_mpg_9 = item
            break
    else:
        raise ValueError("auto_mpg_9 reference not found")
csv_url = auto_mpg_9["URL"]
assert csv_url.endswith(".csv")

# Store the CSV file as a local file
with open("auto-mpg.csv", mode="wt", encoding="utf-8") as csv_file:
    response = requests.get(csv_url)
    response.raise_for_status()
    csv_file.write(response.text)

# Data cleaning:
# - Store weights as float64, not int64
# - Replace region integer codes with explicit strings (USA, Europe, Japan)
# - Store the cleaned-up data frame as a Parquet file   
df = pd.read_csv("auto-mpg.csv")
df["weight"] = df["weight"].astype("float64") 
origin_map = {1: "USA", 2: "Europe", 3: "Japan"}
df["origin"] = df["origin"].map(origin_map)
df["origin"] = pd.Categorical(df["origin"])
df.to_parquet("auto-mpg.parquet", index=False)
