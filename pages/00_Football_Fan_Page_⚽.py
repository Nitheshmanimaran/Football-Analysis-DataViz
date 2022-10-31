from email.mime import image
import json
from tkinter import Image
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
df = pd.read_csv("D:/EPITA/data-reporting-visualisation/Final_Project/Data/FIFA23_official_data.csv")
st.title("Welcome to the Football Fan Page")

st.header("Dream Team Based on Your Preferences")
st.markdown(" Based on The Visualisation below done in various ways, you can choose your dream team based on your preferences. ")
st.write("This page is dedicated to all the football fans out there. I have worked on this project to analyse highs and lows of the football game, through data. I have used various datasets to make this project in order to have a diversified outlook on football, and explain various aspects of it")

st.header("Imagine you are a football manager, and you have to choose your dream team. You can choose your dream team based on the following parameters: ")





#Most Expensive Players
st.title(" **1. Your Dream Team - Most Expensive Players** ")
#Removing nan values from the value column
df = df[df['Value'].notna()]
df_value = df[df['Value'].str.contains('M')]
# Getting the Top players in the csv file using the value column
# Removing M and euro from the value column
df_value['Value'] = df_value['Value'].str.replace('M', '')
df_value['Value'] = df_value['Value'].str.replace('€', '')
df_value['Value'] = df_value['Value'].astype(float)
df_value = df_value.sort_values(by=['Value'], ascending=False)
top_10_value = df_value.head(11)
imagelist = []
for i in top_10_value['Photo']:
    #Displaying the 4 images horizontally using the st.image function
    imagelist = imagelist + [i]
st.image(imagelist, width=100)
# Bar chart of the top 10 players based on the value column
fig = px.bar(top_10_value, x='Name', y='Value', color='Club', title='Top 10 Players Based on Value')
st.plotly_chart(fig)






#Most skillful players
st.title(" **2. Your Dream Team - Most Skillful Players** ")
#Removing nan values from the value column
df = df[df['Overall'].notna()]
top_10_overall = df.sort_values(by=['Overall'], ascending=False).head(11)
imagelist_1 = []
for i in top_10_overall['Photo']:
    # Displaying all the images in the same row
    imagelist_1 = imagelist_1 + [i]
st.image(imagelist_1, width=100)
# Bar chart of the top 10 players based on the overall column
fig_1 = px.bar(top_10_overall, x='Name', y='Overall', color='Club', title='Top 10 Players Based on Overall')
st.plotly_chart(fig_1)






#Top 11 players in each country
st.title(" **3. Your Dream Team - Top 11 Players in Each Country** ")
#Select a country
nationality = st.selectbox('Select a country', df['Nationality'].unique())
df_country = df[df['Nationality'] == nationality]
country_flag = df_country['Flag'].iloc[0]
st.image(country_flag, width=50)
#Filtering the data based on the country selected
df_country = df[df['Nationality'] == nationality]
#Sorting the data based on the overall column
df_country = df_country.sort_values(by=['Overall'], ascending=False).head(11)
imagelist_2 = []
for i in df_country['Photo']:
    # Displaying all the images in the same row
    imagelist_2 = imagelist_2 + [i]
st.image(imagelist_2, width=100)
# Bar chart of the top 10 players based on the overall column
fig_2 = px.bar(df_country, x='Name', y='Overall', color='Club', title='Top 11 Players in ' + nationality)
st.plotly_chart(fig_2)






#Top 11 players in each position
st.title(" **4. Your Dream Team - Top 11 Players in Each Position** ")
# Changing the position column in the csv file - only keeping the last three characters of the position
df['Position'] = df['Position'].str[-3:]
#removing the > from the position column if it exists
df['Position'] = df['Position'].str.replace('>', '')
#Removing nan values from the value column
df = df[df['Position'].notna()]
#Select a position
position = st.selectbox('Select a position', df['Position'].unique())
#Filtering the data based on the position selected
df_position = df[df['Position'] == position]
#Sorting the data based on the overall column
df_position = df_position.sort_values(by=['Overall'], ascending=False).head(11)
imagelist_3 = []
for i in df_position['Photo']:
    # Displaying all the images in the same row
    imagelist_3 = imagelist_3 + [i]
st.image(imagelist_3, width=100)
# Bar chart of the top 10 players based on the overall column
fig_3 = px.bar(df_position, x='Name', y='Overall', color='Club', title='Top 11 Players in ' + position)
st.plotly_chart(fig_3)









#Top 11 players in each club
st.title(" **5. Your Dream Team - Top 11 Players in Each Club** ")
#Select a club
club = st.selectbox('Select a club', df['Club'].unique())
#Filtering the data based on the club selected
df_club = df[df['Club'] == club]
#Displaying the selected club logo
#Getting the club logo
club_logo = df_club['Club Logo'].iloc[0]
#Displaying the club logo
st.image(club_logo, width=50)
#Sorting the data based on the overall column
df_club = df_club.sort_values(by=['Overall'], ascending=False).head(11)
imagelist_4 = []
for i in df_club['Photo']:
    # Displaying all the images in the same row
    imagelist_4 = imagelist_4 + [i] 
st.image(imagelist_4, width=100)
# Bar chart of the top 10 players based on the overall column
fig_4 = px.bar(df_club, x='Name', y='Overall', color='Club', title='Top 11 Players in ' + club)
st.plotly_chart(fig_4)





# Top 11 players based on International Reputation
st.title(" **6. Your Dream Team - Top 11 Players Based on International Reputation** ")
#Removing nan values from the value column
df = df[df['International Reputation'].notna()]
top_10_international_reputation = df.sort_values(by=['International Reputation'], ascending=False).head(11)
imagelist_5 = []
for i in top_10_international_reputation['Photo']:
    # Displaying all the images in the same row
    imagelist_5 = imagelist_5 + [i]
st.image(imagelist_5, width=100)
# Bar chart of the top 10 players based on the overall column
fig_5 = px.bar(top_10_international_reputation, x='Name', y='International Reputation', color='Club', title='Top 11 Players Based on International Reputation')
st.plotly_chart(fig_5)





# Top 11 players based on Wage
st.title(" **7. Your Dream Team - Top 11 Players Based on Wage** ")
#Removing nan values from the value column
df = df[df['Wage'].notna()]
#Removing the € sign from the wage column
df['Wage'] = df['Wage'].str.replace('K', '')
df['Wage'] = df['Wage'].str.replace('€', '')
df['Wage'] = df['Wage'].astype(float)
top_10_wage = df.sort_values(by=['Wage'], ascending=False).head(11)
imagelist_6 = []
for i in top_10_wage['Photo']:
    # Displaying all the images in the same row
    imagelist_6 = imagelist_6 + [i]
st.image(imagelist_6, width=100)
# Bar chart of the top 10 players based on the overall column
fig_6 = px.bar(top_10_wage, x='Name', y='Wage', color='Club', title='Top 11 Players Based on Wage')
fig_6.update_yaxes(ticksuffix="K")
st.plotly_chart(fig_6)





# Top 11 Affordable Players but with high Overall
st.title(" **8. Your Dream Team - Top 11 Affordable Players but with high Overall** ")
#Removing nan values from the value column
df = df[df['Value'].notna()]
#Removing the € sign from the value column
df['Value'] = df['Value'].str.replace('M', '')
df['Value'] = df['Value'].str.replace('K', '')
df['Value'] = df['Value'].str.replace('€', '')
df['Value'] = df['Value'].astype(float)
#Removing nan values from the overall column
df = df[df['Overall'].notna()]
#Sorting the data based on value mean and overall mean
top_10_value_overall = df.sort_values(by=['Value', 'Overall'], ascending=False).head(11)
imagelist_7 = []
for i in top_10_value_overall['Photo']:
    # Displaying all the images in the same row
    imagelist_7 = imagelist_7 + [i]
st.image(imagelist_7, width=100)
# Bar chart of the top 10 players based on the overall column
fig_7 = px.bar(top_10_value_overall, x='Name', y='Value', color='Club', title='Top 11 Affordable Players but with high Overall')
# Displaying their overall in the hover data
fig_7.update_traces(hovertemplate='Name: %{x}<br>Value: %{y}M<br>Overall: %{customdata[0]}<extra></extra>', customdata=top_10_value_overall[['Overall']])
fig_7.update_yaxes(ticksuffix="K")
st.plotly_chart(fig_7)







