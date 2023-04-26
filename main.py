import pandas as pd
import numpy as np
from pathlib import Path

csv_file_path = Path(__file__).parent / "car data.csv"
car_df = pd.read_csv(csv_file_path)

# Show some basic info from df
print(car_df.info(verbose=True))

# Show the first 10 rows
print(car_df.head(10))

# Show the last 10 rows
print(car_df.tail(10))

# Show the number of rows with empty values
print(car_df.isnull().sum())

# Show the Actual/Present selling price for car given a value
print()
car_avg_present_price = car_df[["Car_Name", "Year", "Present_Price"]]
min_val = car_avg_present_price["Year"].min()
max_val = car_avg_present_price["Year"].max()
value_range = int(input(f"[*] See the present value of the what year ({min_val}, {max_val}): "))
for index, info in car_avg_present_price.iterrows():
    if info["Year"] == value_range:
        print("Car Name: " + info["Car_Name"].capitalize(), end=" ")
        print("$", info["Present_Price"])

#Show the number of owners a car had
print()
car_owners = car_df[["Car_Name", "Owner"]]
for index, info in car_owners.iterrows():
    if info["Owner"] > 0:
        print(info["Car_Name"].capitalize(), end=" ")
        print("number of owners: ", info["Owner"])