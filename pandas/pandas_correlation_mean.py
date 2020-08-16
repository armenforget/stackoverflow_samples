import pandas as pd
import numpy as np

rs = np.random.RandomState(0)
correlation_matrices = []
for _ in range(10):
    df = pd.DataFrame(rs.rand(3, 3))
    correlation_matrices.append(df.corr())

grouped_matrices = pd.concat(correlation_matrices).groupby(level=0)
mean_corr = grouped_matrices.mean()
std_corr = grouped_matrices.std()

print(mean_corr)
print(std_corr)
