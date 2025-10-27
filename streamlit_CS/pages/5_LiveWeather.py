import streamlit as st
import pandas as pd
import requests
import plotly.express as px
import time

st.set_page_config(page_title="Live Weather", page_icon="🌦️", layout="wide")

st.title("🌦️ Live Weather in Denver")
st.caption("Using the Open-Meteo API — auto-refreshing line chart of temperature over time.")

# --- Constants ---
LAT, LON = 39.7392, -104.9903  # Denver
API_URL = f"https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&current=temperature_2m,wind_speed_10m"

HEADERS = {"User-Agent": "msudenver-dataviz-class/1.0", "Accept": "application/json"}

# --- Cached fetch ---
@st.cache_data(ttl=600, show_spinner=False)
def fetch_weather():
    """Fetch current weather data (safe and cached)."""
    try:
        resp = requests.get(API_URL, headers=HEADERS, timeout=10)
        resp.raise_for_status()
        j = resp.json()["current"]
        df = pd.DataFrame([{
            "time": pd.to_datetime(j["time"]),
            "temperature": j["temperature_2m"],
            "wind": j["wind_speed_10m"]
        }])
        return df, None
    except requests.RequestException as e:
        return None, f"Weather API error: {e}"

# --- Auto-refresh settings ---
st.subheader("🔁 Auto Refresh Settings")
refresh_sec = st.slider("Refresh every (sec)", 10, 120, 30)
auto_refresh = st.toggle("Enable auto-refresh", value=False)
st.caption(f"Last refreshed at: {time.strftime('%H:%M:%S')}")

# --- Session state history ---
if "weather_history" not in st.session_state:
    st.session_state.weather_history = pd.DataFrame(columns=["time", "temperature", "wind"])

# --- Fetch data ---
df, err = fetch_weather()
if err:
    st.warning(err)
else:
    st.session_state.weather_history = (
        pd.concat([st.session_state.weather_history, df])
        .drop_duplicates(subset="time")
        .tail(20)  # keep short history
    )

# --- Plot temperature over time ---
if not st.session_state.weather_history.empty:
    st.subheader("Temperature (C) Over Time")
    fig = px.line(
        st.session_state.weather_history,
        x="time",
        y="temperature",
        title="Live Temperature in Denver",
        markers=True
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("No weather data available yet.")

# If auto-refresh is ON, wait and rerun the app
if auto_refresh:
    time.sleep(refresh_sec)
    fetch_weather.clear()  # clear cache to force new fetch
    st.rerun()
