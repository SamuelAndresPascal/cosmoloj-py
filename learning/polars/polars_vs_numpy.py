import requests
import numpy as np
import polars as pl
import time
import pandas as pd

# Download the text file
text = requests.get("https://files.rcsb.org/download/3w32.pdb").text

# Turn it into a 2D array of characters
char_tab_np = np.array(text.splitlines()).view(dtype=(str, 1)).reshape(-1, 80)

# Create a polars DataFrame from the numpy array
char_tab_pl = pl.DataFrame(char_tab_np)

char_tab_pd = pd.DataFrame(char_tab_np)

start = time.time_ns()
for i in range(1000):
    # Sort by first column with numpy
    char_tab_np[np.argsort(char_tab_np[:, 0])]
print(time.time_ns() - start)

start = time.time_ns()
for i in range(1000):
    # Sort by first column with polars
    char_tab_pd.sort_values(by=0, axis=1)
print(time.time_ns() - start)

start = time.time_ns()
for i in range(1000):
    # Sort by first column with polars
    char_tab_pl.sort(by="column_0")
print(time.time_ns() - start)
