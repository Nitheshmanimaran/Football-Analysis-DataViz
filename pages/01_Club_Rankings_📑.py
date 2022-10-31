# Importing Soccer_Football Clubs Ranking.csv
from unicodedata import category
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go


#ignore warnings
import warnings
warnings.filterwarnings('ignore')

from Homepage import footer

st.markdown(footer, unsafe_allow_html=True)


df = pd.read_csv("D:/EPITA/data-reporting-visualisation/Final_Project/Data/Soccer_Football Clubs Ranking.csv")

#Input box to the user to select which category to display
st.title("Soccer Football Clubs Ranking")

category = st.selectbox("Select Category", ('Ranking - Top', 'Ranking - Bottom','Points - Scored - Top','Points - Scored - Bot','Points Gained In 1 year'))

# Getting the number 

category_number = st.slider("Enter the Number of clubs you want to see", 1, 100, 10)

# Displaying the data

if category == 'Ranking - Top':
    #Getting the top 10 columns in the csv file using the ranking column
    df = df.sort_values(by=['ranking'], ascending=True)
    top_10 = df.head(category_number)
    #Chart for the top 10 clubs in the world
    fig = px.bar(top_10, x='club name ', y='point score', color='club name ', title='Top 10 Clubs in the World')
    st.plotly_chart(fig)
    with st.expander('See Explanation:'):
        st.markdown('This chart shows the top ranking holders in respect with the number of clubs chosen. The points are calculated based on the number of wins, draws and losses. The points are calculated as follows: 3 points for a win, 1 point for a draw and 0 points for a loss. The points are calculated for each club and the bottom 10 clubs are displayed in the chart.')

elif category == 'Ranking - Bottom':
    #Getting the bottom 10 columns in the csv file using the ranking column
    df = df.sort_values(by=['ranking'], ascending=False)
    bottom_10 = df.head(category_number)
    #Chart for the bottom 10 clubs in the world
    fig = px.bar(bottom_10, x='club name ', y='point score', color='club name ', title='Bottom 10 Clubs in the World')
    st.plotly_chart(fig)
    with st.expander('See Explanation:'):
        st.markdown('This chart shows the bottom ranking holders in respect with the number of clubs chosen. The points are calculated based on the number of wins, draws and losses. The points are calculated as follows: 3 points for a win, 1 point for a draw and 0 points for a loss. The points are calculated for each club and the bottom 10 clubs are displayed in the chart.')

elif category == 'Points - Scored - Top':
    #Getting the top 10 columns in the csv file using the point score column
    df = df.sort_values(by=['point score'], ascending=True)
    top_10 = df.head(category_number)
    #Chart for the top 10 clubs in the world
    fig = px.bar(top_10, x='club name ', y='point score', color='club name ', title='Top 10 Clubs in the World')
    st.plotly_chart(fig)
    with st.expander('See Explanation:'):
        st.markdown('This chart shows the top 10 point holders in respect with the number of clubs chose. The points are calculated based on the number of wins, draws and losses. The points are calculated as follows: 3 points for a win, 1 point for a draw and 0 points for a loss. The points are calculated for each club and the top 10 clubs are displayed in the chart.')

elif category == 'Points - Scored - Bot':
    #Getting the bottom 10 columns in the csv file using the point score column
    df = df.sort_values(by=['point score'], ascending=False)
    bottom_10 = df.head(category_number)
    #Chart for the bottom 10 clubs in the world
    fig = px.bar(bottom_10, x='club name ', y='point score', color='club name ', title='Bottom 10 Clubs in the World')
    st.plotly_chart(fig)
    with st.expander('See Explanation:'):
        st.markdown('This chart shows the bottom 10 point holders in respect with the number of clubs. The points are calculated based on the number of wins, draws and losses. The points are calculated as follows: 3 points for a win, 1 point for a draw and 0 points for a loss. The points are calculated for each club and the bottom 10 clubs are displayed in the chart.')

elif category == 'Points Gained In 1 year':
    #Getting the top 10 columns in the csv file using the point score column
    df = df.sort_values(by=['1 year change'], ascending=False)
    top_10 = df.head(category_number)
    #Chart for the top 10 clubs in the world
    fig = px.bar(top_10, x='club name ', y='point score', color='club name ', title='Top 10 Clubs in the World')
    st.plotly_chart(fig)
    with st.expander('See Explanation:'):
        st.markdown('This chart shows selected number of clubs in the world based on the points gained by them in 1 year')


st.header("Interesting observations about clubs")
#Getting top 10 countries in the csv file using the ranking column based on clubs having the highest point score
df = df.sort_values(by=['point score'], ascending=False)
top_10_countries = df.head(10)
#Sunburst plot for the top 10 countries in the world based on clubs having the highest point score
st.markdown('## Sunburst Plot for the Top 10 Countries in the World based on Clubs having the Highest Point Score')
fig = px.sunburst(top_10_countries, path=['country', 'club name ','point score'], values='point score')
# Increasing the size of the sunburst plot
fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))
st.plotly_chart(fig)
with st.expander('See Explanation:'):
    st.markdown('There are three layers to this sunburst graph for top 10 clubs with score, country and club. For example, if we choose England, it shows us its points with its clubs, and we can furthur into a simple club')


#Getting bottom 10 countries in the csv file using the ranking column based on clubs having the lowest point score
df = df.sort_values(by=['point score'], ascending=True)
bottom_10_countries = df.head(10)
#Sunburst plot for the bottom 10 countries in the world based on clubs having the lowest point score
st.markdown('## Sunburst Plot for the Bottom 10 Countries in the World based on Clubs having the Lowest Point Score')
fig = px.sunburst(bottom_10_countries, path=['country', 'club name ','point score'], values='point score')
# Increasing the size of the sunburst plot
fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))
st.plotly_chart(fig)
with st.expander('See Explanation:'):
    st.markdown('There are three layers to this sunburst graph for bottom 10 with score, country and club. For example, if we choose Moldova, it shows us its points with its club, FC Codru Lozova ')

# Bubble Plot for the top 10 clubs in the world based on points scored
df = df.sort_values(by=['point score'], ascending=False)
top_10 = df.head(10)
st.markdown('## Bubble Chart for the top 10 clubs in the world based on points scored')
fig = px.scatter(top_10, x='club name ', y='point score', size='point score', color='club name ', title='Top 10 Clubs in the World based on points scored')
st.plotly_chart(fig)
with st.expander('See Explanation:'):
    st.markdown('We have made a bubble chart for the 10 top clubs in the world based on the points scored.')
    




