import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

def load_fund_data():
    data = {
        'Fund': [
            'Vanguard Target Retirement 2025 Fund',
            'Vanguard Target Retirement 2030 Fund', 
            'Vanguard Target Retirement 2035 Fund',
            'Vanguard Target Retirement 2040 Fund',
            'Vanguard Target Retirement 2045 Fund'
        ],
        'Ticker': ['VTTVX', 'VTHRX', 'VTTHX', 'VFORX', 'VTIVX'],
        '1-Month': [-2.02, -2.28, -2.38, -2.48, -2.6],
        '3-Month': [-1.64, -1.69, -1.61, -1.5, -1.46],
        'YTD': [9.44, 10.64, 11.78, 12.88, 13.91],
        '1-Year': [9.44, 10.64, 11.78, 12.88, 13.91],
        '3-Year': [1.92, 2.44, 2.97, 3.51, 4.0],
        '5-Year': [5.66, 6.44, 7.2, 7.97, 8.73],
        '10-Year': [6.32, 6.92, 7.51, 8.08, 8.57],
        '15-Year': [7.61, 8.19, 8.75, 9.23, 9.56]
    }
    return pd.DataFrame(data)

def main():
    st.title('Vanguard Target Retirement Fund Returns')
    
    # Load data
    df = load_fund_data()
    
    # Multiselect for time periods
    time_periods = ['1-Month', '3-Month', 'YTD', '1-Year', '3-Year', '5-Year', '10-Year', '15-Year']
    selected_periods = st.multiselect('Select Time Periods', time_periods, default=['YTD', '1-Year'])
    
    # Multiselect for funds
    selected_funds = st.multiselect('Select Funds', df['Fund'], default=df['Fund'])
    
    # Filter data based on selections
    filtered_df = df[df['Fund'].isin(selected_funds)]
    
    # Melt the dataframe for easier plotting
    melted_df = filtered_df.melt(
        id_vars=['Fund', 'Ticker'], 
        value_vars=selected_periods, 
        var_name='Period', 
        value_name='Return'
    )
    
    # Create interactive chart
    fig = px.bar(
        melted_df, 
        x='Period', 
        y='Return', 
        color='Fund', 
        barmode='group',
        title='Fund Returns by Time Period',
        labels={'Return': 'Return (%)', 'Period': 'Time Period'}
    )
    
    # Customize layout
    fig.update_layout(
        xaxis_title='Time Period',
        yaxis_title='Return (%)',
        legend_title='Funds'
    )
    
    # Display the chart
    st.plotly_chart(fig, use_container_width=True)
    
    # Display detailed data table
    st.subheader('Detailed Returns')
    display_df = filtered_df.set_index('Fund')[selected_periods]
    st.dataframe(display_df)

if __name__ == '__main__':
    main()
