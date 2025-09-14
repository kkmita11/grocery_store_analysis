import pandas as pd
import numpy as np

mon_sell = pd.read_csv("../data/SELL_1.csv", encoding="cp1250", sep=";")
day_sell = pd.read_csv("../data/Day_sell_24_12_18.csv", encoding="cp1250", sep=";")

print(mon_sell.info())
print(day_sell.info())


mon_sell["Date"] = pd.to_datetime(mon_sell["Date"], format="%d.%m.%Y")
day_sell["Date"] = pd.to_datetime(day_sell["Date"], format="%d.%m.%Y")


mon_cols_to_float = [
    "Pquantity", "pce_zn", "pwa_zn", "pce_sn", "pwa_sn",
    "pce_sb", "pwa_sb", "pudzsb", "pmarza",
    "pmarzajedn", "pkwmarza", "pudzmarza"
]

for col in mon_cols_to_float:
    mon_sell[col] = (
        mon_sell[col]
        .replace(" ", np.nan)
        .str.replace(",", ".", regex=False)
        .astype(float)
    )

print(mon_sell[mon_cols_to_float].describe().round(2))


day_cols_day_float = ["zn", "sb", "tax", "marza"]

for col in day_cols_day_float:
    day_sell[col] = (
        day_sell[col]
        .replace(" ", np.nan)
        .str.replace(",", ".", regex=False)
        .astype(float)
    )

print(day_sell[day_cols_day_float].describe().round(2))


print(mon_sell.isna().sum())
print(mon_sell[mon_sell['pce_zn'].isna()].to_string())
mon_sell = mon_sell.fillna(0)


print(day_sell.isna().sum())
print(day_sell[day_sell['Date'].isna()])
day_sell = day_sell.drop(day_sell.index[361])

duplicates_day = day_sell["Date"].duplicated().sum()
print(f"Liczba duplikatów w day_sell['Date']: {duplicates_day}")


print((day_sell == 0).sum())
print((mon_sell == 0).sum())


shopping_sundays = [
    "31.12.2017",
    "04.03.2018", "25.03.2018", "29.04.2018", "06.05.2018", "27.05.2018",
    "03.06.2018", "24.06.2018", "01.07.2018", "29.07.2018", "05.08.2018",
    "26.08.2018", "02.09.2018", "30.09.2018", "07.10.2018", "28.10.2018",
    "04.11.2018", "25.11.2018", "02.12.2018", "16.12.2018", "23.12.2018", "30.12.2018"
]




day_sell["day"] = day_sell["Date"].dt.day
day_sell["month"] = day_sell["Date"].dt.month
day_sell["year"] = day_sell["Date"].dt.year
day_sell["day_of_week"] = day_sell["Date"].dt.day_name()
day_sell["is_weekend"] = day_sell["Date"].dt.weekday >= 5

shopping_sundays_dt = pd.to_datetime(shopping_sundays, format="%d.%m.%Y")
day_sell["is_shopping_sunday"] = day_sell["Date"].isin(shopping_sundays_dt)


mon_sell["month"] = mon_sell["Date"].dt.month




total_day = day_sell['sb'].sum()
total_mon = mon_sell['pwa_sb'].sum()

total_diff = total_mon - total_day
print("Całkowita różnica:", total_diff)

percent_diff = (total_diff / total_mon) * 100
print("Procentowa różnica wzg mon_sell: {:.2f}%".format(percent_diff))




#mon_sell.to_csv("../data/SELL_1_cleaned.csv", sep=";", encoding="cp1250", index=False)
#day_sell.to_csv("../data/Day_sell_cleaned.csv", sep=";", encoding="cp1250", index=False)

print("Pliki zapisane do CSV.")
