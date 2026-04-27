import streamlit as st
price = st.number_input("Enter Price of Product:")
discount = st.slider("Select Discount Percentage:",0,50)
if st.button("Calculate Discounted Price"):
    discounted_price = price - (price * discount / 100)
    st.write("Final Price:", discounted_price)
    st.table({"Original Price": [price],  "Discounted Price": [discounted_price]})    
    
