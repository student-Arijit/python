import pandas as pd

df = pd.read_csv('temp.csv')

last = df.index[-1]
for i in range(last):
    string=df['Date'].iloc[i]

    month=string[0:2]
    date=string[3:5]
    year=string[6:10]

    new_date=date + "-" + month + "-" + year

    df.loc[i, 'Date'] = new_date

df.to_csv('temp.csv', index=False)
