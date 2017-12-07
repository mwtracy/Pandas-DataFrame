
import pandas as pd

import numpy as np


dates = pd.date_range('20160101', periods=6)
df = pd.DataFrame(np.arange(24).reshape(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])

df['E'] = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20160101', periods=6))

print df
print df.iloc[0, 2]

df1 = pd.DataFrame(np.arange(12).reshape(3, 4))

# print df1

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20171205'),
                    'C': pd.Series(1, index=list(range(4))),
                    'D': np.array([3]*4, dtype='int32'),
                    'E': pd.Categorical(['train', 'test', 'train', 'test']),
                    'F': 'foo'
                    })
# print df2

# print df2.T

