import pandas as pd
from datetime import datetime, timedelta

df=pd.read_csv('marsWeather.csv')

dates=df['terrestrial_date']
format="%d-%m-%Y"

date_object=[datetime.strptime(date, format) for date in dates]

for i in range(1, len(date_object)):
    expected=date_object[i-1] + timedelta(days=1)
    if date_object[i] != expected:
        print(f"found gap between {date_object[i-1].strftime(format)} and {date_object[i].strftime(format)}")
