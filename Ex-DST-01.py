import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import time

#---------------------------------------------------------------------------------------
#To run Streamlit, we must run one expression streamlit
st.title('Dry Test - 5" Bridge Plug @ 3760 m')
st.header('Shahini Oil Field')
st.subheader('EXP Well SNI-001')
st.caption('_Rig 31-Fath NIDC_')
st.text('This test has been done on 2023/Oct/18 by NIDC.')
st.divider() # 👈 Draws a horizontal rule
#D:\Work\Python Jobs>streamlit run ex-dst-01.py
#-------------------------------------------------------------------------------------------
#st.button('Generate Plots')
#st.number_input('Enter Time')

#date = st.date_input('Pick a date')
#colorarmin = st.color_picker('Pick a color')

df = pd.read_csv('D:\Work\Python Jobs\Sample Data\REPORT CMK-21\Gauges 90563 BOTTOM\dst-01.txt',  
                 sep='\s'
                 )
#st.dataframe(df)
#-------------------------------------------------------------------------------------------
# Cache the dataframe so it's only loaded once
@st.cache_data
def load_data():
    return pd.DataFrame(df)

#Show Dataframe Check Box
if st.checkbox('Show the data _(test results)_',  
               value=False, key="use_container_width"  
               ):
    chart_data = pd.DataFrame(df)
    st.dataframe(df, use_container_width = st.session_state.use_container_width) 
    df = load_data()

# Boolean to resize the dataframe, stored as a session state variable
# Display the dataframe and allow the user to stretch the dataframe
# across the full width of the container, based on the checkbox value
#--------------------------------------------------------------------------------------------

fig1 = px.line(df, x='Elapsed-Time', y='Pressure', color='Date')
fig2 = px.line(df, x='Elapsed-Time', y='Temperature', color='Date')

#fig3 = px.scatter_3d(df, x='Elapsed-Time', y='Pressure', z="Temperature" )
st.plotly_chart(fig1, use_container_width=True)
st.divider() # 👈 Draws a horizontal rule
st.plotly_chart(fig2, use_container_width=True)
#st.plotly_chart(fig3)
#------------------------------------------------------------------------------------------

import scipy
import plotly.figure_factory as ff

# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig33 = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig33, use_container_width=True)



































