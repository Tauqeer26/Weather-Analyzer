# **Weather Analyzer**

This project is a comprehensive Weather Analyzer application that retrieves and processes weather data from a database and external API. The application allows users to retrieve information on cities and countries, calculate various weather statistics, and plot graphs based on the data. Additionally, it integrates with the OpenMeteo API to fetch real-time weather data.

## **Features**
- **Retrieve all cities**
- **Retrieve all countries**
- **Calculate average annual temperature**
- **Calculate average seven-day precipitation**
- **Calculate average mean temperature by city**
- **Calculate average annual precipitation by country**
- **Plot: Annual precipitation by Country**
- **Plot: City Weather Statistics**
- **Plot: Minimum and Maximum Temperature of a city**
- **Plot: Avg_temp_vs_avg_rainfall**
- **Plot: Average_mean_temp_and_precipitation_by_city**
- **Plot: Average seven day Precipitation Plot**
- **Getting weather data from OpenMeteo API**

## **Getting Started**
### **Prerequisites**
Ensure you have Python 3.x installed. You'll also need to install the required packages. These can be installed using the provided requirements.txt file.

### **Installation**
1. Clone the repository to your local machine:
   ```
   git clone https://github.com/your-username/weather-analyzer.git
   cd weather-analyzer
   ```
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Ensure you have the database file **CIS4044-N-SDI-OPENMETEO-PARTIAL.db** in the same directory as the script.

### **Usage**
Run the **phase_3.py** script to start the Weather Analyzer application:
```
python weather_analyzer.py
```
Follow the on-screen menu to perform various weather analysis tasks. Select a number from 1 to 13 to choose an action, or 0 to exit.

## **Menu Options**
1. **Retrieve all cities**: Displays a list of all cities in the database.
2. **Retrieve all countries**: Displays a list of all countries in the database.
3. **Calculate average annual temperature**: Calculates the average annual temperature for a specified city and year.
4. **Calculate average seven-day precipitation**: Calculates the average precipitation over seven days for a specified city starting from a given date.
5. **Calculate average mean temperature by city**: Calculates the average mean temperature for all cities between specified dates.
6. **Calculate average annual precipitation by country**: Calculates the average annual precipitation for each country for a specified year.
7. **Plot: Annual precipitation by Country**: Plots the annual precipitation by country for a specified year.
8. **Plot: City Weather Statistics**: Plots weather statistics for all cities between specified dates.
9. **Plot: Minimum and Maximum Temperature of a city**: Plots the minimum and maximum temperature for a specified city, year, and month.
10. **Plot: Avg_temp_vs_avg_rainfall**: Plots average temperature vs average rainfall.
11. **Plot: Average_mean_temp_and_precipitation_by_city**: Plots average mean temperature and precipitation by city between specified dates.
12. **Plot: Average seven day Precipitation Plot**: Plots the average seven-day precipitation for a specified city starting from a given date.
13. **Getting weather data from OpenMeteo API**: Fetches weather data from the OpenMeteo API.

### **Exiting the Program**
To exit the program, select 0 from the menu or choose **n** when prompted to continue.

## **Contributing**
If you would like to contribute to this project, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## **Acknowledgements**
This project was developed as part of the CIS4044 course. Special thanks to the course instructors and teaching assistants for their support and guidance.
