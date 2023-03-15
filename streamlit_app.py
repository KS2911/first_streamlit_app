import streamlit

streamlit.title('My Parents new healty dinner')
streamlit.header('Breakfast Menu')
streamlit.text('Parantha')
streamlit.text('chole puri')
streamlit.text('Dosa')
streamlit.header('🥣 🥗 🐔 🥑🍞')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
