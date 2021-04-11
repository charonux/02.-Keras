# %%
import numpy as np
import pandas as pd

# %%
data = pd.read_csv('dataset\data.csv')

# %%
data.replace('?', np.nan, inplace=True)
data = data.astype({"age": np.float64, "fare": np.float64})

# %%
