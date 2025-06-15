import pandas as pd
from datetime import datetime

df=pd.read_csv("marsWeather.csv")
date_format="%d-%m-%Y"

new_df=[datetime.strptime(date, date_format) for date in df['terrestrial_date']]
new_df.sort()
sorted_date=[dt.strftime(date_format) for dt in new_df]
df["terrestrial_date"]=sorted_date

df.to_csv('marsWeather.csv')
