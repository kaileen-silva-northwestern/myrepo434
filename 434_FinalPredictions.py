#!/usr/bin/env python
# coding: utf-8

# In[26]:


from azureml.opendatasets import NycTlcGreen
import pandas as pd

from datetime import datetime
from dateutil.relativedelta import relativedelta


# In[27]:


green_taxi_df = pd.DataFrame([])
start = datetime.strptime("1/1/2016","%m/%d/%Y")
end = datetime.strptime("1/31/2016","%m/%d/%Y")

for sample_month in range(12):
    temp_df_green = NycTlcGreen(start + relativedelta(months=sample_month), end + relativedelta(months=sample_month))         .to_pandas_dataframe()
    green_taxi_df = green_taxi_df.append(temp_df_green.sample(2000))
    
green_taxi_df.head(10)


# In[28]:


def build_time_features(vector):
    pickup_datetime = vector[0]
    month_num = pickup_datetime.month
    day_of_month = pickup_datetime.day
    day_of_week = pickup_datetime.weekday()
    hour_of_day = pickup_datetime.hour
    country_code = "US"
    
    return pd.Series((month_num, day_of_month, day_of_week, hour_of_day, country_code))

green_taxi_df[["month_num", "day_of_month","day_of_week", "hour_of_day", "country_code"]] = green_taxi_df[["lpepPickupDatetime"]].apply(build_time_features, axis=1)
green_taxi_df.head(10)


# In[29]:


columns_to_remove = ["lpepDropoffDatetime", "puLocationId", "doLocationId", "extra", "mtaTax",
                     "improvementSurcharge", "tollsAmount", "ehailFee", "tripType", "rateCodeID", 
                     "storeAndFwdFlag", "paymentType", "fareAmount", "tipAmount"
                    ]
for col in columns_to_remove:
    green_taxi_df.pop(col)
    
green_taxi_df = green_taxi_df.rename(columns={"lpepPickupDatetime": "datetime"})
green_taxi_df["datetime"] = green_taxi_df["datetime"].dt.normalize()
green_taxi_df.head(5)


# In[30]:


from azureml.opendatasets import PublicHolidays
# call default constructor to download full dataset
holidays_df = PublicHolidays().to_pandas_dataframe()
holidays_df.head(5)


# In[31]:


holidays_df = holidays_df.rename(columns={"countryRegionCode": "country_code", "date": "datetime"})
holidays_df["datetime"] = holidays_df["datetime"].dt.normalize()
holidays_df.pop("countryOrRegion")
holidays_df.pop("holidayName")

taxi_holidays_df = pd.merge(green_taxi_df, holidays_df, how="left", on=["datetime", "country_code"])
taxi_holidays_df.head(5)


# In[32]:


from azureml.opendatasets import NoaaIsdWeather

weather_df = pd.DataFrame([])
start = datetime.strptime("1/1/2016","%m/%d/%Y")
end = datetime.strptime("1/31/2016","%m/%d/%Y")

for sample_month in range(12):
    tmp_df = NoaaIsdWeather(cols=["temperature", "precipTime", "precipDepth", "snowDepth"], start_date=start + relativedelta(months=sample_month), end_date=end + relativedelta(months=sample_month))        .to_pandas_dataframe()
    print("--weather downloaded--")
    
    # filter out coordinates not in NYC to conserve memory
    tmp_df = tmp_df.query("latitude>=40.53 and latitude<=40.88")
    tmp_df = tmp_df.query("longitude>=-74.09 and longitude<=-73.72")
    print("--filtered coordinates--")
    weather_df = weather_df.append(tmp_df)
    
weather_df.head(10)


# In[33]:


weather_df["datetime"] = weather_df["datetime"].dt.normalize()
weather_df.pop("usaf")
weather_df.pop("wban")
weather_df.pop("longitude")
weather_df.pop("latitude")

# filter out NaN
weather_df = weather_df.query("temperature==temperature")

# group by datetime
aggregations = {"snowDepth": "mean", "precipTime": "max", "temperature": "mean", "precipDepth": "max"}
weather_df_grouped = weather_df.groupby("datetime").agg(aggregations)
weather_df_grouped.head(10)


# In[34]:


taxi_holidays_weather_df = pd.merge(taxi_holidays_df, weather_df_grouped, how="left", on=["datetime"])
taxi_holidays_weather_df.describe()


# In[122]:


final_df = taxi_holidays_weather_df.query("pickupLatitude>=40.53 and pickupLatitude<=40.88")
final_df = final_df.query("pickupLongitude>=-74.09 and pickupLongitude<=-73.72")
final_df = final_df.query("tripDistance>0 and tripDistance<75")
final_df = final_df.query("passengerCount>0 and passengerCount<100")
final_df = final_df.query("totalAmount>0")

columns_to_remove_for_training = ["datetime", "pickupLongitude", "pickupLatitude", "dropoffLongitude", "dropoffLatitude", "country_code"]
for col in columns_to_remove_for_training:
    final_df.pop(col)


# In[123]:


final_df.describe()


# In[124]:


final_df.dropna()
final_df.info()


# # Final Model

# In[125]:


import numpy as np


# In[126]:


final_df = final_df.drop(labels=['normalizeHolidayName','isPaidTimeOff','vendorID','precipDepth',
                                 'passengerCount','month_num','day_of_month','day_of_week',
                                'hour_of_day','snowDepth','precipTime','temperature'], axis=1)


# In[127]:


def clean_dataset(df):
    assert isinstance(df, pd.DataFrame), "df needs to be a pd.DataFrame"
    df.dropna(inplace=True)
    indices_to_keep = ~df.isin([np.nan, np.inf, -np.inf]).any(1)
    return df[indices_to_keep].astype(np.float64)


# In[128]:


clean_dataset(final_df)


# In[129]:


y_df = final_df.pop("totalAmount")


# In[130]:


x_df = final_df


# In[131]:


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(x_df, y_df, test_size=0.2, random_state=222)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)


# In[132]:


from sklearn.linear_model import LinearRegression

# Instantiate a regression object
lr = LinearRegression()

# fit the training sets to model 
lr.fit(X_train, y_train)


# In[133]:


# predict future values
y_hat_train = lr.predict(X_train)


# In[134]:


y_hat_train


# In[135]:


y_test = pd.DataFrame(y_hat_train, columns = ['Preds'])


# In[155]:


y_test.head()


# In[154]:


X_train.head()


# In[156]:


X_train.reset_index(drop=True, inplace=True)
y_test.reset_index(drop=True, inplace=True)


# In[173]:


df_final = X_train.join(y_test)


# In[174]:


df_final['distance'] = round(df_final['tripDistance'],1)


# In[182]:


df_pred = df_final.groupby('distance').agg({'Preds': ['min', 'max']})


# In[184]:


df_pred = df_pred.droplevel(axis=1, level=0).reset_index()


# In[185]:


df_pred


# In[186]:


df_pred.to_csv('/Users/kaileendebenhamsilva/Desktop/predictions.csv')


# In[ ]:




