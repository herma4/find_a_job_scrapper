import pandas as pd

def to_csv(data):
    df = pd.DataFrame(data)
    df.to_csv("jobs.csv", index=False)