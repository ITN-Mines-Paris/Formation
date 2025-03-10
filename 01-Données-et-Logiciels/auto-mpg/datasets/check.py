# Python Standard Library
import hashlib
import json

# Get the dataset checksum info from the references.json file
with open("../references.json", encoding="utf-8") as references:
    bibliography = json.load(references)
    for item in bibliography:
        if item["id"] == "auto_mpg_9":
            auto_mpg_9 = item
            break
    else:
        raise ValueError("auto_mpg_9 reference not found")
hash_info = auto_mpg_9["custom"]["checksum"]

# Check the checksum of the local CSV file
hash = getattr(hashlib, hash_info["type"])()
try:
    bytes = open("auto-mpg.csv", mode="rb").read()
except FileNotFoundError:
    raise FileNotFoundError("auto-mpg.csv file not found")
hash.update(bytes)
if hash.hexdigest() != hash_info["value"]:
    error = f"""auto-mpg.csv checksum mismatch
- expected: {hash_info["value"]}
- actual:   {hash.hexdigest()}"""
    raise ValueError(error)