import streamlit as st
import requests 

# Page 3: 
def page3():
    """
    Connects to an API and retrieves weather reports based on previously selected location
    """
    st.title("Get weather information:")

    # Retrieve location name from previous function:
    location = st.session_state.get("location_name", None)

    # Fetch weather information:

    api_key = '5a68dbd3fe6242678ac130253242505'

    if location:
        st.write(f"Location: {location}:")
        url = f'https://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=no'
        response = requests.get(url)

        if response.status_code == 200:
            weather_info = response.json()
            st.write(f"Weather in {weather_info['location']['name']}, {weather_info['location']['country']}:")
            st.write(f"Temperature: {weather_info['current']['temp_c']}°C")
            st.write(f"Weather: {weather_info['current']['condition']['text']}")
            st.write(f"Humidity: {weather_info['current']['humidity']}%")
            st.write(f"Wind: {weather_info['current']['wind_kph']}")
        
        else:
            st.write("Failed to fetch weather report information")
    
    else:
        st.write("You have not selected any location under Location information. Go to 'Location information', and input your desired latitude and longitud")


if __name__ == '__main__':
    page3()