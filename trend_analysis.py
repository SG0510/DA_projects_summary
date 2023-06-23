from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=10, timeout=(5,10))
kw_list = ["Blockchain","bitcoin"]
pytrends.build_payload(kw_list,cat=0,timeframe='today 12-m',geo = '',gprop= '')

df = pytrends.interest_over_time()
print(df.head())

# df = pytrends.get_historical_interest(kw_list,year_start=2021, month_start=1, day_start= 1, hour_start= 0, year_end=2021, month_end= 1, day_end=10, hour_end= 0,)
# df =df.reset_index()
# print(df.head())