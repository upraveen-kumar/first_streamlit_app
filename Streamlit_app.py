import streamlit
import pandas
import requests
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

#create a function to return normalized json data
def get_fruity_vice_data(fruit_name):
      #capture api-response. separate out fruit name from url
      fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_name);
      # take the json response & normalize it 
      fruityvice_normalized = pandas.json_normalize(fruityvice_response.json()); 
      return (fruityvice_normalized);

#create a function to return data from fruit load list table
def get_fruit_load_list():
      with conn.cursor() as cur:
            cur.execute("select * from fruit_load_list");
            return cur.fetchall();
 
streamlit.header('Fruity vice\'s fruit advice');
#get fruit name from user
try:  
  fruit_name = streamlit.text_input('enter ur fruit\'s name');
  if not fruit_name:
    streamlit.error('please select a fruit 2get info');
  else:
    streamlit.write ('user entered fruit name', fruit_name);
    if streamlit.button('get fruit load list'):
      fn_return = get_fruity_vice_data(fruit_name);   #fn call here
      streamlit.dataframe (fn_return);
      
      conn = snowflake.connector.connect(**streamlit.secrets["snowflake"]);
      streamlit.header("contents of fruit load list table");
      data_rows = get_fruit_load_list();  # fn call here
      streamlit.dataframe(data_rows);
      
except URLError as e:
    streamlit.error();
#streamlit.text(fruityvice_normalized);

streamlit.stop();

fruit_name = streamlit.text_input("what fruit would u like 2add from above list?", 'banana');
streamlit.write ("thanx 4adding ", fruit_name);

#exeercise 2demo control flow. rite now, below code will get executed unconditionally
cur.execute("insert into fruit_load_list values ('from streamlit')");

      
