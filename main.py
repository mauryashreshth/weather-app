import streamlit as st
import requests
import json

st.set_page_config(page_title="Weather App")
st.markdown(
    '''
    <html>
        <head>
            <title>Weather App</title>
        </head>
    </html>
    <style>
        [data-testid="stAppViewContainer"] {
            background-image: url("https://c1.wallpaperflare.com/preview/793/57/104/storm-storm-clouds-sky-clouds.jpg");
            background-size: cover;
        }
        .body {
            background-color: transparent !important;
        }
        .centered {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }
        .box {
            background-color: rgba(173, 216, 230, 0.5);
            border: 1px solid #ddd;
            padding: 10px;
            border-radius: 5px;
        }
    </style>
    ''',
    unsafe_allow_html=True,
)

st.title("Live weather powered by WeatherAPI")

city = st.text_input("Enter a city name", "New York")
weather_data = {}
# Create a button for the user to trigger data retrieval
if st.button("Get Weather Data"):
    fp = open("key.txt", "r")
    API_key = fp.readline()
    fp.close()
    # Texting phase
    url = f'http://api.weatherapi.com/v1/current.json?key={API_key}&q={city}'

    data = requests.get(url)
    weather_data = json.loads(data.text)
    print(weather_data)
    # Display the weather data in a box below the input controls
    st.write(
        f'''
            ## Weather Data
            <div class="box">
                <div class = "centered">
                <h6 style = "display: inline">City: {weather_data['location']['name']}</h6>
                <h6 style = "display: inline">Temperature: {weather_data['current']['temp_c']}</h6>
                <h6 style = "display: inline">Conditions: {weather_data['current']['condition']['text']}</h6>
                <img src="{weather_data['current']['condition']['icon']}" alt="Weather Image" style="max-width: 100px;">
                <h6 style = "display: inline">Last updated: {weather_data['current']['last_updated']}</h6>
                </div>
            </div>
            ''',
        unsafe_allow_html=True,
    )






