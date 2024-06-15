from datetime import datetime
from phase_1 import WeatherAnalyzer as WA # phase 1 is the module which has a class with a name WeatherAnalyzer
from phase_2 import MatPLOTS as mp #phase 2 is the module which has a class with a name MatPLOTS
from phase_4 import OpenMeteo #phase 4 is the module which has a function with a name OpenMeteo
#----------------Libraries-----------------------------------------# 

Ana = WA("CIS4044-N-SDI-OPENMETEO-PARTIAL.db")
plot = mp("CIS4044-N-SDI-OPENMETEO-PARTIAL.db")
while True:
    #Weather Analyzer Menu
    print("====================================================")
    print("==============WEATHER ANALYSER======================")
    print("====================================================")
    print("1. Retrieve all cities")
    print("2. Retrieve all countries")
    print("3. Calculate average annual temperature")
    print("4. Calculate average seven-day precipitation")
    print("5. Calculate average mean temperature by city")
    print("6. Calculate average annual precipitation by country")
    print("====================================================")
    print("==============GRAPH PLOTTING========================")
    print("====================================================")
    print("7.  Plot: Annual precipitation by Country")
    print("8.  Plot: City Weather Statistics")
    print("9.  Plot: Minimum and Maximum Temperature of a city")
    print("10. Plot: Avg_temp_vs_avg_rainfall")
    print("11. Plot: Average_mean_temp_and_precipitation_by_city")
    print("12. Plot: Average seven day Precipitation Plot")
    print("====================================================")
    print("==============OPENMETEO API=========================")
    print("====================================================")
    print("13. Getting weather data from OpenMeteo API")
    print("0.  Exit")
    try:
        num = int(input("Select a number from 1-13 or 0 to Exit: "))
        
        # Checking user input and calling corresponding methods based on input
        if num == 1:
            # Call the method to select all cities
            Ana.select_all_cities()
        elif num == 2:
            # Call the method to select all countries
            Ana.select_all_countries()
        elif num == 3:
            # Getting user input for City ID and year, then calling the method
            cID = int(input("Enter City ID: (from 1-4) "))
            year = input("Enter year: (e.g., 2020) ")
            Ana.average_annual_temperature(cID, year)

        elif num == 4:
            # Loop to ensure valid City ID input
            while True:
                cID = int(input("Enter City ID: (from 1-4) "))
                # Validate if input is between 1 and 4
                if 1 <= cID <= 4: #There are 4 cities in the data
                    break
                else:
                    print("Invalid input. Please enter a number between 1 and 4.")
            # Loop to ensure valid start date input
            while True:
                sDate_str = input("Enter start date (e.g 2022-01-01): ")
                try:
                    sDate = datetime.strptime(sDate_str, '%Y-%m-%d')
                    break
                except ValueError:
                    print("Invalid date format. Please enter the correct format (e.g 2022-01-01).")

            # Call Ana's method with the validated inputs
            Ana.average_seven_day_precipitation(cID, sDate)

        elif num == 5:
            # Loop to ensure valid date range input
            while True:
                date_from_str = input("Enter start date (YYYY-MM-DD): ")
                date_to_str = input("Enter end date (YYYY-MM-DD): ")
                try:
                    date_from = datetime.strptime(date_from_str, '%Y-%m-%d') # input Date format
                    date_to = datetime.strptime(date_to_str, '%Y-%m-%d')
                    break
                except ValueError: #Error handling
                    print("Invalid date format. Please enter the correct format (YYYY-MM-DD).")

             # Call Ana's method with the validated date range inputs
            Ana.average_mean_temp_by_city(date_from, date_to)
        
        # Check if num equals 6
        elif num == 6:
            year=input("Enter a year: (e.g 2020) ")
            Ana.average_annual_precipitation_by_country(year)

        # Check if num equals 7
        elif num==7:
            year = input("Enter year: (e.g 2020) ")
            plot.average_annual_precipitation_by_country(year)
        elif num == 8:
            while True:
                # Convert input strings to datetime objects
                datef = input("Enter Date From: (e.g 2022-01-01) ")
                datet = input("Enter Date To:   (e.g 2022-01-01) ")
                #Error Handling
                try:
                    date_from = datetime.strptime(datef, '%Y-%m-%d')
                    date_to = datetime.strptime(datet, '%Y-%m-%d')
                    break
                except ValueError:
                    print("Invalid date format. Please enter the date in the correct format (e.g. 2022-01-01).")
            
            plot.plot_city_weather_statistics(date_from, date_to)

        elif num == 9:
            while True:
                try:
                    cID = int(input("Enter City ID: (from 1-4) "))
                    if 1 <= cID <= 4:
                        break
                    else:
                        print("Invalid input. Please enter a number between 1 and 4.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            while True:
                try:
                    year = int(input("Enter year: (e.g. 2020) "))
                    if year >= 0:  
                        break
                    else:
                        print("Invalid input. Please enter a valid year.")
                except ValueError:
                    print("Invalid input. Please enter a valid year.")

            while True:
                try:
                    month = int(input("Enter month (1-12): "))
                    if 1 <= month <= 12:
                        break
                    else:
                        print("Invalid input. Please enter a number between 1 and 12.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            plot.plot_daily_temperature(cID, year, month)

        elif num ==10:
            
            plot.plot_avg_temp_vs_avg_rainfall()
        elif num ==11:
            datef = input("Enter Date From: (e.g 2022-01-01) ")
            datet = input("Enter Date To:   (e.g 2022-01-01) ")
            plot.average_mean_temp_and_precipitation_by_city(datef,datet)
        elif num==12:
            cID=int(input('Enter City ID: (from 1-4) '))
            start_date=input('Enter Start Date: (e.g 2022-01-01)')
            plot.average_seven_day_precipitation(cID,start_date)
        elif num==13:
            #This is the OpenMeteo Function created in phase_4.py file 
            OpenMeteo()
        
        elif num == 0:
            print("Exiting Weather Analyzer. Goodbye!")
            break
        else:
            print("Select a correct number")

        continue_option = input("Do you want to continue? (y/n): ").lower()
        if continue_option != 'y':
            print("Exiting Weather Analyzer. Goodbye!")
            break
    except ValueError:
        print("Invalid input. Please enter the correct format.")
        continue_option = input("Do you want to continue? (y/n): ").lower()
        if continue_option != 'y':
            print("Exiting Weather Analyzer. Goodbye!")
            break
 