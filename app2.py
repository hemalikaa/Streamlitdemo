import pandas as pd
import numpy as np 
import streamlit as st
import plotly.express as px
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns

st.title('More charts and utilities')
data = pd.read_csv('https://raw.githubusercontent.com/qurat-azim/instructionaldatasets/main/data/penguins.csv')
st.sidebar.header("Select Options")
selected_category = st.sidebar.selectbox("Select Species", options = ['All','Adelie','Gentoo','Chinstrap'])

#filter data
if selected_category is 'All':
    filtered_data = data
else:
    filtered_data = data[data['species'] == selected_category]
    

#matplot lib
st.write("#### Matplotlib Histogram")
fig, ax = plt.subplots()
ax.hist(filtered_data['culmen_length_mm'],bins=30, color="skyblue", edgecolor="black")
ax.set_title("Matplotlib Histogram for Culmen Length")
ax.set_xlabel("Value")
ax.set_ylabel("Frequency")
st.pyplot(fig)

st.write("#### Seaborn Density Plot")
fig, ax = plt.subplots()
fig = sns.displot(filtered_data['culmen_depth_mm'], color="black", kind='kde', ax=ax, fill=True)
ax.set_title("Seaborn Density for Culmen Depth")
ax.set_xlabel("Value")
ax.set_ylabel("Density")
st.pyplot(fig)

st.write("### Altair Scatter Plot")

scatter_plot = alt.Chart(filtered_data).mark_circle().encode(
    x = alt.X('flipper_length_mm', title='Flipper Length'),
    y = alt.Y('body_mass_g', title = 'Body Mass'),
    color = alt.Color('island',scale=alt.Scale(scheme='tableau10')),
    tooltip = ['island', 'flipper_length_mm', 'body_mass_g']
).properties(
    width = 600,
    height = 400,
    title = "Scatter Plot of Penguin"
).interactive()

st.altair_chart(scatter_plot, use_container_width=True)