import sqlite3

class WeatherAnalyzer:

    def __init__(self, db_name):
        # Establishing connection to the database
        self.connection = sqlite3.connect(db_name)

    def select_all_countries(self):
        try:
             # SQL Query to select all countries
            query = "SELECT * FROM [countries]"
            cursor = self.connection.cursor()
            results = cursor.execute(query)
            # Iterating through query results and printing country information
            for row in results:
                print(f"Country Id: {row[0]} -- Country Name: {row[1]} -- Country Timezone: {row[2]}")
        except sqlite3.OperationalError as ex:
            # Handling exceptions related to database operations
            print(ex)

    def select_all_cities(self):
        try:
            # SQL Query to select all cities
            query = "SELECT * FROM [cities]"
            cursor = self.connection.cursor()
            results = cursor.execute(query)
            # Iterating through query results and printing information
            for row in results:
                print(f"City Id: {row[0]} -- City Name: {row[1]} -- Longitude: {row[2]} -- Latitude: {row[3]} -- Country Id of the City: {row[4]}")
        except sqlite3.OperationalError as ex:
            # Handling exceptions related to database operations
            print(ex)

    def average_annual_temperature(self, city_id, year):
        try:
            # SQL query to calculate average annual temperature for a given city and year
            query = """
            SELECT AVG(mean_temp)
            FROM daily_weather_entries
            WHERE city_id = ? AND strftime('%Y', date) = ?
            """
            cursor = self.connection.cursor()
            cursor.execute(query, (city_id, year))
            average_temperature = cursor.fetchone()[0]
            # Displaying the average annual temperature for the specified city and year
            print(f"Average annual temperature for City {city_id} in {year}: {average_temperature} °C")
        except sqlite3.OperationalError as ex:
            # Handling exceptions related to database operations
            print(ex)

    def average_seven_day_precipitation(self, city_id, start_date):
        try:
            # SQL query to calculate average_seven_day_precipitation
            cursor = self.connection.cursor()

            query = """
            SELECT AVG(precipitation)
            FROM daily_weather_entries
            WHERE city_id = ? AND date BETWEEN ? AND date(?, '+6 days')
            """
            # Executing the query with parameters
            cursor.execute(query, (city_id, start_date, start_date))
            # Retrieving the average precipitation result
            average_precipitation = cursor.fetchone()[0]
            print(f"Average seven-day precipitation for City {city_id} starting from {start_date}: {average_precipitation} mm")
        except sqlite3.OperationalError as ex:
            # Handling exceptions related to database operations
            print(ex)

    def average_mean_temp_by_city(self, date_from, date_to):
        try:
            # SQL query to calculate average mean temperature by city
            cursor = self.connection.cursor()

            query = """
            SELECT city_id, AVG(mean_temp) AS avg_mean_temp
            FROM daily_weather_entries
            WHERE date BETWEEN ? AND ?
            GROUP BY city_id
            """
            # Executing the query with parameters
            cursor.execute(query, (date_from, date_to))
            results = cursor.fetchall()
            # Iterating through query results and printing information
            for row in results:
                city_id, avg_mean_temp = row
                print(f"City {city_id}: Average mean temperature between {date_from} and {date_to}: {avg_mean_temp} °C")

        except sqlite3.OperationalError as ex:
            # Handling exceptions related to database operations
            print(ex)

    def average_annual_precipitation_by_country(self, year):
        try:
            cursor = self.connection.cursor()
            # SQL query to calculate average annual precipitation by country
            query = '''
                SELECT countries.name, AVG(daily_weather_entries.precipitation)
                FROM countries
                JOIN cities ON countries.id = cities.id
                JOIN daily_weather_entries ON cities.id = daily_weather_entries.city_id
                WHERE strftime('%Y', daily_weather_entries.date) = ?
                GROUP BY countries.name
            '''
             # Executing the query with parameters
            cursor.execute(query, (str(year),))
            results = cursor.fetchall()
            # Iterating through query results and printing information
            for country, avg_precipitation in results:
                print(f"Average annual precipitation for {country} in {year}: {avg_precipitation} mm")
        except sqlite3.OperationalError as ex:
            # Handling exceptions related to database operations
            print(ex)
    def close_connection(self):
        # Method to close the database connection
        self.connection.close()
