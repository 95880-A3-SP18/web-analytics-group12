#this is data analysis function

import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import matplotlib.pyplot as plt
import re
from numpy import NaN
import glob
l = [pd.read_csv(filename, sep=",", encoding="ISO-8859-1") for filename in glob.glob("rent_data/*.csv")]
rent_df = pd.concat(l, ignore_index=True)
rent_df = rent_df.drop_duplicates(subset=["Headline"]).reset_index(drop=True)
rent_df['Housing'] = rent_df['Housing'].astype(str)

pattern = re.compile('([0-9]+)\s?(bed|bedroom|brd|br|Bedroom|BR)')
pattern_bed = re.compile('(..)([0-9]+)\s*(br)')

def convert_housing(row, pattern, pattern_bed):
    headline = row['Headline']
    housing = row['Housing']
    if housing == 'nan':
        if bool(pattern.search(headline)):
            housing = pattern.search(headline).group(1)
            housing = int(housing)
            return housing
        else:
            return ('NaN')
    else:
        housing = pattern_bed.search(housing).group(2)
        housing = int(housing)
        return housing

rent_df['Housing'] = rent_df.apply(convert_housing, axis=1, pattern=pattern, pattern_bed=pattern_bed)
temp_housing = []
for row in rent_df['Housing']:
    if row != 'NaN':
        temp_housing.append(row)
mean_housing = round(np.mean(temp_housing))
for i, row in enumerate(rent_df['Housing']):
    if row == 'NaN':
        rent_df['Housing'][i] = mean_housing
rent_df['Housing'] = rent_df['Housing'].astype(int)
# deal with Price variable
rent_df['Price'] = rent_df['Price'].astype(str)

pattern = re.compile('^\$\d*(\,?\d{3})*')

def convert_money(row, pattern):
    price = row['Price']
    if bool(pattern.match(price)):
        price = price.replace("$", "")
        price = price.replace(",", "")
        price = float(price)
        return price
    else:
        return (NaN)
rent_df['Price'] = rent_df.apply(convert_money, axis=1, pattern=pattern)
rent_df['Price'] = rent_df['Price'].astype(float)
# cmu is on (40.443322, -79.943583)
# range: latitude--(40.429331, 40.454349)
# range: longitude--(-79.961402, -79.914453)
# only concern the apartments inside this area range
import math
def cal_distance(row):
    latitude = row['Latitude']
    longitude = row['Longitude']
    distance = math.sqrt((latitude - 40.443322) ** 2 + (longitude - (-79.943583)) ** 2)
    if latitude >= 40.429331 and latitude <= 40.454349 and longitude >= -79.961402 and longitude <= -79.914453:
        return distance
    else:
        return (np.nan)

rent_df['Distance'] = rent_df.apply(cal_distance, axis=1)
distance_df = rent_df[['Distance', 'Price']]
distance_df = distance_df.dropna(axis=0, how='any')
# distance_df
def distance_level(row):
    distance = row['Distance']
    interval = (max(distance_df['Distance']) - min(distance_df['Distance'])) / 3
    if distance >= min(distance_df['Distance']) and distance < interval:
        level = 1
    elif distance >= interval and distance < interval * 2:
        level = 2
    else:
        level = 3
    return level

distance_df['Distance'] = distance_df.apply(distance_level, axis=1)
# general price distribution
from scipy.stats import norm
import matplotlib.mlab as mlab

x = rent_df['Price']
(mu, sigma) = norm.fit(x)
fig, ax = plt.subplots(figsize=(10, 8))

n, bins, patches = plt.hist(x, 15, normed=1, facecolor='g', alpha=0.75)
ax.axvline(np.mean(x), color='b', linestyle='dashed', linewidth=2)

# add a 'best fit' line
y = mlab.normpdf(bins, mu, sigma)
ax.plot(bins, y, '--')

plt.xlabel('Price')
plt.ylabel('Probability')
plt.title('Price Distribution Histogram')
plt.grid(True)
plt.show()

# price distribution by housing plan

x = rent_df['Housing']
y = rent_df['Price']

plt.figure(figsize=(10, 8))
plt.bar(x, y, color='green')

plt.grid(True)
plt.xlabel('Number of bedroom')
plt.ylabel('Price')
plt.title('Price Distribution by Housing')
plt.show()

# price distribution by housing per bedroom
# add another variable 'Price_per_bed'
rent_df['Price_per_bed'] = rent_df['Price'] / rent_df['Housing']

x = rent_df['Housing']
y = rent_df['Price_per_bed']

plt.figure(figsize=(10, 8))
plt.bar(x, y, color='green')
plt.xlabel('Number of bedroom')
plt.ylabel('Price per bedroom')
plt.title('Price (per bedroom) Distribution by Housing')
plt.grid(True)
plt.show()

import matplotlib.pylab as plb

rent_df['Available Date'] = pd.to_datetime(rent_df['Available Date'])
# rent_df['Month'] = rent_df['Available Date'].dt.month

df = pd.DataFrame(columns=('Available Date', 'Price'), data=rent_df)
df = df.sort_values(by=['Available Date'])

dates = np.array(df['Available Date'])
price = np.array(df['Price'])

price_series = Series(price, index=dates)
plt.figure(figsize=(10, 8))
price_series['2018-01-01':'2018-12-01'].plot(style='k.')
plt.ylim(0, 5000)
plt.xticks(rotation=35)
plt.xlabel('Available Date')
plt.ylabel('Price')
plt.title('Price Time Series')
plt.show()

# regress price on housing
import statsmodels.formula.api as smf
model_1 = smf.ols(formula='Price ~ C(Housing)', data=rent_df)
results_model1 = model_1.fit()
results_model1.summary()

rent_df['Price_per_bed'] = rent_df['Price_per_bed'].astype(int)
# rent_df.info()
# regress price per bedroom on housing
model_2 = smf.ols(formula='Price_per_bed ~ C(Housing)', data=rent_df)
results_model2 = model_2.fit()
results_model2.summary()

# regess price on distance
model_3 = smf.ols(formula='Price ~ C(Distance)', data=distance_df)
results_model3 = model_3.fit()
results_model3.summary()

model_3 = smf.ols(formula='Price ~ C(Month)', data=rent_df)
results_model3 = model_3.fit()
results_model3.summary()

# Final regression model for prediction
model_4 = smf.ols(formula='Price ~ C(Housing) + C(Month)', data=rent_df)
results_model4 = model_4.fit()
results_model4.summary()
