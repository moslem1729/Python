import khayyam

print(khayyam.JalaliDatetime.now().daysinmonth)
print(khayyam.JalaliDatetime.now().dayofyear())
print(khayyam.JalaliDatetime.now().weekdayname())
print(khayyam.JalaliDate(1346, 12, 30).weekdayname())


def cdr_partitions(start_date, end_date):
    year_of_start_date = start_date[:4]
    month_of_start_date = start_date[5:7]
    day_of_start_date = start_date[8:10]
    year_of_end_date = end_date[:4]
    month_of_end_date = end_date[5:7]
    day_of_end_date = end_date[8:10]
    print(year_of_end_date)
    print(month_of_end_date)
    print(day_of_end_date)


start_date = '1401/01/20'
end_date = "1401/07/10"
print(cdr_partitions(start_date,end_date))