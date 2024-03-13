##Import Excel to Python##
##Cleaning Duplicate of Time Release##
import pandas as pd
data = pd.read_excel (r"C:\Users\ANGELA\Downloads\REVOU_Case Study_08032024\Games Sales - Case Study.xlsx")
data['Relaease'] = pd.to_datetime(data['Release'])
data = data.drop_duplicates()
data.head()


## which game is the oldest and the newest games in that dataset##
df =pd.DataFrame(data)
Time=df.sort_values(by=['Release'], ascending=False)
print(Time)

## which publisher published most of the games##
agg_publisher = data.groupby('Publisher', as_index=False)['Name'].nunique()
pub=agg_publisher.sort_values('Name', ascending=False)
print(pub)

## which developer developed most of the games##
agg_dev = data.groupby('Developer', as_index=False)['Name'].nunique()
dev=agg_dev.sort_values('Name', ascending=False)
print(dev)