from itertools import count
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from Homepage import footer
#ignore warnings
import warnings
warnings.filterwarnings('ignore')

st.markdown(footer, unsafe_allow_html=True)




# Importing the data from the csv file FIFA23_official_data.csv
df = pd.read_csv("D:/EPITA/data-reporting-visualisation/Final_Project/Data/FIFA23_official_data.csv")

st.header("FIFA 23 Players Information")

# Input box to select what kind of top players you want to see
st.subheader("Select the category of top players you want to see")
top_players = st.selectbox("Top Players", ('Overall', 'Potential', 'Value', 'Wage', 'International Reputation', 'Skill Moves', 'Height', 'Weight','Age'))

# Input box to select the number of top players you want to see
st.subheader("Select the number of top players you want to see")
top_players_number = st.slider("Top Players Number", 1, 100, 10)

# IF user selects Overall, Potential, Value, Wage, International Reputation, Weak Foot, Skill Moves, Height, Weight, Release Clause
# THEN display the top players in the selected category
if top_players == 'Overall':
    st.subheader("Top Players by Overall")
    # Getting the Top players in the csv file using the overall column

    #Removing nan values from the overall column
    df = df[df['Overall'].notna()]
    df = df.sort_values(by=['Overall'], ascending=False)
    top_10_overall = df.head(top_players_number)
    # Chart for the Top players in the world
    fig = px.bar(top_10_overall, x='Name', y='Overall', color='Name', title='Top Players in the World based on Overall information') 
    # Adjusting the range of the y-axis 80-100 increasing by 1
    fig.update_yaxes(range=[80, 100], tick0=80, dtick=1)
    st.plotly_chart(fig)
    with st.expander('See Explanation:'):
        st.markdown('This chart shows the Top players in the world based on their overall rating. The overall rating is calculated based on the player’s attributes such as pace, shooting, passing, dribbling, defending, physicality, etc. The overall rating is calculated for each player and the Top players are displayed in the chart.')

elif top_players == 'Potential':
    st.subheader("Top Players by Potential")
    #Removing nan values from the potential column
    df = df[df['Potential'].notna()]
    # Getting the Top players in the csv file using the potential column
    df = df.sort_values(by=['Potential'], ascending=False)
    top_10_potential = df.head(top_players_number)
    # Chart for the Top players in the world
    fig = px.bar(top_10_potential, x='Name', y='Potential', color='Name', title='Top Players in the World based on Potential information') 
    # Adjusting the range of the y-axis 80-100 increasing by 1
    fig.update_yaxes(range=[80, 100], tick0=80, dtick=1)
    st.plotly_chart(fig)
    with st.expander('See Explanation:'):
        st.markdown('This chart shows the Top players in the world based on their potential rating. The potential rating is calculated based on the player’s attributes such as pace, shooting, passing, dribbling, defending, physicality, etc. The potential rating is calculated for each player and the Top players are displayed in the chart.')

elif top_players == 'Value':
    #Removing nan values from the value column
    df = df[df['Value'].notna()]
    df_value = df[df['Value'].str.contains('M')]
    # Getting the Top players in the csv file using the value column
    # Removing M and euro from the value column
    df_value['Value'] = df_value['Value'].str.replace('M', '')
    df_value['Value'] = df_value['Value'].str.replace('€', '')
    df_value['Value'] = df_value['Value'].astype(float)
    df_value = df_value.sort_values(by=['Value'], ascending=False)
    top_10_value = df_value.head(top_players_number)
    # Chart for the Top players in the world
    fig = px.bar(top_10_value, x='Name', y='Value', color='Name', title='Top Players in the World based on Value information')
    # Rename the x-axis to Value in millions of euros
    fig.update_yaxes(title_text='Value in millions of euros')
    st.plotly_chart(fig)
    with st.expander('See Explanation:'):
        st.markdown('This chart shows the Top players in the world based on their value. The value is calculated based on the player’s attributes such as pace, shooting, passing, dribbling, defending, physicality, etc. The value is calculated for each player and the Top players are displayed in the chart.')

elif top_players == 'Wage':
    #Removing nan values from the wage column
    df = df[df['Wage'].notna()]
    df_wage = df[df['Wage'].str.contains('K')]
    # Getting the Top players in the csv file using the wage column
    # Removing K and euro from the wage column
    df_wage['Wage'] = df_wage['Wage'].str.replace('K', '')
    df_wage['Wage'] = df_wage['Wage'].str.replace('€', '')
    df_wage['Wage'] = df_wage['Wage'].astype(float)
    df_wage = df_wage.sort_values(by=['Wage'], ascending=False)
    top_10_wage = df_wage.head(top_players_number)
    # Chart for the Top players in the world
    fig = px.bar(top_10_wage, x='Name', y='Wage', color='Name', title='Top Players in the World based on Wage information')
    # Rename the x-axis to Wage in thousands of euros
    fig.update_yaxes(title_text='Wage in thousands of euros')
    st.plotly_chart(fig)
    with st.expander('See Explanation:'):
        st.markdown('This chart shows the Top players in the world based on their wage. The wage is calculated based on the player’s attributes such as pace, shooting, passing, dribbling, defending, physicality, etc. The wage is calculated for each player and the Top players are displayed in the chart.')

elif top_players == 'International Reputation':
    #Removing nan values from the international reputation column
    df = df[df['International Reputation'].notna()]
    # Getting the Top players in the csv file using the international reputation column
    df = df.sort_values(by=['International Reputation'], ascending=False)
    top_10_international_reputation = df.head(top_players_number)
    # Chart for the Top players in the world
    fig = px.bar(top_10_international_reputation, x='Name', y='International Reputation', color='Name', title='Top Players in the World based on International Reputation information')
    # Rename the x-axis to International Reputation
    fig.update_yaxes(title_text='International Reputation')
    st.plotly_chart(fig)
    with st.expander('See Explanation:'):
        st.markdown('This chart shows the Top players in the world based on their international reputation. The international reputation is calculated based on the player’s attributes such as pace, shooting, passing, dribbling, defending, physicality, etc. The international reputation is calculated for each player and the Top players are displayed in the chart.')

elif top_players == 'Skill Moves':
    #Removing nan values from the skill moves column
    df = df[df['Skill Moves'].notna()]

    # Getting the Top players in the csv file using the skill moves column
    df = df.sort_values(by=['Skill Moves'], ascending=False)
    top_10_skill_moves = df.head(top_players_number)
    # Chart for the Top players in the world
    fig = px.bar(top_10_skill_moves, x='Name', y='Skill Moves', color='Name', title='Top Players in the World based on Skill Moves information')
    # Rename the x-axis to Skill Moves
    fig.update_yaxes(title_text='Skill Moves')
    st.plotly_chart(fig)
    with st.expander('See Explanation:'):
        st.markdown('This chart shows the Top players in the world based on their skill moves. The skill moves is calculated based on the player’s attributes such as pace, shooting, passing, dribbling, defending, physicality, etc. The skill moves is calculated for each player and the Top players are displayed in the chart.')

elif top_players == 'Height':
    #Removing nan values from the height column
    df = df[df['Height'].notna()]

    # Getting the Top players in the csv file using the height column
    df = df.sort_values(by=['Height'], ascending=False)
    top_10_height = df.head(top_players_number)
    
    fig = px.scatter(top_10_height, x='Name', y='Height', color='Name', title='Top Players in the World based on Height information')

    st.plotly_chart(fig)

    with st.expander('See Explanation:'):
        st.markdown('This chart shows the Top players in the world based on their height. The height is calculated based on the player’s attributes such as pace, shooting, passing, dribbling, defending, physicality, etc. The height is calculated for each player and the Top players are displayed in the chart.')

elif top_players == 'Weight':
    #Removing nan values from the weight column
    df = df[df['Weight'].notna()]

    # Getting the Top players in the csv file using the weight column
    df = df.sort_values(by=['Weight'], ascending=False)
    top_10_weight = df.head(top_players_number)
    # Tree map for the Top players in the world
    fig =px.scatter(top_10_weight, x='Name', y='Weight', color='Name', title='Top Players in the World based on Weight information')
    # #Rename the x-axis to Weight
    fig.update_yaxes(title_text='Weight')
    
    st.plotly_chart(fig)
    with st.expander('See Explanation:'):
        st.markdown('This chart shows the Top players in the world based on their weight. The weight is calculated based on the player’s attributes such as pace, shooting, passing, dribbling, defending, physicality, etc. The weight is calculated for each player and the Top players are displayed in the chart.')

elif top_players == 'Age':
    #Removing nan values from the age column
    df = df[df['Age'].notna()]

    # Getting the Top players in the csv file using the age column
    df = df.sort_values(by=['Age'], ascending=False)
    top_10_age = df.head(top_players_number)
    # Chart for the Top players in the world
    fig = px.bar(top_10_age, x='Name', y='Age', color='Name', title='Top Players in the World based on Age information')
    # Rename the x-axis to Age
    fig.update_yaxes(title_text='Age')

    st.plotly_chart(fig)
    with st.expander('See Explanation:'):
        st.markdown('This chart shows the Top players in the world based on their age. The age is calculated based on the player’s attributes such as pace, shooting, passing, dribbling, defending, physicality, etc. The age is calculated for each player and the Top players are displayed in the chart.')

st.header('Other Interesting Charts')

#World cloud based on Number of Players in each country
st.subheader('Number of Players in each country')
#Getting the number of players in each country
country_count = df['Nationality'].value_counts()
#World cloud based on Number of Players in each country
st.subheader('World Cloud based on Number of Players in each country')

#Instantiate a word cloud object
wc = WordCloud(background_color='white', max_words=1000, contour_width=3, contour_color='steelblue')

#Generate the word cloud
wc.generate_from_frequencies(country_count)

#Display the word cloud
fig, ax = plt.subplots()

plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()
st.pyplot(fig)

with st.expander('See Explanation:'):
    st.markdown('This chart shows the number of players in each country. The number of players is calculated based on the player’s attributes such as pace, shooting, passing, dribbling, defending, physicality, etc. The number of players is calculated for each player and the number of players in each country is displayed in the chart.')

df_age = df.sort_values(by=['Age'], ascending=False)
top_10_age = df_age.head(10)

# Radar chart for the Top players in the world based on thier Age
fig = px.line_polar(top_10_age, r='Age', theta='Name', line_close=True, title='Top Players in the World based on Age information')
#Increasing the size of the chart
fig.update_layout(
    autosize=False,
    width=750,
    height=750,
)

st.plotly_chart(fig)

with st.expander('See Explanation:'):
    st.markdown('This chart shows the Top players in the world based on their age. The age is calculated based on the player’s attributes such as pace, shooting, passing, dribbling, defending, physicality, etc. The age is calculated for each player and the Top players are displayed in the chart.')

# Age distribution of the players with histogram
fig = px.histogram(df, x='Age', title='Age distribution of the players')
# Increasing the size of the chart
fig.update_layout(
    autosize=False,
    width=750,
    height=750,
)

# Rename the x-axis to Age
fig.update_xaxes(title_text='Age')
st.plotly_chart(fig)
with st.expander('See Explanation:'):
    st.markdown('This chart shows the age distribution of the players. The age is calculated based on the player’s attributes such as pace, shooting, passing, dribbling, defending, physicality, etc. The age is calculated for each player and the age distribution is displayed in the chart.')

# top_10_height
df_height = df.sort_values(by=['Height'], ascending=False)
top_10_height = df_height.head(10)
#top_10_weight
df_weight = df.sort_values(by=['Weight'], ascending=False)
top_10_weight = df_weight.head(10)


# SUnburst plot for Top Players name and thier ranking with Height
fig = px.sunburst(top_10_height, path=['Height','Name'], labels='Height', title='Top Players in the World based on Height and Weight information', color='Overall')
# Increasing the size of the chart
fig.update_layout(
    autosize=False,
    width=750,
    height=750,
)

st.plotly_chart(fig)
with st.expander('See Explanation:'):
    st.markdown('This chart shows the Top players in the world based on their height. The height is calculated based on the player’s attributes such as pace, shooting, passing, dribbling, defending, physicality, etc. The height is calculated for each player and the Top players are displayed in the chart.')

# SUnburst plot for Top Players name and thier ranking with Weight
fig = px.sunburst(top_10_weight, path=['Weight','Name'], labels='Weight', title='Top Players in the World based on Weight information', color='Overall')
# Increasing the size of the chart
fig.update_layout(
    autosize=False,
    width=750,
    height=750,
)

st.plotly_chart(fig)
with st.expander('See Explanation:'):
    st.markdown('This chart shows the Top players in the world based on their weight. The weight is calculated based on the player’s attributes such as pace, shooting, passing, dribbling, defending, physicality, etc. The weight is calculated for each player and the Top players are displayed in the chart.')


























