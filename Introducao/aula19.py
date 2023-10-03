from datetime import timedelta, datetime
from dateutil.relativedelta import relativedelta

def years_to_months(years):
    return years * 12

delta = relativedelta(years=5)
start_date = datetime(2020,12,20)
end_date = start_date + delta
period = years_to_months(5)


print(f'the payment will be finished in {period} months')

loan_value = 1000000

parcel_value = 1000000 / period

date = start_date
relative_month = relativedelta(months=1)
for month in range(period):
    print(f'Parcel {month+1}: ', 'R$', round(parcel_value, 2), date.strftime('%d/%m/%Y') )
    date += relative_month

