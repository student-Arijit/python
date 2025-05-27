import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Streamlit page config
st.set_page_config(page_title="Death by State Dashboard", layout="wide")

# Title
st.title("📊 Deaths by State Visualization")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("data.csv")
    df.drop('#', axis=1, inplace=True)
    df.drop(index=0, axis=0, inplace=True)
    df["Death"] = pd.to_numeric(df["Death"], errors='coerce')
    return df

data = load_data()

# Sidebar options
st.sidebar.header("⚙️ Controls")
sort_data = st.sidebar.checkbox("Sort by Deaths", value=True)
chart_type = st.sidebar.selectbox("Chart Type", ["Bar Chart", "Line Chart"])
bar_color = st.sidebar.color_picker("Pick a Color", "#87CEEB")  # skyblue default

# Sort data if required
if sort_data:
    data = data.sort_values(by="Death", ascending=False)

# Plotting
fig, ax = plt.subplots(figsize=(12, 6))
x_axis = data["State"]
y_axis = data["Death"]

if chart_type == "Bar Chart":
    ax.bar(x_axis, y_axis, color=bar_color, width=0.6)
    ax.set_title("Bar Chart: Deaths by State", fontsize=16)
else:
    ax.plot(x_axis, y_axis, color=bar_color, marker='p')
    ax.set_title("Line Chart: Deaths by State", fontsize=16)

ax.set_xlabel("State", fontsize=12)
ax.set_ylabel("Death Count", fontsize=12)
plt.xticks(rotation=90)

# Show chart
st.pyplot(fig)

# Show raw data
st.subheader("📋 Data Table")
st.dataframe(data, use_container_width=True)
