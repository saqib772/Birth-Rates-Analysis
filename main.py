import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Function to read the uploaded CSV file
def read_csv(file):
    df = pd.read_csv(file)
    return df

# Function to calculate total births per day
def calculate_births_per_day(df):
    births_per_day = df.groupby(['year', 'month', 'day'])['births'].sum().reset_index()
    return births_per_day

# Function to visualize birth rates over time using a line plot
def visualize_birth_rates(birth_rates):
    fig = px.line(birth_rates, x='month', y='births', color='year', title='Average Birth Rates')
    st.plotly_chart(fig)

# Function to create a bar plot for birth distribution by day
def visualize_birth_distribution(df):
    birth_counts = df['day'].value_counts().sort_index()
    fig = go.Figure(data=go.Bar(x=birth_counts.index, y=birth_counts.values))
    fig.update_layout(title='Birth Distribution by Day', xaxis_title='Day', yaxis_title='Number of Births')
    st.plotly_chart(fig)

# Function to display monthly birth trends by gender
def display_monthly_trends(df):
    gender_monthly_births = df.groupby(['year', 'month', 'gender'])['births'].sum().reset_index()
    fig = px.line(gender_monthly_births, x='month', y='births', color='gender', line_group='year',
                  title='Monthly Birth Trends by Gender')
    st.plotly_chart(fig)

# Function to perform time series forecasting with ARIMA and display predictions
def perform_forecasting(birth_rates):
    birth_rates['date'] = pd.to_datetime(birth_rates[['year', 'month']].assign(day=1))
    birth_rates_ts = birth_rates.set_index('date')
    model = sm.tsa.ARIMA(birth_rates_ts['births'], order=(2, 1, 2))
    model_fit = model.fit()
    future_years = 5
    future_dates = pd.date_range(start=birth_rates_ts.index[-1], periods=future_years*12, freq='M')
    forecast = model_fit.forecast(steps=future_years*12)
    forecast_df = pd.DataFrame({
        'date': future_dates,
        'forecasted_births': forecast
    })
    forecast_df.set_index('date', inplace=True)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=birth_rates_ts.index, y=birth_rates_ts['births'],
                             mode='lines+markers', name='Historical Data'))
    fig.add_trace(go.Scatter(x=forecast_df.index, y=forecast_df['forecasted_births'],
                             mode='lines', name='Forecasted Data'))
    fig.update_layout(title='Birth Rate Forecast for the Next 5 Years',
                      xaxis_title='Date', yaxis_title='Average Birth Rates')
    st.plotly_chart(fig)

# Streamlit app
def main():
    st.title('Birth Analysis')
    st.write('Upload a CSV file to analyze birth data')

    file = st.file_uploader('Upload CSV', type=['csv'])
    if file is not None:
        df = read_csv(file)
        st.dataframe(df.head())

        births_per_day = calculate_births_per_day(df)
        visualize_birth_rates(births_per_day)

        visualize_birth_distribution(df)

        display_monthly_trends(df)

        perform_forecasting(births_per_day)

# if __I apologize for the incomplete response. Here's the complete code:

# ```python
# Import the necessary libraries
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import statsmodels.api as sm

# Function to calculate total births per day
def calculate_births_per_day(df):
    births_per_day = df.groupby(['year', 'month', 'day'])['births'].sum().reset_index()
    return births_per_day

# Function to visualize birth rates over time using a line plot
def visualize_birth_rates(birth_rates):
    fig = px.line(birth_rates, x='month', y='births', color='year', title='Average Birth Rates')
    st.plotly_chart(fig)

# Function to create a bar plot for birth distribution by day
def visualize_birth_distribution(df):
    birth_counts = df['day'].value_counts().sort_index()
    fig = go.Figure(data=go.Bar(x=birth_counts.index, y=birth_counts.values))
    fig.update_layout(title='Birth Distribution by Day', xaxis_title='Day', yaxis_title='Number of Births')
    st.plotly_chart(fig)

# Function to display monthly birth trends by gender
def display_monthly_trends(df):
    gender_monthly_births = df.groupby(['year', 'month', 'gender'])['births'].sum().reset_index()
    fig = px.line(gender_monthly_births, x='month', y='births', color='gender', line_group='year',
                  title='Monthly Birth Trends by Gender')
    st.plotly_chart(fig)

# Function to perform time series forecasting with ARIMA and display predictions
def perform_forecasting(birth_rates):
    birth_rates['date'] = pd.to_datetime(birth_rates[['year', 'month']].assign(day=1))
    birth_rates_ts = birth_rates.set_index('date')
    model = sm.tsa.ARIMA(birth_rates_ts['births'], order=(2, 1, 2))
    model_fit = model.fit()
    future_years = 5
    future_dates = pd.date_range(start=birth_rates_ts.index[-1], periods=future_years*12, freq='M')
    forecast = model_fit.forecast(steps=future_years*12)
    forecast_df = pd.DataFrame({
        'date': future_dates,
        'forecasted_births': forecast
    })
    forecast_df.set_index('date', inplace=True)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=birth_rates_ts.index, y=birth_rates_ts['births'],
                             mode='lines+markers', name='Historical Data'))
    fig.add_trace(go.Scatter(x=forecast_df.index, y=forecast_df['forecasted_births'],
                             mode='lines', name='Forecasted Data'))
    fig.update_layout(title='Birth Rate Forecast for the Next 5 Years',
                      xaxis_title='Date', yaxis_title='Average Birth Rates')
    st.plotly_chart(fig)

# Streamlit app
def main():
    st.title('Birth Analysis')
    st.write('Upload a CSV file to analyze birth data')

    file = st.file_uploader('Upload CSV', type=['csv'])
    if file is not None:
        df = pd.read_csv(file)
        st.dataframe(df.head())

        births_per_day = calculate_births_per_day(df)
        visualize_birth_rates(births_per_day)

        visualize_birth_distribution(df)

        display_monthly_trends(df)

        perform_forecasting(births_per_day)

if __name__ == '__main__':
    main()
