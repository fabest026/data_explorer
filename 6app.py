import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load built-in Seaborn datasets
dataset_options = ['titanic', 'iris', 'tips']

# Set up the sidebar
st.sidebar.title("Farhan Dataset Explorer App")

# Dataset upload option
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type="csv")
selected_dataset = st.sidebar.selectbox("Or choose a predefined dataset", dataset_options)

# Load the dataset
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = sns.load_dataset(selected_dataset)

# EDA
st.header("Exploratory Data Analysis")
st.write(df.head())
st.write("Basic statistics:")
st.write(df.describe())

# Plotting options
st.sidebar.title("Plot Options")
plot_type = st.sidebar.selectbox("Choose a plot type", ["Scatter Plot", "Bar Chart", "Histogram"])
x_axis = st.sidebar.selectbox("X-axis column", df.columns)
y_axis = st.sidebar.selectbox("Y-axis column", df.columns)

# Plotting
if plot_type == "Scatter Plot":
    fig, ax = plt.subplots()
    ax.scatter(df[x_axis], df[y_axis])
elif plot_type == "Bar Chart":
    fig, ax = plt.subplots()
    ax.bar(df[x_axis], df[y_axis])
elif plot_type == "Histogram":
    fig, ax = plt.subplots()
    ax.hist(df[x_axis])
st.pyplot(fig)