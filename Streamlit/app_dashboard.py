import streamlit as st
st.title("Simple Sales Dashboard")
#st.description("Simple Sales Dashboard")
month = st.selectbox("months:", ["January", "February", "March","April"])
sales = {"January":1200,
         "February":1500,
         "March":900,
         "April":2000
         }
st.metric(label = month,value=sales[month])
#st.write("Sales Data:", sales)
st.bar_chart(list(sales.values()))