"""
main.py - A module for fetching weather information using the OpenWeatherMap API and displaying it to the user.

This module serves as the main entry point for the Weather Information App. It interacts with the user to obtain
an API key and location information, fetches weather data using the OpenWeatherMap API, and displays the weather
information to the user.

Functions:
    main(): Main function to run the Weather Information App.


"""

from weather_api import fetch_weather
from file_handler import write_to_file


def main():
    """
    Main function to run the Weather Information App.

    This function interacts with the user to obtain an API key and location information.
    It then fetches weather data using the OpenWeatherMap API and displays the weather information to the user.

    Parameters:
        None

    Returns:
        None

    Raises:
        None
    """
    print("Welcome to the Weather Information App!")
    print("You need an API key to access weather data from OpenWeatherMap.")
    print("You can obtain your API key by signing up at https://home.openweathermap.org/users/sign_up")

    # Prompt user for API key, city name, and country (optional)
    api_key = input("Please enter your OpenWeatherMap API key: ")
    location = input("Enter the city name: ")
    country = input("Enter Country (Optional): ")

    # Fetch weather data from OpenWeatherMap API
    status_code, weather_data = fetch_weather(api_key, location, country)

    if status_code == 200:
        # Write weather data to file
        write_to_file(location, weather_data)

        # Display weather information to the user
        print("Current temperature is: {:.2f} °C".format(weather_data["main"]["temp"] - 273.15))
        print("Current weather desc  : " + weather_data["weather"][0]["description"])
        print("Current Humidity      :", weather_data["main"]["humidity"], "%")
        print("Current wind speed    :", weather_data["wind"]["speed"], "kmph")
        print("Country Code          :", weather_data["sys"]["country"])
    elif 400 <= status_code < 500:  # Check if status code is in the 4xx range (Client error)
        print(
            f"Failed to fetch weather data. Client error: Status Code {status_code}, message: {weather_data['message']}")
    else:
        print(f"Failed to fetch weather data. Server error: Status Code {status_code}")
         # Check if status code is in the 5xx range (Server error)


if __name__ == "__main__":
    main()
