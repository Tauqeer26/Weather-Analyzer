#https://open-meteo.com/

#----------------API Website :  ------------# 
import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry
import sqlite3
#----------------Libraries-----------------------------------------# 

def OpenMeteo():
# Setup the Open-Meteo API client with cache and retry on error
	cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
	retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
	openmeteo = openmeteo_requests.Client(session = retry_session)

	# Make sure all required weather variables are listed here
	# The order of variables in hourly or daily is important to assign them correctly below
	url = "https://api.open-meteo.com/v1/forecast"
	params = {
		"latitude": 54.5762,
		"longitude": -1.2348,
		"current": ["temperature_2m", "relative_humidity_2m", "apparent_temperature", "is_day", "precipitation", "rain", "showers", "snowfall", "weather_code"],
		"hourly": ["temperature_2m", "relative_humidity_2m", "precipitation", "rain", "showers", "snowfall", "snow_depth", "weather_code", "wind_speed_10m", "soil_temperature_0cm", "soil_temperature_6cm", "soil_moisture_1_to_3cm", "soil_moisture_3_to_9cm"],
		"daily": ["weather_code", "temperature_2m_max", "precipitation_sum", "rain_sum", "showers_sum", "snowfall_sum"],
		"timezone": "Europe/London"
	}
	responses = openmeteo.weather_api(url, params=params)

	# Process first location. Add a for-loop for multiple locations or weather models
	response = responses[0]
	print(f"Coordinates {response.Latitude()}°E {response.Longitude()}°N")
	print(f"Elevation {response.Elevation()} m asl")
	print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
	print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

	# Current values. The order of variables needs to be the same as requested.
	current = response.Current()
	current_temperature_2m = current.Variables(0).Value()
	current_relative_humidity_2m = current.Variables(1).Value()
	current_apparent_temperature = current.Variables(2).Value()
	current_is_day = current.Variables(3).Value()
	current_precipitation = current.Variables(4).Value()
	current_rain = current.Variables(5).Value()
	current_showers = current.Variables(6).Value()
	current_snowfall = current.Variables(7).Value()
	current_weather_code = current.Variables(8).Value()

	print(f"Current time {current.Time()}")
	print(f"Current temperature_2m {current_temperature_2m}")
	print(f"Current relative_humidity_2m {current_relative_humidity_2m}")
	print(f"Current apparent_temperature {current_apparent_temperature}")
	print(f"Current is_day {current_is_day}")
	print(f"Current precipitation {current_precipitation}")
	print(f"Current rain {current_rain}")
	print(f"Current showers {current_showers}")
	print(f"Current snowfall {current_snowfall}")
	print(f"Current weather_code {current_weather_code}")

	# Process hourly data. The order of variables needs to be the same as requested.
	hourly = response.Hourly()
	hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
	hourly_relative_humidity_2m = hourly.Variables(1).ValuesAsNumpy()
	hourly_precipitation = hourly.Variables(2).ValuesAsNumpy()
	hourly_rain = hourly.Variables(3).ValuesAsNumpy()
	hourly_showers = hourly.Variables(4).ValuesAsNumpy()
	hourly_snowfall = hourly.Variables(5).ValuesAsNumpy()
	hourly_snow_depth = hourly.Variables(6).ValuesAsNumpy()
	hourly_weather_code = hourly.Variables(7).ValuesAsNumpy()
	hourly_wind_speed_10m = hourly.Variables(8).ValuesAsNumpy()
	hourly_soil_temperature_0cm = hourly.Variables(9).ValuesAsNumpy()
	hourly_soil_temperature_6cm = hourly.Variables(10).ValuesAsNumpy()
	hourly_soil_moisture_1_to_3cm = hourly.Variables(11).ValuesAsNumpy()
	hourly_soil_moisture_3_to_9cm = hourly.Variables(12).ValuesAsNumpy()

	hourly_data = {"date": pd.date_range(
		start = pd.to_datetime(hourly.Time(), unit = "s"),
		end = pd.to_datetime(hourly.TimeEnd(), unit = "s"),
		freq = pd.Timedelta(seconds = hourly.Interval()),
		inclusive = "left"
	)}
	hourly_data["temperature_2m"] = hourly_temperature_2m
	hourly_data["relative_humidity_2m"] = hourly_relative_humidity_2m
	hourly_data["precipitation"] = hourly_precipitation
	hourly_data["rain"] = hourly_rain
	hourly_data["showers"] = hourly_showers
	hourly_data["snowfall"] = hourly_snowfall
	hourly_data["snow_depth"] = hourly_snow_depth
	hourly_data["weather_code"] = hourly_weather_code
	hourly_data["wind_speed_10m"] = hourly_wind_speed_10m
	hourly_data["soil_temperature_0cm"] = hourly_soil_temperature_0cm
	hourly_data["soil_temperature_6cm"] = hourly_soil_temperature_6cm
	hourly_data["soil_moisture_1_to_3cm"] = hourly_soil_moisture_1_to_3cm
	hourly_data["soil_moisture_3_to_9cm"] = hourly_soil_moisture_3_to_9cm

	hourly_dataframe = pd.DataFrame(data = hourly_data)
	print(hourly_dataframe)
	hourly_dataframe.to_csv('hourly_weather_data.csv', index=False)

	# Process daily data. The order of variables needs to be the same as requested.
	daily = response.Daily()
	daily_weather_code = daily.Variables(0).ValuesAsNumpy()
	daily_temperature_2m_max = daily.Variables(1).ValuesAsNumpy()
	daily_precipitation_sum = daily.Variables(2).ValuesAsNumpy()
	daily_rain_sum = daily.Variables(3).ValuesAsNumpy()
	daily_showers_sum = daily.Variables(4).ValuesAsNumpy()
	daily_snowfall_sum = daily.Variables(5).ValuesAsNumpy()

	daily_data = {"date": pd.date_range(
		start = pd.to_datetime(daily.Time(), unit = "s"),
		end = pd.to_datetime(daily.TimeEnd(), unit = "s"),
		freq = pd.Timedelta(seconds = daily.Interval()),
		inclusive = "left"
	)}
	daily_data["weather_code"] = daily_weather_code
	daily_data["temperature_2m_max"] = daily_temperature_2m_max
	daily_data["precipitation_sum"] = daily_precipitation_sum
	daily_data["rain_sum"] = daily_rain_sum
	daily_data["showers_sum"] = daily_showers_sum
	daily_data["snowfall_sum"] = daily_snowfall_sum

	daily_dataframe = pd.DataFrame(data = daily_data)
	daily_dataframe.to_csv('daily_weather_data.csv', index=False)
	print(daily_dataframe)



	# Read the CSV files into pandas DataFrames
	hourly_dataframe = pd.read_csv('hourly_weather_data.csv')
	daily_dataframe = pd.read_csv('daily_weather_data.csv')

	# Create/connect to an SQLite database
	conn = sqlite3.connect('weather_data.db')

	# Write DataFrames to SQLite tables
	hourly_dataframe.to_sql('hourly_weather', conn, if_exists='replace', index=False)
	daily_dataframe.to_sql('daily_weather', conn, if_exists='replace', index=False)

	# Commit changes and close the connection
	conn.commit()
	conn.close()
	print("Its Done")