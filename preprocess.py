import pandas as pd

df = pd.read_csv("./GRE_vocab.csv")

df["Learn"] = 0
df["Test"] = 0
df["Wrong"] = 0
df["Mymeaning"] = ""

df.to_csv("./GRE_vocab_1.csv")

print(df)