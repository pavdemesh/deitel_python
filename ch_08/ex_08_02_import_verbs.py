import pandas as pd
import numpy as np


d = pd.read_csv("ex_08_02_verbs.txt", sep="\t", names=["infinitiv", "Xuita", "Buita", "Third Person", "Srakota"])

c = np.array(d["Third Person"])
print(c.size)
