import streamlit
import pandas

streamlit.title('My Mother\'s New Diner Menu');
streamlit.header('Breakfast Menu');
streamlit.text('🥣 Omega 3 & blueberry oatmeal');
streamlit.text('🥗 kale, spinach & rocket smootie');
streamlit.text('🐔 hard boiled free range egg');
streamlit.text('🥑🍞 avocado toast');

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇');
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt");
#instead of giving index by nbr, give it a name i.e in the multi select below, index is now fruit name (1st col of csv file), instead of position!
my_fruit_list = my_fruit_list.set_index('Fruit');

#multi select list -- users can pick their own fruit combo
streamlit.multiselect('pick ur choice of fruits:', list(my_fruit_list.index));
streamlit.dataframe(my_fruit_list);
