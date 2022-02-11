import csv
import matplotlib.pyplot as plt

import pandas as pd

df = pd.read_csv('data/straight_sample_2.csv')

df1 = df.loc[df['Sensor_id_s']==df.iat[2,1]]
df2 = df.loc[df['Sensor_id_s']==df.iat[3,1]]
print(df2)

df1.plot.line(x="Timestamp",figsize=(10,8))
plt.title('move forward (right hand)')

plt.savefig('data/straight_sample_2_right_hand.png')
