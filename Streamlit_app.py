import streamlit
#import pandas
#import requests
import snowflake.connector
from urllib.error import URLError


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
selected_fruits = streamlit.multiselect('pick ur choice of fruits:', list(my_fruit_list.index), ['Watermelon', 'Honeydew', 'Cantaloupe']);
displayed_fruits = my_fruit_list.loc[selected_fruits]
streamlit.dataframe(displayed_fruits);

streamlit.header('Fruity vice\'s fruit advice');
#get fruit name from user
fruit_name = streamlit.text_input('enter ur fruit\'s name', 'banana');
streamlit.write ('user entered fruit name', fruit_name);

#capture api-response. separate out fruit name from url
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_name);

# tempoararily, stop further execution from here
streamlit.stop();

# take the json response & normalize it 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json()); 
streamlit.dataframe(fruityvice_normalized);
streamlit.text(fruityvice_response);

conn = snowflake.connector.connect(**streamlit.secrets["snowflake"]);
cur = conn.cursor();
cur.execute("select * from fruit_load_list");
data_row = cur.fetchall();
streamlit.header("contents of fruit load list table");
streamlit.dataframe(data_row);

fruit_name = streamlit.text_input("what fruit would u like 2add from above list?", 'banana');
streamlit.write ("thanx 4adding ", fruit_name);

#exeercise 2demo control flow. rite now, below code will get executed unconditionally
cur.execute("insert into fruit_load_list values ('from streamlit')");

