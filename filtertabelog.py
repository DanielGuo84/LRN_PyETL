import pandas as pd
df = pd.read_csv("tabelog.csv", encoding="utf-8")
print(df[df["價錢"] <= 5000])
df[df["價錢"] <= 5000].to_csv("tabelogfilter.csv",
                              encoding="utf-8",
                              index=False)