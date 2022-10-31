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

df = pd.read_csv("D:/EPITA/data-reporting-visualisation/Final_Project/Data/german bundesliga data.csv")

st.title("Bundesliga Stastistics")

selection = st.selectbox("Select the  Category",("Best Matches","Match Possession %","Pass Success %","Total Shots","Shots on Target","Shots off Target","Blocked Shots","Corners","Throw-Ins","Aerials Won","Clearances","Fouls"))

selection_number = st.slider("Select the range for visualisation", 1, 100, 10)

if selection == "Best Matches":

    df = df.sort_values(by=['Match Excitement'], ascending=False)
    df = df.head(selection_number)
    # Displaying Home Team, Away Team, Match Excitement and Score
    #st.write(df[['Home Team', 'Away Team', 'Match Excitement', 'Score']])
    # Bubble Chart for Match Excitement
    fig = px.scatter(df, x="Home Team", y="Away Team", color="Match Excitement", hover_name="Score", size = "Match Excitement")
    st.plotly_chart(fig)
    with st.expander('See Explanation'):
        st.markdown("This chart shows the best matches in respect with the number of matches chosen. The Match Excitement is calculated based on the number of goals, shots on target, shots off target, blocked shots, corners, throw-ins, aerials won, clearances, fouls, yellow cards, red cards, goals scored and goals conceded. The Match Excitement is calculated for each match and the best matches are displayed in the chart.")

elif selection == "Match Possession %":

    year = st.slider("Select the  Year", 2014, 2020, 2016)
    #Home Team Possession

    st.subheader("Home Team Possession")
    #Teams with the highest Home possession percentage based on the year selected and display the away team on that match
    df = df[df['year'] == year]
    df_h = df.sort_values(by=['Home Team Possession %'], ascending=False)
    df_h = df_h.head(selection_number)
    df_h = df_h[['Home Team', 'Home Team Possession %', 'Away Team']]
    
    # Chart for Home Team Possession
    #fig = px.bar(df, x="Home Team", y="Home Team Possession %", color="Away Team", barmode="group")
    #Scatter Plot for Home Team Possession
    fig = px.scatter(df_h, x="Home Team", y="Home Team Possession %", color="Away Team",size = "Home Team Possession %")

    # Increase the plot size
    fig.update_layout(
        autosize=False,
        width=750,
        height=500,
    )
    st.plotly_chart(fig)
    # Away Team Possession
    st.subheader("Away Team Possession")
    #Teams with the highest Away possession percentage based on the year selected and display the home team on that match
    df_a = df.sort_values(by=['Away Team Possession %'], ascending=False)
    df_a = df_a.head(selection_number)
    df_a = df_a[['Away Team', 'Away Team Possession %', 'Home Team']]
    # Chart for Away Team Possession
    #fig = px.bar(df, x="Away Team", y="Away Team Possession %", color="Home Team", barmode="group")
    #Scatter Plot for Away Team Possession
    fig = px.scatter(df_a, x="Away Team", y="Away Team Possession %", color="Home Team",size = "Away Team Possession %")
    # Increase the plot size
    fig.update_layout(
        autosize=False,
        width=750,
        height=500,
    )
    st.plotly_chart(fig)
    with st.expander('See Explanation'):
        st.markdown("This chart shows the teams with the highest possession percentage based on the year selected. The home team and away team are displayed in the chart.")

elif selection == "Pass Success %":
        
    year = st.slider("Select the  Year", 2014, 2020, 2016)
    #Home Team Pass Success
    st.subheader("Home Team Pass Success")
    #Teams with the highest Home pass success percentage based on the year selected and display the away team on that match
    df = df[df['year'] == year]
    df_h = df.sort_values(by=['Home Team Pass Success %'], ascending=False)
    df_h = df_h.head(selection_number)
    df_h = df_h[['Home Team', 'Home Team Pass Success %', 'Away Team']]
    # Chart for Home Team Pass Success
    #fig = px.bar(df, x="Home Team", y="Home Team Pass Success %", color="Away Team", barmode="group")
    #Scatter Plot for Home Team Pass Success
    fig = px.scatter(df_h, x="Home Team", y="Home Team Pass Success %", color="Away Team",size = "Home Team Pass Success %")
    # Increase the plot size
    fig.update_layout(
        autosize=False,
        width=750,
        height=500,
    )
    st.plotly_chart(fig)
    # Away Team Pass Success
    st.subheader("Away Team Pass Success")
    #Teams with the highest Away pass success percentage based on the year selected and display the home team on that match
    df_a = df.sort_values(by=['Away Team Pass Success %'], ascending=False)
    df_a = df_a.head(selection_number)
    df_a = df_a[['Away Team', 'Away Team Pass Success %', 'Home Team']]
    # Chart for Away Team Pass Success
    #fig = px.bar(df, x="Away Team", y="Away Team Pass Success %", color="Home Team", barmode="group")
    #Scatter Plot for Away Team Pass Success
    fig = px.scatter(df_a, x="Away Team", y="Away Team Pass Success %", color="Home Team",size = "Away Team Pass Success %")
    # Increase the plot size
    fig.update_layout(
        autosize=False,
        width=750,
        height=500,
    )
    st.plotly_chart(fig)
    with st.expander('See Explanation'):
        st.markdown("This chart shows the teams with the highest pass success percentage based on the year selected. The home team and away team are displayed in the chart.")

elif selection == "Total Shots":
            
    year = st.slider("Select the  Year", 2014, 2020, 2016)
    #Home Team Total Shots
    st.subheader("Home Team Total Shots")
    #Teams with the highest Home total shots based on the year selected and display the away team on that match
    df = df[df['year'] == year]
    df_h = df.sort_values(by=['Home Team Total Shots'], ascending=False)
    df_h = df_h.head(selection_number)
    df_h = df_h[['Home Team', 'Home Team Total Shots', 'Away Team']]
    # Chart for Home Team Total Shots
    #fig = px.bar(df, x="Home Team", y="Home Team Total Shots", color="Away Team", barmode="group")
    #Scatter Plot for Home Team Total Shots
    fig = px.scatter(df_h, x="Home Team", y="Home Team Total Shots", color="Away Team",size = "Home Team Total Shots")
    # Increase the plot size
    fig.update_layout(
        autosize=False,
        width=750,
        height=500,
    )
    st.plotly_chart(fig)
    # Away Team Total Shots
    st.subheader("Away Team Total Shots")
    #Teams with the highest Away total shots based on the year selected and display the home team on that match
    df_a = df.sort_values(by=['Away Team Total Shots'], ascending=False)
    df_a = df_a.head(selection_number)
    df_a = df_a[['Away Team', 'Away Team Total Shots', 'Home Team']]
    # Chart for Away Team Total Shots
    #fig = px.bar(df, x="Away Team", y="Away Team Total Shots", color="Home Team", barmode="group")
    #Scatter Plot for Away Team Total Shots
    fig = px.scatter(df_a, x="Away Team", y="Away Team Total Shots", color="Home Team",size = "Away Team Total Shots")
    # Increase the plot size
    fig.update_layout(
        autosize=False,
        width=750,
        height=500,
    )
    st.plotly_chart(fig)
    with st.expander('See Explanation'):
        st.markdown("This chart shows the teams with the highest total shots based on the year selected. The home team and away team are displayed in the chart.")

elif selection == "Shots on Target":
                
    year = st.slider("Select the  Year", 2014, 2020, 2016)
    #Home Team Total Shots on Target
    st.subheader("Home Team Total Shots on Target")
    #Teams with the highest Home total shots on target based on the year selected and display the away team on that match
    df = df[df['year'] == year]
    df_h = df.sort_values(by=['Home Team On Target Shots'], ascending=False)
    df_h = df_h.head(selection_number)
    df_h = df_h[['Home Team', 'Home Team On Target Shots', 'Away Team']]
    # Chart for Home Team Total Shots on Target
    #fig = px.bar(df, x="Home Team", y="Home Team Shots on Target", color="Away Team", barmode="group")
    #Scatter Plot for Home Team Total Shots on Target
    fig = px.scatter(df_h, x="Home Team", y="Home Team On Target Shots", color="Away Team",size = "Home Team On Target Shots")
    # Increase the plot size
    fig.update_layout(
        autosize=False,
        width=750,
        height=500,
    )
    st.plotly_chart(fig)
    # Away Team Total Shots on Target
    st.subheader("Away Team Total Shots on Target")
    #Teams with the highest Away total shots on target based on the year selected and display the home team on that match
    df_a = df.sort_values(by=['Away Team On Target Shots'], ascending=False)
    df_a = df_a.head(selection_number)
    df_a = df_a[['Away Team', 'Away Team On Target Shots', 'Home Team']]
    # Chart for Away Team Total Shots on Target
    #fig = px.bar(df, x="Away Team", y="Away Team Shots on Target", color="Home Team", barmode="group")
    #Scatter Plot for Away Team Total Shots on Target
    fig = px.scatter(df_a, x="Away Team", y="Away Team On Target Shots", color="Home Team",size = "Away Team On Target Shots")
    # Increase the plot size
    fig.update_layout(
        autosize=False,
        width=750,
        height=500,
    )
    st.plotly_chart(fig)
    with st.expander('See Explanation'):
        st.markdown("This chart shows the teams with the highest total shots on target based on the year selected. The home team and away team are displayed in the chart.")

elif selection == "Shots off Target":
                    
    year = st.slider("Select the  Year", 2014, 2020, 2016)
    #Home Team Total Shots off Target
    st.subheader("Home Team Total Shots off Target")
    #Teams with the highest Home total shots off target based on the year selected and display the away team on that match
    df = df[df['year'] == year]
    df_h = df.sort_values(by=['Home Team Off Target Shots'], ascending=False)
    df_h = df_h.head(selection_number)
    df_h = df_h[['Home Team', 'Home Team Off Target Shots', 'Away Team']]
    # Chart for Home Team Total Shots off Target
    #fig = px.bar(df, x="Home Team", y="Home Team Shots off Target", color="Away Team", barmode="group")
    #Scatter Plot for Home Team Total Shots off Target
    fig = px.scatter(df_h, x="Home Team", y="Home Team Off Target Shots", color="Away Team",size = "Home Team Off Target Shots")
    # Increase the plot size
    fig.update_layout(
        autosize=False,
        width=750,
        height=500,
    )
    st.plotly_chart(fig)
    # Away Team Total Shots off Target
    st.subheader("Away Team Total Shots off Target")
    #Teams with the highest Away total shots off target based on the year selected and display the home team on that match
    df_a = df.sort_values(by=['Away Team Off Target Shots'], ascending=False)
    df_a = df_a.head(selection_number)
    df_a = df_a[['Away Team', 'Away Team Off Target Shots', 'Home Team']]
    # Chart for Away Team Total Shots off Target
    #fig = px.bar(df, x="Away Team", y="Away Team Shots off Target", color="Home Team", barmode="group")
    #Scatter Plot for Away Team Total Shots off Target
    fig = px.scatter(df_a, x="Away Team", y="Away Team Off Target Shots", color="Home Team",size = "Away Team Off Target Shots")
    # Increase the plot size
    fig.update_layout(
        autosize=False,
        width=750,
        height=500,
    )
    st.plotly_chart(fig)
    with st.expander('See Explanation'):
        st.markdown("This chart shows the teams with the highest total shots off target based on the year selected. The home team and away team are displayed in the chart.")

elif selection == "Blocked Shots":
                            
    year = st.slider("Select the  Year", 2014, 2020, 2016)
    #Home Team Total Blocked Shots
    st.subheader("Home Team Total Blocked Shots")
    #Teams with the highest Home total blocked shots based on the year selected and display the away team on that match
    df = df[df['year'] == year]
    df_h = df.sort_values(by=['Home Team Blocked Shots'], ascending=False)
    df_h = df_h.head(selection_number)
    df_h = df_h[['Home Team', 'Home Team Blocked Shots', 'Away Team']]
    # Chart for Home Team Total Blocked Shots
    #fig = px.bar(df, x="Home Team", y="Home Team Blocked Shots", color="Away Team", barmode="group")
    #Scatter Plot for Home Team Total Blocked Shots
    fig = px.scatter(df_h, x="Home Team", y="Home Team Blocked Shots", color="Away Team",size = "Home Team Blocked Shots")
    # Increase the plot size
    fig.update_layout(
        autosize=False,
        width=750,
        height=500,
    )
    st.plotly_chart(fig)
    # Away Team Total Blocked Shots
    st.subheader("Away Team Total Blocked Shots")
    #Teams with the highest Away total blocked shots based on the year selected and display the home team on that match
    df_a = df.sort_values(by=['Away Team Blocked Shots'], ascending=False)
    df_a = df_a.head(selection_number)
    df_a = df_a[['Away Team', 'Away Team Blocked Shots', 'Home Team']]
    # Chart for Away Team Total Blocked Shots
    #fig = px.bar(df, x="Away Team", y="Away Team Blocked Shots", color="Home Team", barmode="group")
    #Scatter Plot for Away Team Total Blocked Shots
    fig = px.scatter(df_a, x="Away Team", y="Away Team Blocked Shots", color="Home Team",size = "Away Team Blocked Shots")
    # Increase the plot size
    fig.update_layout(
        autosize=False,
        width=750,
        height=500,
    )
    st.plotly_chart(fig)
    with st.expander('See Explanation'):
        st.markdown("This chart shows the teams with the highest total blocked shots based on the year selected. The home team and away team are displayed in the chart.")

elif selection == "Fouls":
                                        
    year = st.slider("Select the  Year", 2014, 2020, 2016)
    #Home Team Total Fouls
    st.subheader("Home Team Total Fouls")
    #Teams with the highest Home total fouls based on the year selected and display the away team on that match
    df = df[df['year'] == year]
    df_h = df.sort_values(by=['Home Team Fouls'], ascending=False)
    df_h = df_h.head(selection_number)
    df_h = df_h[['Home Team', 'Home Team Fouls', 'Away Team']]
    # Chart for Home Team Total Fouls
    #fig = px.bar(df, x="Home Team", y="Home Team Fouls", color="Away Team", barmode="group")
    #Scatter Plot for Home Team Total Fouls
    fig = px.scatter(df_h, x="Home Team", y="Home Team Fouls", color="Away Team",size = "Home Team Fouls")
    # Increase the plot size
    fig.update_layout(
        autosize=False,
        width=750,
        height=500,
    )
    st.plotly_chart(fig)
    # Away Team Total Fouls
    st.subheader("Away Team Total Fouls")
    #Teams with the highest Away total fouls based on the year selected and display the home team on that match
    df_a = df.sort_values(by=['Away Team Fouls'], ascending=False)
    df_a = df_a.head(selection_number)
    df_a = df_a[['Away Team', 'Away Team Fouls', 'Home Team']]
    # Chart for Away Team Total Fouls
    #fig = px.bar(df, x="Away Team", y="Away Team Fouls", color="Home Team", barmode="group")
    #Scatter Plot for Away Team Total Fouls
    fig = px.scatter(df_a, x="Away Team", y="Away Team Fouls", color="Home Team",size = "Away Team Fouls")
    # Increase the plot size
    fig.update_layout(
        autosize=False,
        width=750,
        height=500,
    )
    st.plotly_chart(fig)
    with st.expander('See Explanation'):
        st.markdown("This chart shows the teams with the highest total fouls based on the year selected. The home team and away team are displayed in the chart.")

elif selection == "Corners":
                                                    
    year = st.slider("Select the  Year", 2014, 2020, 2016)
    #Home Team Total Corners
    st.subheader("Home Team Total Corners")
    #Teams with the highest Home total corners based on the year selected and display the away team on that match
    df = df[df['year'] == year]
    df_h = df.sort_values(by=['Home Team Corners'], ascending=False)
    df_h = df_h.head(selection_number)
    df_h = df_h[['Home Team', 'Home Team Corners', 'Away Team']]
    # Chart for Home Team Total Corners
    #fig = px.bar(df, x="Home Team", y="Home Team Corners", color="Away Team", barmode="group")
    #Scatter Plot for Home Team Total Corners
    fig = px.scatter(df_h, x="Home Team", y="Home Team Corners", color="Away Team",size = "Home Team Corners")
    # Increase the plot size
    fig.update_layout(
        autosize=False,
        width=750,
        height=500,
    )
    st.plotly_chart(fig)
    # Away Team Total Corners
    st.subheader("Away Team Total Corners")
    #Teams with the highest Away total corners based on the year selected and display the home team on that match
    df_a = df.sort_values(by=['Away Team Corners'], ascending=False)
    df_a = df_a.head(selection_number)
    df_a = df_a[['Away Team', 'Away Team Corners', 'Home Team']]
    # Chart for Away Team Total Corners
    #fig = px.bar(df, x="Away Team", y="Away Team Corners", color="Home Team", barmode="group")
    #Scatter Plot for Away Team Total Corners
    fig = px.scatter(df_a, x="Away Team", y="Away Team Corners", color="Home Team",size = "Away Team Corners")
    # Increase the plot size
    fig.update_layout(
        autosize=False,
        width=750,
        height=500,
    )
    st.plotly_chart(fig)
    with st.expander('See Explanation'):
        st.markdown("This chart shows the teams with the highest total corners based on the year selected. The home team and away team are displayed in the chart.")

elif selection == "Offsides":
                                                            
    year = st.slider("Select the  Year", 2014, 2020, 2016)
    #Home Team Total Offsides
    st.subheader("Home Team Total Offsides")
    #Teams with the highest Home total offsides based on the year selected and display the away team on that match
    df = df[df['year'] == year]
    df_h = df.sort_values(by=['Home Team Offsides'], ascending=False)
    df_h = df_h.head(selection_number)
    df_h = df_h[['Home Team', 'Home Team Offsides', 'Away Team']]
    # Chart for Home Team Total Offsides
    #fig = px.bar(df, x="Home Team", y="Home Team Offsides", color="Away Team", barmode="group")
    #Scatter Plot for Home Team Total Offsides
    fig = px.scatter(df_h, x="Home Team", y="Home Team Offsides", color="Away Team",size = "Home Team Offsides")
    # Increase the plot size
    fig.update_layout(
        autosize=False,
        width=750,
        height=500,
    )
    st.plotly_chart(fig)
    # Away Team Total Offsides
    st.subheader("Away Team Total Offsides")
    #Teams with the highest Away total offsides based on the year selected and display the home team on that match
    df_a = df.sort_values(by=['Away Team Offsides'], ascending=False)
    df_a = df_a.head(selection_number)
    df_a = df_a[['Away Team', 'Away Team Offsides', 'Home Team']]
    # Chart for Away Team Total Offsides
    #fig = px.bar(df, x="Away Team", y="Away Team Offsides", color="Home Team", barmode="group")
    #Scatter Plot for Away Team Total Offsides
    fig = px.scatter(df_a, x="Away Team", y="Away Team Offsides", color="Home Team",size = "Away Team Offsides")
    # Increase the plot size
    fig.update_layout(
        autosize=False,
        width=750,
        height=500,
    )
    st.plotly_chart(fig)
    with st.expander('See Explanation'):
        st.markdown("This chart shows the teams with the highest total offsides based on the year selected. The home team and away team are displayed in the chart.")

elif selection == "Throw-Ins":

    year = st.slider("Select the  Year", 2014, 2020, 2016)
    #Home Team Total Throw-Ins
    st.subheader("Home Team Total Throw-Ins")
    #Teams with the highest Home total throw-ins based on the year selected and display the away team on that match
    df = df[df['year'] == year]
    df_h = df.sort_values(by=['Home Team Throw Ins'], ascending=False)
    df_h = df_h.head(selection_number)
    df_h = df_h[['Home Team', 'Home Team Throw Ins', 'Away Team']]
    # Chart for Home Team Total Throw-Ins
    #fig = px.bar(df, x="Home Team", y="Home Team Throw-Ins", color="Away Team", barmode="group")
    #Scatter Plot for Home Team Total Throw-Ins
    fig = px.scatter(df_h, x="Home Team", y="Home Team Throw Ins", color="Away Team",size = "Home Team Throw Ins")
    # Increase the plot size
    fig.update_layout(
        autosize=False,
        width=750,
        height=500,
    )
    st.plotly_chart(fig)
    # Away Team Total Throw-Ins
    st.subheader("Away Team Total Throw-Ins")
    #Teams with the highest Away total throw-ins based on the year selected and display the home team on that match
    df_a = df.sort_values(by=['Away Team Throw Ins'], ascending=False)
    df_a = df_a.head(selection_number)
    df_a = df_a[['Away Team', 'Away Team Throw Ins', 'Home Team']]
    # Chart for Away Team Total Throw-Ins
    #fig = px.bar(df, x="Away Team", y="Away Team Throw-Ins", color="Home Team", barmode="group")
    #Scatter Plot for Away Team Total Throw-Ins
    fig = px.scatter(df_a, x="Away Team", y="Away Team Throw Ins", color="Home Team",size = "Away Team Throw Ins")
    # Increase the plot size
    fig.update_layout(
        autosize=False,
        width=750,
        height=500,
    )
    st.plotly_chart(fig)
    with st.expander('See Explanation'):
        st.markdown("This chart shows the teams with the highest total throw-ins based on the year selected. The home team and away team are displayed in the chart.")

elif selection == "Aerials Won":
    
    year = st.slider("Select the  Year", 2014, 2020, 2016)
    #Home Team Total Aerials Won
    st.subheader("Home Team Total Aerials Won")
    #Teams with the highest Home total aerials won based on the year selected and display the away team on that match
    df = df[df['year'] == year]
    df_h = df.sort_values(by=['Home Team Aerials Won'], ascending=False)
    df_h = df_h.head(selection_number)
    df_h = df_h[['Home Team', 'Home Team Aerials Won', 'Away Team']]
    # Chart for Home Team Total Aerials Won
    #fig = px.bar(df, x="Home Team", y="Home Team Aerials Won", color="Away Team", barmode="group")
    #Scatter Plot for Home Team Total Aerials Won
    fig = px.scatter(df_h, x="Home Team", y="Home Team Aerials Won", color="Away Team",size = "Home Team Aerials Won")
    # Increase the plot size
    fig.update_layout(
        autosize=False,
        width=750,
        height=500,
    )
    st.plotly_chart(fig)
    # Away Team Total Aerials Won
    st.subheader("Away Team Total Aerials Won")
    #Teams with the highest Away total aerials won based on the year selected and display the home team on that match
    df_a = df.sort_values(by=['Away Team Aerials Won'], ascending=False)
    df_a = df_a.head(selection_number)
    df_a = df_a[['Away Team', 'Away Team Aerials Won', 'Home Team']]
    # Chart for Away Team Total Aerials Won
    #fig = px.bar(df, x="Away Team", y="Away Team Aerials Won", color="Home Team", barmode="group")
    #Scatter Plot for Away Team Total Aerials Won
    fig = px.scatter(df_a, x="Away Team", y="Away Team Aerials Won", color="Home Team",size = "Away Team Aerials Won")
    # Increase the plot size
    fig.update_layout(
        autosize=False,
        width=750,
        height=500,
    )
    st.plotly_chart(fig)
    with st.expander('See Explanation'):
        st.markdown("This chart shows the teams with the highest total aerials won based on the year selected. The home team and away team are displayed in the chart.")

elif selection == "Clearances":
        
    year = st.slider("Select the  Year", 2014, 2020, 2016)
    #Home Team Total Clearances
    st.subheader("Home Team Total Clearances")
    #Teams with the highest Home total clearances based on the year selected and display the away team on that match
    df = df[df['year'] == year]
    df_h = df.sort_values(by=['Home Team Clearances'], ascending=False)
    df_h = df_h.head(selection_number)
    df_h = df_h[['Home Team', 'Home Team Clearances', 'Away Team']]
    # Chart for Home Team Total Clearances
    #fig = px.bar(df, x="Home Team", y="Home Team Clearances", color="Away Team", barmode="group")
    #Scatter Plot for Home Team Total Clearances
    fig = px.scatter(df_h, x="Home Team", y="Home Team Clearances", color="Away Team",size = "Home Team Clearances")
    # Increase the plot size
    fig.update_layout(
        autosize=False,
        width=750,
        height=500,
    )
    st.plotly_chart(fig)
    # Away Team Total Clearances
    st.subheader("Away Team Total Clearances")
    #Teams with the highest Away total clearances based on the year selected and display the home team on that match
    df_a = df.sort_values(by=['Away Team Clearances'], ascending=False)
    df_a = df_a.head(selection_number)
    df_a = df_a[['Away Team', 'Away Team Clearances', 'Home Team']]
    # Chart for Away Team Total Clearances
    #fig = px.bar(df, x="Away Team", y="Away Team Clearances", color="Home Team", barmode="group")
    #Scatter Plot for Away Team Total Clearances
    fig = px.scatter(df_a, x="Away Team", y="Away Team Clearances", color="Home Team",size = "Away Team Clearances")
    # Increase the plot size
    fig.update_layout(
        autosize=False,
        width=750,
        height=500,
    )
    st.plotly_chart(fig)
    with st.expander('See Explanation'):
        st.markdown("This chart shows the teams with the highest total clearances based on the year selected. The home team and away team are displayed in  the chart.")
    
st.header("Other Interesting Charts")




df = pd.read_csv("D:/EPITA/data-reporting-visualisation/Final_Project/Data/german bundesliga data.csv")





#Donut Chart for Home Team Goals Scored vs Away Team Goals Scored
st.subheader("Home Team Goals Scored vs Away Team Goals Scored")
df_1 = df[['Home Team Goals Scored', 'Away Team Goals Scored']]
df_1 = df_1.sum()
fig = px.pie(df_1, values=df_1.values, names=df_1.index, title='Home Team Goals Scored vs Away Team Goals Scored',hole=.3)
# Increase the plot size
fig.update_layout(
    autosize=False,
    width=750,
    height=500,
)

st.plotly_chart(fig)
with st.expander('See Explanation'):
    st.markdown("This chart shows the total goals scored by the home team and away team in the Bundesliga.")


# Line chart to show match excitement on each year
st.subheader("Match Excitement on Each Year")
df_2 = df[['year', 'Match Excitement']]
df_2 = df_2.groupby('year').sum()
fig = px.line(df_2, x=df_2.index, y="Match Excitement", title='Match Excitement on Each Year')
#Update y axes name
fig.update_yaxes(title_text='Match Excitement- Total Cummulative Points')
fig.update_layout(
    autosize=False,
    width=750,
    height=500,
)
st.plotly_chart(fig)
with st.expander('See Explanation'):
    st.markdown("This chart shows the total match excitement on each year in the Bundesliga.")


# Density plot for Home Team Goals Scored
st.subheader("Home Team Goals Scored Distribution")
df_3 = df[['Home Team Goals Scored']]
fig = px.density_heatmap(df_3, x="Home Team Goals Scored", marginal_x="histogram", marginal_y="rug", title='Home Team Goals Scored')
fig.update_layout(
    autosize=False,
    width=750,
    height=500,
)
#update y name
fig.update_yaxes(title_text='Density')

st.plotly_chart(fig)
with st.expander('See Explanation'):
    st.markdown("We can clearly see that number of matches having 1 Home team goal is not so far from 2. So, normally two goals .This chart shows the distribution of the home team goals scored in the Bundesliga.")

# Distribution chart for Away Team Goals Scored
st.subheader("Away Team Goals Scored Distribution")
df_4 = df[['Away Team Goals Scored']]
fig = px.density_heatmap(df_4, x="Away Team Goals Scored", marginal_x="histogram", marginal_y="rug", title='Away Team Goals Scored')
fig.update_layout(
    autosize=False,
    width=750,
    height=500,
)
#update y name
fig.update_yaxes(title_text='Density')

st.plotly_chart(fig)
with st.expander('See Explanation'):
    st.markdown("We can clearly see that number of matches having 1 Away team goal is  so far from 2. So, normally 0 - 1 .This chart shows the distribution of the away team goals scored in the Bundesliga.")

# Line  graph for Shot On target on each year
st.subheader("Shot On Target on Each Year")
df_5 = df[['year', 'Home Team On Target Shots', 'Away Team On Target Shots']]
df_5 = df_5.groupby('year').sum()
fig = px.line(df_5, x=df_5.index, y=["Home Team On Target Shots", "Away Team On Target Shots"], title='Shot On Target on Each Year')
fig.update_layout(
    autosize=False,
    width=750,
    height=500,
)
#update y name
fig.update_yaxes(title_text='Shot On Target')

st.plotly_chart(fig)
with st.expander('See Explanation'):
    st.markdown("This chart shows the total shot on target on each year in the Bundesliga.")

# Line  graph for Shot Off target on each year
st.subheader("Shot Off Target on Each Year")
df_6 = df[['year', 'Home Team Off Target Shots', 'Away Team Off Target Shots']]
df_6 = df_6.groupby('year').sum()
fig = px.line(df_6, x=df_6.index, y=["Home Team Off Target Shots", "Away Team Off Target Shots"], title='Shot Off Target on Each Year')
fig.update_layout(
    autosize=False,
    width=750,
    height=500,
)
#update y name
fig.update_yaxes(title_text='Shot Off Target')

st.plotly_chart(fig)
with st.expander('See Explanation'):
    st.markdown("This chart shows the total shot off target on each year in the Bundesliga.")

# Box plot for Home Team Total Fouls vs Away Team Total Fouls on each year
st.subheader(" Minimum, Maximum , Mean of Total Fouls on Each Year")
df_7 = df[['year', 'Home Team Fouls', 'Away Team Fouls']]
df_7 = df_7.groupby('year').sum()
fig = px.box(df_7, x=df_7.index, y=["Home Team Fouls", "Away Team Fouls"], title='Minimum, Maximum , Mean of Total Fouls on Each Year')
fig.update_layout(
    autosize=False,
    width=750,
    height=500,
)
#update y name
fig.update_yaxes(title_text='Total Fouls')
fig.update_xaxes(title_text='Year')

st.plotly_chart(fig)
with st.expander('See Explanation'):
    st.markdown("This chart shows the minimum, maximum and mean of the total fouls on each year in the Bundesliga.")


# Area Chart for Total Cards on each year 
st.subheader("Total Cards on Each Year by Home Team and Away Team")
df_8 = df[['year', 'Home Team Red Cards', 'Home Team Yellow Cards', 'Away Team Red Cards', 'Away Team Yellow Cards']]
#sum of red and yellow cards
df_8['Home Team Red Cards'] = df_8['Home Team Red Cards'] + df_8['Home Team Yellow Cards']
df_8['Away Team Red Cards'] = df_8['Away Team Red Cards'] + df_8['Away Team Yellow Cards']
df_8 = df_8.groupby('year').sum()
fig = px.area(df_8, x=df_8.index, y=["Home Team Red Cards", "Away Team Red Cards"], title='Home Team vs Away Team Cards on Each Year')
fig.update_layout(
    autosize=False,
    width=750,
    height=500,
)
#update y name
fig.update_yaxes(title_text='Red Cards vs Yellow Cards')
fig.update_xaxes(title_text='Year')

st.plotly_chart(fig)
with st.expander('See Explanation'):
    st.markdown("This chart shows the total cards on each year in the Bundesliga.")

