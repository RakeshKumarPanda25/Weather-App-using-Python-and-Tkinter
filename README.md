# Weather-App-using-Python-and-Tkinter
The primary goal of this project is to build a simple desktop application using Python and Tkinter that allows users to:

-> Enter the name of a city

-> Retrieve real-time weather data via the OpenWeatherMap API

-> Display temperature, condition, humidity, and wind speed in a user-friendly format

**Technologies Used:**

Component	      -     Description

Python	        -     Core programming language

Tkinter         -     GUI framework for building the app interface

Requests        -	   For sending HTTP requests to the weather API

OpenWeatherMap  -    API	Provides real-time weather data for any city

**Working:**

*User Interface (Tkinter):*

![image](https://github.com/user-attachments/assets/f0e8f014-5fab-4d16-86d5-a07ca537e4ce)

A GUI window is launched with:

  -> A label for the app title

  -> An entry box for the user to type a city name

  -> A "Get Weather" button

  -> A label to display results

*User Action:*

-> The user types a city name and clicks the "Get Weather" button.

*Backend Logic (get_weather() function):*

-> The function builds the API URL using the entered city and your OpenWeatherMap API_KEY.

-> A GET request is sent to the OpenWeatherMap server.

-> If a valid response is received (status code 200):

  -> Temperature, weather description, humidity, and wind speed are extracted.

  -> This information is displayed in a formatted string on the GUI.

-> If the city is invalid (e.g., typo), it shows an error message.

*Post-Processing:*

![image](https://github.com/user-attachments/assets/820aeb47-d4e2-49b7-a66c-949494c1f0b8)

-> The entry box is cleared after each request.

**Features:**

-> Clean and user-friendly GUI

-> Real-time weather data retrieval

-> Handles both valid and invalid inputs

-> Automatically clears input after submission

**Limitations:**

-> The app requires internet access to work (as it relies on live API calls).

-> Error handling is minimal (e.g., no timeout or network error management).

-> The API key is hardcoded in the script — not secure for public release.

-> Does not support advanced features like forecast, multi-city display, or graphics.

**Possible Improvements:**

1. Add support for:

  -> Country code to improve city accuracy (e.g., "Paris, FR")

  -> Weather icons or images based on conditions

  -> Forecasts for multiple days using OpenWeatherMap's forecast API

2. Enhance error handling:

  -> Show specific messages for network failures or invalid inputs

3. Improve UI:

  -> Add themes, icons, or modern design using ttk or other GUI libraries

4. Secure the API Key:

  -> Store it in an environment variable or external config file

**Conclusion:**
This Weather App provides a solid foundation for GUI-based API interaction using Python. It is an excellent demonstration of combining frontend (Tkinter) and backend (HTTP request, API handling) skills to create a responsive desktop tool.
