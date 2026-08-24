import csv, json

def load_csv(path, model):
    out = []
    with open(path) as f:
        r = csv.DictReader(f)
        for row in r:
            out.append({
                "time": row.get("validTime", ""),
                "model": model,
                "tmp850": float(row.get("value", 0))
            })
    return out

gfs = load_csv("gfs_850.csv", "GFS")
icon = load_csv("icon_850.csv", "ICON")

combined = gfs + icon

with open("docs/850mb.json", "w") as f:
    json.dump(combined, f)
