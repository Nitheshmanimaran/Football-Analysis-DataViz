import json
from urllib.request import urlopen
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from Homepage import footer
#ignore warnings
import warnings
warnings.filterwarnings('ignore')

st.markdown(footer, unsafe_allow_html=True)




# Importing the data
df = pd.read_csv("D:/EPITA/data-reporting-visualisation/Final_Project/Data/ucl_stats.csv")

# Input box to the user to select which category to display
st.title("Champions League Statistics")


# Getting the year using the slider
year = st.slider('Select a year to see the statistics of the Champions League', 1993, 2020)

category = st.selectbox("Select a Category to visualise", ('Champions and their stats','Most Wins','Most Loss','Most Draws','Most Goals Scored','Most Goals Conceded','Most Group Points','Goal Difference'))
if category == 'Champions and their stats':
    st.header("Champions and their stats")
    # Filtering the data for the selected year
    df_year = df[df['year']==year]
    # Filtering the data for the champions
    df_champions = df_year[df_year['champions']==1]
    # Displaing champions name
    st.write("The Champions of the year",year,"are",df_champions['team'].values[0])
    #st.write("The Champions of the year",year,"are",a)
    # Displaying the df_champions as a table without the index
    st.table(df_champions.set_index('team'))

elif category == 'Most Wins':
    st.header("Most Wins")
    # Filtering the data for the selected year
    df_year = df[df['year']==year]
    # Sorting the data based on the wins
    df_year = df_year.sort_values(by=['wins'], ascending=False)
    # Getting the top 10 teams
    df_year = df_year.head(10)
    # Creating a bar chart
    fig = px.bar(df_year, x='team', y='wins', color='team', title='Top 10 Teams with Most Wins')
    st.plotly_chart(fig)
    with st.expander('See Explanation:'):
        st.markdown('This chart shows the top 10 teams with the most wins in the Champions League. The number of wins are calculated based on the number of matches played by the team in the Champions League. The team with the most wins is displayed at the top of the chart.')

elif category == 'Most Loss':
    st.header("Most Loss")
    # Filtering the data for the selected year
    df_year = df[df['year']==year]
    # Sorting the data based on the losses
    df_year = df_year.sort_values(by=['losts'], ascending=False)
    # Getting the top 10 teams
    df_year = df_year.head(10)
    # Creating a bar chart
    fig = px.bar(df_year, x='team', y='losts', color='team', title='Top 10 Teams with Most Loss')
    st.plotly_chart(fig)
    with st.expander('See Explanation:'):
        st.markdown('This chart shows the top 10 teams with the most losses in the Champions League. The number of losses are calculated based on the number of matches played by the team in the Champions League. The team with the most losses is displayed at the top of the chart.')

elif category == 'Most Draws':
    st.header("Most Draws")
    # Filtering the data for the selected year
    df_year = df[df['year']==year]
    # Sorting the data based on the draws
    df_year = df_year.sort_values(by=['draws'], ascending=False)
    # Getting the top 10 teams
    df_year = df_year.head(10)
    # Creating a bar chart
    fig = px.bar(df_year, x='team', y='draws', color='team', title='Top 10 Teams with Most Draws')
    st.plotly_chart(fig)
    with st.expander('See Explanation:'):
        st.markdown('This chart shows the top 10 teams with the most draws in the Champions League. The number of draws are calculated based on the number of matches played by the team in the Champions League. The team with the most draws is displayed at the top of the chart.')

elif category == 'Most Goals Scored':
    st.header("Most Goals Scored")
    # Filtering the data for the selected year
    df_year = df[df['year']==year]
    # Sorting the data based on the goals scored
    df_year = df_year.sort_values(by=['goals_scored'], ascending=False)
    # Getting the top 10 teams
    df_year = df_year.head(10)
    # Creating a bar chart
    fig = px.bar(df_year, x='team', y='goals_scored', color='team', title='Top 10 Teams with Most Goals Scored')
    st.plotly_chart(fig)
    with st.expander('See Explanation:'):
        st.markdown('This chart shows the top 10 teams with the most goals scored in the Champions League. The number of goals scored are calculated based on the number of matches played by the team in the Champions League. The team with the most goals scored is displayed at the top of the chart.')

elif category == 'Most Goals Conceded':
    st.header("Most Goals Conceded")
    # Filtering the data for the selected year
    df_year = df[df['year']==year]
    # Sorting the data based on the goals conceded
    df_year = df_year.sort_values(by=['goals_conceded'], ascending=False)
    # Getting the top 10 teams
    df_year = df_year.head(10)
    # Creating a bar chart
    fig = px.bar(df_year, x='team', y='goals_conceded', color='team', title='Top 10 Teams with Most Goals Conceded')
    st.plotly_chart(fig)
    with st.expander('See Explanation:'):
        st.markdown('This chart shows the top 10 teams with the most goals conceded in the Champions League. The number of goals conceded are calculated based on the number of matches played by the team in the Champions League. The team with the most goals conceded is displayed at the top of the chart.')

elif category == 'Most Group Points':
    st.header("Most Group Points")
    # Filtering the data for the selected year
    df_year = df[df['year']==year]
    # Sorting the data based on the group points
    df_year = df_year.sort_values(by=['group_point'], ascending=False)
    # Getting the top 10 teams
    df_year = df_year.head(10)
    # Creating a bar chart
    fig = px.bar(df_year, x='team', y='group_point', color='team', title='Top 10 Teams with Most Group Points')
    st.plotly_chart(fig)
    with st.expander('See Explanation:'):
        st.markdown('This chart shows the top 10 teams with the most group points in the Champions League. The number of group points are calculated based on the number of matches played by the team in the Champions League. The team with the most group points is displayed at the top of the chart.')

elif category == 'Goal Difference':
    st.header("Goal Difference")
    # Filtering the data for the selected year
    df_year = df[df['year']==year]
    # Sorting the data based on the goal difference
    df_year = df_year.sort_values(by=['gd'], ascending=False)
    # Getting the top 10 teams
    df_year = df_year.head(10)
    # Creating a bar chart
    fig = px.bar(df_year, x='team', y='gd', color='team', title='Top 10 Teams with the Highest Goal Difference')
    st.plotly_chart(fig)
    with st.expander('See Explanation:'):
        st.markdown('This chart shows the top 10 teams with the highest goal difference in the Champions League. The goal difference is calculated by subtracting the goals conceded from the goals scored. The team with the highest goal difference is displayed at the top of the chart.')




st.header('Other Interesting Charts')

# Goals scored vs Goals conceded by each team
st.subheader('Goals Scored vs Goals Conceded')

#Getting the team from the user

a = df['team'].unique()
# SORTING THE TEAM NAMES
a.sort()
team = st.selectbox('Select a team', a, index=13)
# Filtering the data for the selected Team
df_team = df[df['team']==team]
# Creating a scatter plot
fig = px.scatter(df_team, x='goals_scored', y='goals_conceded', color='year', title='Goals Scored vs Goals Conceded')
st.plotly_chart(fig)
with st.expander('See Explanation:'):
    st.markdown('This chart shows the goals scored and goals conceded by each team in the Champions League. The team selected by the user is displayed in the chart. The year is displayed on the x-axis and the goals scored and goals conceded are displayed on the y-axis. The user can select a team from the dropdown menu to see the goals scored and goals conceded by the team in the Champions League.')
































