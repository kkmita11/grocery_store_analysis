import pandas as pd

mon_sell = pd.read_csv("../data/SELL_1.csv", encoding="cp1250", sep=";", parse_dates=['Date'])
day_sell = pd.read_csv("../data/Day_sell_24_12_18.csv", encoding="cp1250", sep=";", parse_dates=['Date'])

print(mon_sell.info())
print(day_sell.info())
print(mon_sell.isna().sum())
print(day_sell.isna().sum())
print(day_sell[day_sell['Date'].isna()])
day_sell = day_sell.drop(day_sell.index[-1])

print((day_sell == 0).sum())
print((mon_sell == 0).sum())