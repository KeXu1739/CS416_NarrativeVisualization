import numpy as np
import pandas as pd
import os

if __name__ == "__main__":
    filepath = os.path.abspath(r".\ThrowbackDataThursday Week 10 - US Recorded Music Revenues by Format.csv")
    df = pd.read_csv(filepath)
    df_new = df.loc[(df["Units"]> 0) & (df["Revenue"]> 0) & (df["Revenue (Inflation Adjusted)"]> 0), :]
    df_new.rename(columns={"Revenue (Inflation Adjusted)":"Revenue_Inf_Adj"}, inplace=True)

    df_new.to_csv(r".\US_Recorded_Music_Revenues_by_Format_filtered.csv", index=False)
