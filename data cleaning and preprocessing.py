>>> import pandas as pd
>>> 
>>> # Load the weather data into a DataFrame
... df = pd.read_csv(r'C:\Users\admin\Desktop\Sql Project\Weather_data.csv')
>>> df.head()
      name             datetime  ...                 icon               stations
0  Chennai  2023-05-01T00:00:00  ...  partly-cloudy-night  VOMM,43279099999,AUCE
1  Chennai  2023-05-01T01:00:00  ...  partly-cloudy-night  VOMM,43279099999,AUCE
2  Chennai  2023-05-01T02:00:00  ...  partly-cloudy-night  VOMM,43279099999,AUCE
3  Chennai  2023-05-01T03:00:00  ...  partly-cloudy-night  VOMM,43279099999,AUCE
4  Chennai  2023-05-01T04:00:00  ...  partly-cloudy-night  VOMM,43279099999,AUCE

[5 rows x 24 columns]



>>> df.tail()
        name             datetime  ...                 icon               stations
739  Chennai  2023-05-31T19:00:00  ...  partly-cloudy-night  VOMM,43279099999,AUCE
740  Chennai  2023-05-31T20:00:00  ...  partly-cloudy-night  VOMM,43279099999,AUCE
741  Chennai  2023-05-31T21:00:00  ...  partly-cloudy-night  VOMM,43279099999,AUCE
742  Chennai  2023-05-31T22:00:00  ...  partly-cloudy-night  VOMM,43279099999,AUCE
743  Chennai  2023-05-31T23:00:00  ...  partly-cloudy-night       VOMM,43279099999

[5 rows x 24 columns]



>>> df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 744 entries, 0 to 743
Data columns (total 24 columns):
 #   Column            Non-Null Count  Dtype  
---  ------            --------------  -----  
 0   name              744 non-null    object 
 1   datetime          744 non-null    object 
 2   temp              744 non-null    float64
 3   feelslike         744 non-null    float64
 4   dew               744 non-null    float64
 5   humidity          744 non-null    float64
 6   precip            744 non-null    float64
 7   precipprob        744 non-null    int64  
 8   preciptype        45 non-null     object 
 9   snow              620 non-null    float64
 10  snowdepth         0 non-null      float64
 11  windgust          744 non-null    float64
 12  windspeed         744 non-null    float64
 13  winddir           744 non-null    float64
 14  sealevelpressure  744 non-null    float64
 15  cloudcover        744 non-null    float64
 16  visibility        744 non-null    float64
 17  solarradiation    744 non-null    int64  
 18  solarenergy       744 non-null    float64
 19  uvindex           744 non-null    int64  
 20  severerisk        744 non-null    int64  
 21  conditions        744 non-null    object 
 22  icon              744 non-null    object 
 23  stations          744 non-null    object 
dtypes: float64(14), int64(4), object(6)
memory usage: 139.6+ KB
      
      
      
df.describe()
             temp   feelslike         dew  ...  solarenergy     uvindex  severerisk
count  744.000000  744.000000  744.000000  ...   744.000000  744.000000  744.000000
mean    31.336559   39.937769   26.248925  ...     0.941263    2.596774   39.838710
std      2.338819    4.366092    1.339542  ...     1.235229    3.459637   29.960105
min     24.900000   24.900000   21.500000  ...     0.000000    0.000000    3.000000
25%     29.900000   37.500000   25.100000  ...     0.000000    0.000000   10.000000
50%     30.900000   40.400000   26.100000  ...     0.100000    0.000000   30.000000
75%     32.925000   42.800000   27.000000  ...     1.800000    5.000000   60.000000
max     38.200000   53.100000   30.000000  ...     3.600000   10.000000  100.000000

[8 rows x 18 columns]



print(df.columns)
Index(['name', 'datetime', 'temp', 'feelslike', 'dew', 'humidity', 'precip',
       'precipprob', 'preciptype', 'snow', 'snowdepth', 'windgust',
       'windspeed', 'winddir', 'sealevelpressure', 'cloudcover', 'visibility',
       'solarradiation', 'solarenergy', 'uvindex', 'severerisk', 'conditions',
       'icon', 'stations'],
      dtype='object')
print(df.shape)
(744, 24)


# Remove multiple columns by names
columns_to_drop = ['snow', 'snowdepth']
df_removed_columns = df.drop(columns_to_drop, axis=1)


# Display the remaining columns
remaining_columns = df.columns
print(remaining_columns)
Index(['name', 'datetime', 'temp', 'feelslike', 'dew', 'humidity', 'precip',
       'precipprob', 'preciptype', 'snow', 'snowdepth', 'windgust',
       'windspeed', 'winddir', 'sealevelpressure', 'cloudcover', 'visibility',
       'solarradiation', 'solarenergy', 'uvindex', 'severerisk', 'conditions',
       'icon', 'stations'],
      dtype='object')
print(df)
        name             datetime  ...                 icon               stations
0    Chennai  2023-05-01T00:00:00  ...  partly-cloudy-night  VOMM,43279099999,AUCE
1    Chennai  2023-05-01T01:00:00  ...  partly-cloudy-night  VOMM,43279099999,AUCE
2    Chennai  2023-05-01T02:00:00  ...  partly-cloudy-night  VOMM,43279099999,AUCE
3    Chennai  2023-05-01T03:00:00  ...  partly-cloudy-night  VOMM,43279099999,AUCE
4    Chennai  2023-05-01T04:00:00  ...  partly-cloudy-night  VOMM,43279099999,AUCE
..       ...                  ...  ...                  ...                    ...
739  Chennai  2023-05-31T19:00:00  ...  partly-cloudy-night  VOMM,43279099999,AUCE
740  Chennai  2023-05-31T20:00:00  ...  partly-cloudy-night  VOMM,43279099999,AUCE
741  Chennai  2023-05-31T21:00:00  ...  partly-cloudy-night  VOMM,43279099999,AUCE
742  Chennai  2023-05-31T22:00:00  ...  partly-cloudy-night  VOMM,43279099999,AUCE
743  Chennai  2023-05-31T23:00:00  ...  partly-cloudy-night       VOMM,43279099999

[744 rows x 24 columns]



df.drop('snow', axis=1, inplace=True)
print(df)
        name             datetime  ...                 icon               stations
0    Chennai  2023-05-01T00:00:00  ...  partly-cloudy-night  VOMM,43279099999,AUCE
1    Chennai  2023-05-01T01:00:00  ...  partly-cloudy-night  VOMM,43279099999,AUCE
2    Chennai  2023-05-01T02:00:00  ...  partly-cloudy-night  VOMM,43279099999,AUCE
3    Chennai  2023-05-01T03:00:00  ...  partly-cloudy-night  VOMM,43279099999,AUCE
4    Chennai  2023-05-01T04:00:00  ...  partly-cloudy-night  VOMM,43279099999,AUCE
..       ...                  ...  ...                  ...                    ...
739  Chennai  2023-05-31T19:00:00  ...  partly-cloudy-night  VOMM,43279099999,AUCE
740  Chennai  2023-05-31T20:00:00  ...  partly-cloudy-night  VOMM,43279099999,AUCE
741  Chennai  2023-05-31T21:00:00  ...  partly-cloudy-night  VOMM,43279099999,AUCE
742  Chennai  2023-05-31T22:00:00  ...  partly-cloudy-night  VOMM,43279099999,AUCE
743  Chennai  2023-05-31T23:00:00  ...  partly-cloudy-night       VOMM,43279099999

[744 rows x 23 columns]


df.drop('snowdepth', axis=1, inplace=True)
print(df)
        name             datetime  ...                 icon               stations
0    Chennai  2023-05-01T00:00:00  ...  partly-cloudy-night  VOMM,43279099999,AUCE
1    Chennai  2023-05-01T01:00:00  ...  partly-cloudy-night  VOMM,43279099999,AUCE
2    Chennai  2023-05-01T02:00:00  ...  partly-cloudy-night  VOMM,43279099999,AUCE
3    Chennai  2023-05-01T03:00:00  ...  partly-cloudy-night  VOMM,43279099999,AUCE
4    Chennai  2023-05-01T04:00:00  ...  partly-cloudy-night  VOMM,43279099999,AUCE
..       ...                  ...  ...                  ...                    ...
739  Chennai  2023-05-31T19:00:00  ...  partly-cloudy-night  VOMM,43279099999,AUCE
740  Chennai  2023-05-31T20:00:00  ...  partly-cloudy-night  VOMM,43279099999,AUCE
741  Chennai  2023-05-31T21:00:00  ...  partly-cloudy-night  VOMM,43279099999,AUCE
742  Chennai  2023-05-31T22:00:00  ...  partly-cloudy-night  VOMM,43279099999,AUCE
743  Chennai  2023-05-31T23:00:00  ...  partly-cloudy-night       VOMM,43279099999

[744 rows x 22 columns]


# Display the remaining columns
remaining_columns = df.columns
print(remaining_columns)
Index(['name', 'datetime', 'temp', 'feelslike', 'dew', 'humidity', 'precip',
       'precipprob', 'preciptype', 'windgust', 'windspeed', 'winddir',
       'sealevelpressure', 'cloudcover', 'visibility', 'solarradiation',
       'solarenergy', 'uvindex', 'severerisk', 'conditions', 'icon',
       'stations'],
      dtype='object')




# Data Formatting and Type Conversion
df['datetime'] = pd.to_datetime(df['datetime'], format='%Y-%m-%dT%H:%M:%S')  # Specify datetime format
df['temp'] = df['temp'].astype(float)  # Convert 'temp' column to float type
# Change the name of a single column
df.rename(columns={'name': 'location'}, inplace=True)
print(df.columns)

Index(['location', 'datetime', 'temp', 'feelslike', 'dew', 'humidity',
       'precip', 'precipprob', 'preciptype', 'windgust', 'windspeed',
       'winddir', 'sealevelpressure', 'cloudcover', 'visibility',
       'solarradiation', 'solarenergy', 'uvindex', 'severerisk', 'conditions',
       'icon', 'stations'],
      dtype='object')



# Data Validation and Sanity Checks

# Assuming 'precip' column should only contain non-negative values
df['precip'] = df['precip'].clip(lower=0)
# Display the changed 'precip' column   (clip() method allows to limit the values within a specific range)
print(df['precip'])
0      0.0
1      0.0
2      0.0
3      0.0
4      0.0
      ... 
739    0.0
740    0.0
741    0.0
742    0.0
743    0.0
Name: precip, Length: 744, dtype: float64
                  
         
     
                  
# Feature Engineering
# Extract the day of the week from the datetime
df['day_of_week'] = df['datetime'].dt.dayofweek  
print(df[['datetime', 'day_of_week']])
               datetime  day_of_week
0   2023-05-01 00:00:00            0
1   2023-05-01 01:00:00            0
2   2023-05-01 02:00:00            0
3   2023-05-01 03:00:00            0
4   2023-05-01 04:00:00            0
..                  ...          ...
739 2023-05-31 19:00:00            2
740 2023-05-31 20:00:00            2
741 2023-05-31 21:00:00            2
742 2023-05-31 22:00:00            2
743 2023-05-31 23:00:00            2

[744 rows x 2 columns]



# Check for inconsistent data values

# Check if temperature is within a valid range
invalid_temp = df[(df['temp'] < -50) | (df['temp'] > 60)]

print("Inconsistent temperature values:")
  
Inconsistent temperature values:
print(invalid_temp)
  
Empty DataFrame
Columns: [location, datetime, temp, feelslike, dew, humidity, precip, precipprob, preciptype, windgust, windspeed, winddir, sealevelpressure, cloudcover, visibility, solarradiation, solarenergy, uvindex, severerisk, conditions, icon, stations, day_of_week]
Index: []
      
      
      
      
      
# Check if humidity is within a valid range
invalid_humidity = df[(df['humidity'] < 0) | (df['humidity'] > 100)]
  
print("Inconsistent humidity values:")
  
Inconsistent humidity values:

print(invalid_humidity)
  
Empty DataFrame
Columns: [location, datetime, temp, feelslike, dew, humidity, precip, precipprob, preciptype, windgust, windspeed, winddir, sealevelpressure, cloudcover, visibility, solarradiation, solarenergy, uvindex, severerisk, conditions, icon, stations, day_of_week]
Index: []
      
      
      
      
# Check if any required columns have missing values
missing_columns = df.columns[df.isnull().any()].tolist()
  
print("Columns with missing values:")

Columns with missing values:
print("Columns with missing values:")
print(missing_columns)
['preciptype']



# Replace missing values in 'preciptype' column with 0
df['preciptype'].fillna(0, inplace=True)

# Print the updated DataFrame
print(df)
    location            datetime  ...               stations  day_of_week
0    Chennai 2023-05-01 00:00:00  ...  VOMM,43279099999,AUCE            0
1    Chennai 2023-05-01 01:00:00  ...  VOMM,43279099999,AUCE            0
2    Chennai 2023-05-01 02:00:00  ...  VOMM,43279099999,AUCE            0
3    Chennai 2023-05-01 03:00:00  ...  VOMM,43279099999,AUCE            0
4    Chennai 2023-05-01 04:00:00  ...  VOMM,43279099999,AUCE            0
..       ...                 ...  ...                    ...          ...
739  Chennai 2023-05-31 19:00:00  ...  VOMM,43279099999,AUCE            2
740  Chennai 2023-05-31 20:00:00  ...  VOMM,43279099999,AUCE            2
741  Chennai 2023-05-31 21:00:00  ...  VOMM,43279099999,AUCE            2
742  Chennai 2023-05-31 22:00:00  ...  VOMM,43279099999,AUCE            2
743  Chennai 2023-05-31 23:00:00  ...       VOMM,43279099999            2

[744 rows x 23 columns]


# Check if any required columns have missing values
missing_columns = df.columns[df.isnull().any()].tolist()
print(missing_columns)
[]


# Check for missing data in specific columns
missing_data = df[df['datetime'].isnull() | df['temp'].isnull()]
print(missing_data)
Empty DataFrame
Columns: [location, datetime, temp, feelslike, dew, humidity, precip, precipprob, preciptype, windgust, windspeed, winddir, sealevelpressure, cloudcover, visibility, solarradiation, solarenergy, uvindex, severerisk, conditions, icon, stations, day_of_week]
Index: []
      

     
      
# Identify missing timestamps within a specific time range
start_date = pd.to_datetime('2023-05-01')
end_date = pd.to_datetime('2023-05-31')
missing_timestamps = pd.date_range(start=start_date, end=end_date, freq='H').difference(df['datetime'])
print(missing_timestamps)
DatetimeIndex([], dtype='datetime64[ns]', freq=None)
print(df)

    location            datetime  ...               stations  day_of_week
0    Chennai 2023-05-01 00:00:00  ...  VOMM,43279099999,AUCE            0
1    Chennai 2023-05-01 01:00:00  ...  VOMM,43279099999,AUCE            0
2    Chennai 2023-05-01 02:00:00  ...  VOMM,43279099999,AUCE            0
3    Chennai 2023-05-01 03:00:00  ...  VOMM,43279099999,AUCE            0
4    Chennai 2023-05-01 04:00:00  ...  VOMM,43279099999,AUCE            0
..       ...                 ...  ...                    ...          ...
739  Chennai 2023-05-31 19:00:00  ...  VOMM,43279099999,AUCE            2
740  Chennai 2023-05-31 20:00:00  ...  VOMM,43279099999,AUCE            2
741  Chennai 2023-05-31 21:00:00  ...  VOMM,43279099999,AUCE            2
742  Chennai 2023-05-31 22:00:00  ...  VOMM,43279099999,AUCE            2
743  Chennai 2023-05-31 23:00:00  ...       VOMM,43279099999            2

[744 rows x 23 columns]


print(df.columns)
Index(['location', 'datetime', 'temp', 'feelslike', 'dew', 'humidity',
       'precip', 'precipprob', 'preciptype', 'windgust', 'windspeed',
       'winddir', 'sealevelpressure', 'cloudcover', 'visibility',
       'solarradiation', 'solarenergy', 'uvindex', 'severerisk', 'conditions',
       'icon', 'stations', 'day_of_week'],
      dtype='object')


print(df.shape)
(744, 23)


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px



# Display the first few rows of the DataFrame
print(df.head())
  location            datetime  ...               stations  day_of_week
0  Chennai 2023-05-01 00:00:00  ...  VOMM,43279099999,AUCE            0
1  Chennai 2023-05-01 01:00:00  ...  VOMM,43279099999,AUCE            0
2  Chennai 2023-05-01 02:00:00  ...  VOMM,43279099999,AUCE            0
3  Chennai 2023-05-01 03:00:00  ...  VOMM,43279099999,AUCE            0
4  Chennai 2023-05-01 04:00:00  ...  VOMM,43279099999,AUCE            0

[5 rows x 23 columns]


# Check the summary statistics of numeric columns
print(df.describe())
                            datetime        temp  ...  severerisk  day_of_week
count                            744  744.000000  ...  744.000000   744.000000
mean   2023-05-16 11:29:59.999999744   31.336559  ...   39.838710     2.806452
min              2023-05-01 00:00:00   24.900000  ...    3.000000     0.000000
25%              2023-05-08 17:45:00   29.900000  ...   10.000000     1.000000
50%              2023-05-16 11:30:00   30.900000  ...   30.000000     3.000000
75%              2023-05-24 05:15:00   32.925000  ...   60.000000     5.000000
max              2023-05-31 23:00:00   38.200000  ...  100.000000     6.000000
std                              NaN    2.338819  ...   29.960105     2.008102

[8 rows x 18 columns]



# Check the data types and missing values in the DataFrame
print(df.info())
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 744 entries, 0 to 743
Data columns (total 23 columns):
 #   Column            Non-Null Count  Dtype         
---  ------            --------------  -----         
 0   location          744 non-null    object        
 1   datetime          744 non-null    datetime64[ns]
 2   temp              744 non-null    float64       
 3   feelslike         744 non-null    float64       
 4   dew               744 non-null    float64       
 5   humidity          744 non-null    float64       
 6   precip            744 non-null    float64       
 7   precipprob        744 non-null    int64         
 8   preciptype        744 non-null    object        
 9   windgust          744 non-null    float64       
 10  windspeed         744 non-null    float64       
 11  winddir           744 non-null    float64       
 12  sealevelpressure  744 non-null    float64       
 13  cloudcover        744 non-null    float64       
 14  visibility        744 non-null    float64       
 15  solarradiation    744 non-null    int64         
 16  solarenergy       744 non-null    float64       
 17  uvindex           744 non-null    int64         
 18  severerisk        744 non-null    int64         
 19  conditions        744 non-null    object        
 20  icon              744 non-null    object        
 21  stations          744 non-null    object        
 22  day_of_week       744 non-null    int32         
dtypes: datetime64[ns](1), float64(12), int32(1), int64(4), object(5)
memory usage: 130.9+ KB
None



# Histogram of temperature distribution
plt.hist(df['temp'], bins=20)
(array([  3.,   4.,   6.,  26.,  13.,  38.,  60., 107., 105.,  90.,  53.,
        46.,  52.,  45.,  27.,  30.,  22.,  10.,   4.,   3.]), array([24.9  , 25.565, 26.23 , 26.895, 27.56 , 28.225, 28.89 , 29.555,
       30.22 , 30.885, 31.55 , 32.215, 32.88 , 33.545, 34.21 , 34.875,
       35.54 , 36.205, 36.87 , 37.535, 38.2  ]), <BarContainer object of 20 artists>)
plt.xlabel('Temperature')
Text(0.5, 0, 'Temperature')
plt.ylabel('Frequency')
Text(0, 0.5, 'Frequency')
plt.title('Temperature Distribution')
Text(0.5, 1.0, 'Temperature Distribution')
plt.show()



# Line plot of temperature over time
plt.plot(df['datetime'], df['temp'])
[<matplotlib.lines.Line2D object at 0x0000013A6F641C50>]
plt.xlabel('Date')
Text(0.5, 0, 'Date')
plt.ylabel('Temperature')
Text(0, 0.5, 'Temperature')
plt.title('Temperature Variation over Time')
Text(0.5, 1.0, 'Temperature Variation over Time')
plt.xticks(rotation=45)
(array([19478., 19482., 19486., 19490., 19494., 19498., 19502., 19506.,
       19509.]), [Text(19478.0, 0, '2023-05-01'), Text(19482.0, 0, '2023-05-05'), Text(19486.0, 0, '2023-05-09'), Text(19490.0, 0, '2023-05-13'), Text(19494.0, 0, '2023-05-17'), Text(19498.0, 0, '2023-05-21'), Text(19502.0, 0, '2023-05-25'), Text(19506.0, 0, '2023-05-29'), Text(19509.0, 0, '2023-06-01')])
plt.show()




      
import seaborn as sns

# Scatter plot of temperature vs. humidity
sns.scatterplot(data=df, x='humidity', y='temp')
<Axes: xlabel='humidity', ylabel='temp'>
plt.xlabel('Humidity')
Text(0.5, 0, 'Humidity')
plt.ylabel('Temperature')
Text(0, 0.5, 'Temperature')
plt.title('Temperature vs. Humidity')
Text(0.5, 1.0, 'Temperature vs. Humidity')
plt.show()



# Box plot of temperature by month
df['month'] = pd.to_datetime(df['datetime']).dt.month
sns.boxplot(data=df, x='month', y='temp')
<Axes: xlabel='month', ylabel='temp'>
plt.xlabel('Month')
Text(0.5, 0, 'Month')
plt.ylabel('Temperature')
Text(0, 0.5, 'Temperature')
plt.title('Temperature Variation by Month')
Text(0.5, 1.0, 'Temperature Variation by Month')
plt.show()




# Interactive line plot of temperature over time using Plotly
fig = px.line(df, x='datetime', y='temp', title='Temperature Variation over Time')
fig.show()




#Time Series Analysis:

#Plot a line chart of temperature variations over time with a rolling average
df['datetime'] = pd.to_datetime(df['datetime'])
df.set_index('datetime', inplace=True)
rolling_avg = df['temp'].rolling(window=30).mean()
plt.plot(df.index, df['temp'], label='Temperature')
[<matplotlib.lines.Line2D object at 0x0000013A07290A50>]
plt.plot(df.index, rolling_avg, label='30-day Rolling Average')
[<matplotlib.lines.Line2D object at 0x0000013A072C4A10>]
plt.xlabel('Date')
Text(0.5, 0, 'Date')
plt.ylabel('Temperature')
Text(0, 0.5, 'Temperature')
plt.title('Temperature Time Series')
Text(0.5, 1.0, 'Temperature Time Series')
plt.legend()
<matplotlib.legend.Legend object at 0x0000013A04F6D610>
plt.show()



# Create a heatmap to visualize the correlation between multiple weather variables
correlation_matrix = df[['temp', 'humidity', 'precip', 'windspeed']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
<Axes: >
plt.title('Correlation Heatmap')
Text(0.5, 1.0, 'Correlation Heatmap')
plt.show()




from statsmodels.tsa.seasonal import seasonal_decompose
result = seasonal_decompose(df['temp'], model='additive', period=12)
result.plot()
<Figure size 640x480 with 4 Axes>
plt.show()
