import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to load data
@st.cache  # Cache data loading for better performance
def load_data(file_path):
    data = pd.read_csv(file_path)  # Load your dataset here, modify as needed
    return data

# Function to clean data
def clean_data(df):
    # Perform any necessary data cleaning operations here
    # For example, handling missing values, converting data types, etc.
    # Replace NaNs with 0 for numeric columns as an example
    df.fillna(0, inplace=True)
    return df

# Function to plot charts
def plot_chart(df, chart_type, x_col, y_col):
    if chart_type == 'Line Chart':
        st.subheader('Line Chart')
        plt.figure(figsize=(10, 6))
        plt.plot(df[x_col], df[y_col])
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        st.pyplot()

    elif chart_type == 'Bar Chart':
        st.subheader('Bar Chart')
        plt.figure(figsize=(10, 6))
        plt.bar(df[x_col], df[y_col])
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        st.pyplot()

    elif chart_type == 'Scatter Plot':
        st.subheader('Scatter Plot')
        plt.figure(figsize=(10, 6))
        plt.scatter(df[x_col], df[y_col])
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        st.pyplot()

    elif chart_type == 'Histogram':
        st.subheader('Histogram')
        plt.figure(figsize=(10, 6))
        plt.hist(df[y_col], bins=20, edgecolor='black')
        plt.xlabel(y_col)
        plt.ylabel('Frequency')
        st.pyplot()

# Streamlit app
def main():
    st.title('Data Visualization and Analysis App')

    # Upload CSV file or use a predefined dataset
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file is not None:
        # Load data into a DataFrame
        df = load_data(uploaded_file)

        # Clean the data
        df_cleaned = clean_data(df)

        # Show the dataset
        st.subheader('Dataset')
        st.write(df_cleaned)

        # Summary statistics
        st.subheader('Summary Statistics')
        st.write(df_cleaned.describe())

        # Dropdown menu for chart selection
        st.sidebar.title('Chart Options')
        chart_type = st.sidebar.selectbox('Select chart type', ['Line Chart', 'Bar Chart', 'Scatter Plot', 'Histogram'])

        # Dropdown menus for X and Y axis selection
        x_col = st.sidebar.selectbox('Select X axis', df_cleaned.columns)
        y_col = st.sidebar.selectbox('Select Y axis', df_cleaned.columns)

        # Plot selected chart
        plot_chart(df_cleaned, chart_type, x_col, y_col)

# Run the app
if __name__ == '__main__':
    main()
