from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from random import random


def scale_rates_from_date(input_array, from_date, scaling_factor):
    output_rates = [
        rate * scaling_factor if date >= from_date else rate
        for date, rate in input_array
    ]
    # output_dates=[date for date,rate in input_array]
    # return list(zip(output_dates,output_rates))
    return output_rates


start_date = datetime.strptime("1/1/2023", "%d/%m/%Y")
# print(start_date)
# shift_period=timedelta(days=60)
# new_start_date=start_date+shift_period
# print(new_start_date)
# another_new_start_date=start_date+relativedelta(months=1)
# print(another_new_start_date)
dates_arr = []
values_arr = []
for i in range(12):
    dates_arr.append(start_date + relativedelta(months=i))
    values_arr.append(random())

# for date,rate in zip(dates_arr,values_arr):
#   print(date, rate)
# print(list(zip(dates_arr,values_arr)))
# print(values_arr)

scaled = scale_rates_from_date(list(zip(dates_arr, values_arr)),
                               datetime(2023, 5, 1), 1.05)

# scaled=[rate*1.03 if date>datetime(2023,5,1) else rate for date,rate in list(zip(dates_arr,values_arr)) ]
# for date,rate in scaled:
#   print(date, rate)

for date, old_rate, new_rate in zip(dates_arr, values_arr, scaled):
    print(date, old_rate, new_rate)
