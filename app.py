import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Working with streamlit")
df = pd.DataFrame({"A": [1,2,3,4], "B": [5,6,7,8]})

st.subheader("Here's our first attempt at using dataframe using streamlit")
st.write(df)

st.subheader("Working with charts")
chart_data = pd.DataFrame(np.random.randn(20,3),
columns = ['a', 'b', 'c'])

st.write('Making a line chart')
st.line_chart(chart_data)

st.write('Making a bar chart')
st.bar_chart(chart_data)

st.write('Making a area chart')
st.area_chart(chart_data)

st.write('Making a map')
map_data = pd.DataFrame(np.random.randn(1000, 2)/ [50,50] + [52.5200, 13.4050], 
columns = ['lat', 'lon'])

st.map(map_data)

x = np.linspace(0, np.pi * 2, 100)
t = st.slider('t', 0.0, 10.0, )

x0 = st.slider('x0', 0.0, np.pi * 2, 0.0)

y = np.sin(x*t+x0)

if st.checkbox('Show linechart'):
    st.line_chart(y)

y = np.sin(x*t+x0)
function_name = st.selectbar('Function'), ['sin', 'cos', 'tan']
function_dict = {'sin': np.sin, 'cos': np.cos, 'tan': np.tan}

if st.checkbox("Show line chart"):
    y = function_dict[function_name](x*t+x0)
    st.line_chart(pd.DataFrame({f"{function_name}(x*t+x0)": y},))

# with st.sidebar:
#     st.write("this is the sidebar")
#     x = np.linspace(0, np.pi*2, 100)

#     t = st.slider("t", 0.0, 10.0, 1.0)

#     x0 = st.slider('x0', 0.0, np.pi * 2, 0.0)

#     y = np.sin(x*t+x0)

#     function_name = st.selectbox("Function", )