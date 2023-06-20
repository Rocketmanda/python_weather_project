import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celsius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string containing the temperature and "degrees Celsius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts an ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    date = datetime.fromisoformat(iso_string)
    return date.strftime("%A %d %B %Y")


def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celsius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celsius, rounded to 1 decimal place.
    """
    temp_in_celsius = (float(temp_in_fahrenheit) - 32) * 5 / 9
    return round(temp_in_celsius, 1)


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    numeric_data = [float(value) for value in weather_data]
    return sum(numeric_data) / len(numeric_data)

import csv

def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    data = []
    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            if len(row) == 3:  # Ensure each row has three columns
                date = row[0]
                try:
                    min_temp = int(row[1])
                    max_temp = int(row[2])
                    data.append([date, min_temp, max_temp])
                except ValueError:
                    pass
    return data

csv_file = '/Users/manda/Documents/She-Codes-Plus/Python_She_Codes/python_weather_project/tests/data/example_one.csv'
result = load_data_from_csv(csv_file)
print(result)

def find_min(temperatures):
    if not temperatures:
        return ()
    
    min_temperature = None
    min_index = None

    for index, temperature in enumerate(temperatures):
        try:
            temperature = float(temperature)
            if min_temperature is None or temperature <= min_temperature:
                min_temperature = temperature
                min_index = index
        except ValueError:
            continue

    return min_temperature, min_index



def find_max(temperatures):
    if not temperatures:
        return ()

    max_temperature = None
    max_index = None

    for index, temperature in enumerate(temperatures):
        try:
            temperature = float(temperature)
            if max_temperature is None or temperature >= max_temperature:
                max_temperature = temperature
                max_index = index
        except ValueError:
            continue

    return max_temperature, max_index

def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    summary = ""
    for day_data in weather_data:
        date = convert_date(day_data[0])
        min_temp = convert_f_to_c(float(day_data[1]))
        max_temp = convert_f_to_c(float(day_data[2]))
        summary += f"On {date}, the minimum temperature was {format_temperature(min_temp)} and the maximum temperature was {format_temperature(max_temp)}.\n"
    return summary


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    summary = ""
    for day_data in weather_data:
        date = convert_date(day_data[0])
        min_temp = convert_f_to_c(float(day_data[1]))
        max_temp = convert_f_to_c(float(day_data[2]))
        mean_temp = convert_f_to_c(calculate_mean([float(day_data[1]), float(day_data[2])]))
        summary += f"On {date}, the minimum temperature was {format_temperature(min_temp)}, the maximum temperature was {format_temperature(max_temp)}, and the mean temperature was {format_temperature(mean_temp)}.\n"
    return summary
