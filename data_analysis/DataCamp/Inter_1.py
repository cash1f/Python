# -*- coding: utf-8 -*-

import pandas as pd

dt_cars = pd.read_csv("cars.csv", index_col=0)

# Create car_maniac: observations that have a cars_per_cap over 500
cpc = dt_cars['cars_per_cap']
many_cars = cpc > 500
# many_cars
car_maniac = dt_cars[many_cars]
# Print car_maniac
print(car_maniac)
