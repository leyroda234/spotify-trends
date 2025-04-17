import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load Tito Double P's dataset
df = pd.read_csv('tito_double_p_tracks.csv')
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
df['release_year'] = df['release_date'].dt.year

# Sidebar
st.sidebar.title("🎤 Tito Double P Dashboard")
year_filter = st.sidebar.multiselect(
    "Filter by year", 
    options=sorted(df['release_year'].dropna().unique()), 
    default=[2023, 2024, 2025]
)

df_filtered = df[df['release_year'].isin(year_filter)]

# Main Title
st.title("📈 Tito Double P – Popularity Insights")

# Boxplot
st.subheader("Popularity Distribution by Year")
fig, ax = plt.subplots()
data = [df[df['release_year'] == y]['popularity'].dropna() for y in year_filter]
ax.boxplot(data, labels=year_filter, patch_artist=True,
           boxprops=dict(facecolor='lightblue'),
           medianprops=dict(color='blue'),
           flierprops=dict(marker='o', markerfacecolor='red', markersize=6))
ax.set_ylabel("Popularity (0–100)")
st.pyplot(fig)

# Line chart
st.subheader("Track Popularity Over Time")
df_sorted = df_filtered.sort_values('release_date')
st.line_chart(df_sorted[['release_date', 'popularity']].set_index('release_date'))
