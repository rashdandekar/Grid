from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from numpy import interp
# from random import random
import math


def scale_cums_to_target_from_date(input_arr, from_date, target_cum):
    scaling_factor = target_cum / input_arr[-1][1]
    output_cums = [
        cum * scaling_factor if date >= date_from else cum
        for date, cum in input_arr
    ]
    return output_cums


start_date = datetime(2023, 1, 1)
start_rate = 5000
decline_rate = 0.0028

dates_arr = [start_date + relativedelta(months=i) for i in range(60)]

# for date in dates_arr:
#   print(date)

rates_arr = [
    start_rate * math.exp(-decline_rate * (date - dates_arr[0]).days)
    for date in dates_arr
]

# for date,rate in zip(dates_arr,rates_arr):
#   print(date, rate)
cum_arr = []
cum_arr.append(0)
for i in range(1, 60):
    cum_arr.append(cum_arr[i - 1] +
                   (dates_arr[i] - dates_arr[i - 1]).days * rates_arr[i - 1])

# for date,rate,cum in zip(dates_arr,rates_arr,cum_arr):
#   print(date, rate, cum)
input_arr = list(zip(dates_arr, cum_arr))

# print(input_arr[-1][1])

date_from = datetime(2023, 1, 1)
target_cum = 2.0e6
days_from_start = [(date - dates_arr[0]).days for date in dates_arr]
scaling_factor = target_cum / cum_arr[-1]
scaled_arr = [
    cum * scaling_factor if date >= date_from else cum
    for date, cum in zip(dates_arr, cum_arr)
]
scaled_arr_fn = scale_cums_to_target_from_date(input_arr, date_from,
                                               target_cum)
for date, cum, scaled_cum, scaled_cum_fn in zip(dates_arr, cum_arr, scaled_arr,
                                                scaled_arr_fn):
    print(date, cum, scaled_cum, scaled_cum_fn)
