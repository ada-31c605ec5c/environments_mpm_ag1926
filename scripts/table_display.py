import pandas as pd
from envtest import pandas_table

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
columns = ['A', 'B', 'C']

table = pandas_table(data, columns)
print(table)