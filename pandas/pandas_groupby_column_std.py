import pandas as pd
from pandas._libs.tslibs.offsets import MonthEnd

columns = ['year', 'month', 'day', 'conc']
data = [[2014, 1, 1, 2.0],
        [2014, 1, 1, 4.0],
        [2014, 1, 2, 6.0],
        [2014, 1, 2, 8.0],
        [2014, 2, 1, 2.0],
        [2014, 2, 1, 6.0],
        [2014, 2, 2, 10.0],
        [2014, 2, 2, 14.0]]

df = pd.DataFrame(data, columns=columns)
d_avg = df.groupby(['year', 'month', 'day'], as_index=False)['conc'].mean()
m_avg = d_avg.groupby(['year', 'month'], as_index=False)['conc'].mean()
m_avg['datetime'] = pd.to_datetime(m_avg.year.astype(str) + m_avg.month.astype(str), format='%Y%m') + MonthEnd(1)

# m_std = d_avg.groupby(['year', 'month'], as_index=False)['conc'].agg(np.std)
m_std = d_avg.groupby(['year', 'month'], as_index=False)['conc'].std()

print(f'Concentrations:\n{df}\n')
print(f'Daily Average:\n{d_avg}\n')
print(f'Monthly Average:\n{m_avg}\n')
print(f'Standard Deviation:\n{m_std}\n')
