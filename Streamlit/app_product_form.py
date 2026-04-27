import streamlit as st
st.sidebar.title("Product Form")
product_name = st.sidebar.text_input("Product Name:")
Category = st.sidebar.selectbox("Select Category:", ["Electronics", "Clothing", "Books", "Home & Kitchen"])
price = st.sidebar.number_input("Enter Price of Product:")
if st.sidebar.button("Add Product"):
    st.write("Product Name:", product_name)
    st.write("Category:", Category)
    st.write("Price:", price)
    st.write("Product added successfully!")