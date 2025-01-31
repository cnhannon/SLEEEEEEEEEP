
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Set wide page layout (optional but recommended for background images)
st.set_page_config(layout="wide")

# Load datasets
sleep_data = pd.read_csv("sleep_data_final.csv")
health_and_lifestyle_data = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")
rail_workers_data = pd.read_csv("rail_workers_sleep_data.csv")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Introduction", "Consumption Habits & Sleep Efficiency", "Lifestyle Factors & Stress", "Lifestyle and Wellbeing Analysis", "Work-Related Stress & Sleep", "Conclusion"])


# ------------------------------------------------------------------------------------------------

if page == "Home":
    st.markdown(
        """
        <style>
        /* Apply the background image to the entire app */
        .stApp {
            background: url('https://github.com/cnhannon/sleeeeeeeeep/raw/main/images/04.png');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }
    
        /* Optional: Customize the sidebar to have a slight transparency */
        .css-1d391kg {
            background: rgba(255, 255, 255, 0.1);  /* Adjust transparency */
        }
    
        /* Optional: Customize the main content area background (if needed) */
        .css-18e3th9 {
            background-color: transparent;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <h1 style='color:#d39c5d;'>SLEEEEEEEEEP 😴</h1>
        """, 
        unsafe_allow_html=True
    )

    #st.title("SLEEEEEEEEEP :zzz:")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Team :busts_in_silhouette:")
        st.markdown(
            """
            - **Sumeet Joshi**
            - **Julian Lwanga**
            - **Leah Ramsamy**
            - **Chris Hannon**
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.header("Tools :wrench:")
        st.markdown(
            """
            - Google Colab
            - Google BigQuery
            - Google Sheets
            - Google Docs
            - Streamlit
            - GitHub
            - Trello
            - Slack
            """,
            unsafe_allow_html=True
        )
    
    with col2:
        st.header("Datasets :link:")
        
        st.markdown(
            """
            - <a href="https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset" style="color:#be4cef;">Sleep, Health, and Lifestyle Dataset</a>
            - <a href="https://www.kaggle.com/code/hexenmeiser/sleep-efficiency-dataset-eda-and-scoring" style="color:#be4cef;">Sleep Efficiency Dataset</a>
            - <a href="https://www.kaggle.com/datasets/ydalat/lifestyle-and-wellbeing-data" style="color:#be4cef;">Lifestyle and Wellbeing Dataset</a>
            - <a href="https://catalog.data.gov/dataset/work-schedules-and-sleep-patterns-of-railroad-employees-dispatcher-background-survey" style="color:#be4cef;">Work Schedules and Sleep Patterns of Railroad Employees Dataset</a>
            """,
            unsafe_allow_html=True
        )


    # Display an image in your Streamlit app
    st.image("https://github.com/cnhannon/sleeeeeeeeep/raw/main/images/Slides Pojecect Lw cont.png", use_column_width=True)
    

# -----------------
# INTRODUCTION PAGE
# -----------------
if page == "Introduction":

    # START (TO ADD BACKGROUND IMAGE) - COPY AND PASTE BETWEEN START AND END. WILL NEED TO CHANGE IMAGE URL.

    st.markdown(
        """
        <style>
        /* Apply the background image to the entire app */
        .stApp {
            background: url('https://github.com/cnhannon/sleeeeeeeeep/raw/main/images/04.png');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }

        /* Optional: Customize the sidebar to have a slight transparency */
        .css-1d391kg {
            background: rgba(255, 255, 255, 0.1);  /* Adjust transparency */
        }

        /* Optional: Customize the main content area background (if needed) */
        .css-18e3th9 {
            background-color: transparent;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # END

    st.markdown(
        """
        <h1 style='color:#d39c5d;'>Sleep, Lifestyle, and Job Factors: A Data Analysis Journey 📈</h1>
        """, 
        unsafe_allow_html=True
    )

    
    #st.title("Sleep, Lifestyle, and Job Factors: A Data Analysis Journey :chart_with_upwards_trend:")
    st.header("The Modern Sleep Problem")
    st.write("""
    Sleep quality is declining globally, influenced by numerous factors including lifestyle choices, consumption habits, and job-related stress.
    In this analysis, we explore how caffeine and alcohol consumption, stress, physical activity, and job-related stress impact sleep efficiency,
    stress levels, and overall well-being. We are utilizing three datasets:
    - General Sleep Data: Provides individual sleep behaviors (e.g., caffeine, alcohol consumption, and sleep efficiency).
    - Health and Lifestyle Data: Examines how lifestyle attributes such as physical activity and stress affect sleep.
    - Rail Workers' Sleep Data: Focuses on job-related stress and its impact on rail workers' sleep quality.
    """)


# --------------------------------------------------------------------------------------------

# ---------------------------------------
# CONSUMPTION HABITS AND SLEEP EFFICIENCY
# ---------------------------------------
elif page == "Consumption Habits & Sleep Efficiency":

    # START

    st.markdown(
        """
        <style>
        /* Apply the background image to the entire app */
        .stApp {
            background: url('https://github.com/cnhannon/sleeeeeeeeep/raw/main/images/04.png');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }

        /* Optional: Customize the sidebar to have a slight transparency */
        .css-1d391kg {
            background: rgba(255, 255, 255, 0.1);  /* Adjust transparency */
        }

        /* Optional: Customize the main content area background (if needed) */
        .css-18e3th9 {
            background-color: transparent;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # END

    st.markdown(
        """
        <h1 style='color:#d39c5d;'>The Impact of Consumption Habits on Sleep Efficiency 🍷 ☕</h1>
        """, 
        unsafe_allow_html=True
    )

    
    #st.title("The Impact of Consumption Habits on Sleep Efficiency :wine_glass: :coffee:")
    col1, col2, col3 = st.columns(3)

    # ------------------------------------------
    # ADDED
    st.header("Dataset: Sleep Efficiency")
    #st.markdown("[Click here to visit Streamlit's website](https://streamlit.io)")
    # Button with an ":information_source:" icon and expander for definitions
    #st.write(":information_source: **Key Sleep Definitions**")
    with st.expander("**Key Terms**"):
        st.markdown("""
        - **Sleep Efficiency Duration**: The duration of time spent asleep while in bed, compared to total time spent in bed.
        - **REM Sleep Duration**: The stage of sleep spent in REM sleep, associated with dreaming and cognitive functions like memory and mood regulation.
        - **Deep Sleep Duration**: The stage of sleep where the body focuses on physical recovery and growth, as well as immune function. It's the most restorative phase of sleep.
        - **Light Sleep Duration**: The stage of sleep that makes up the majority of the sleep cycle. It's not as restorative as deep sleep but essential for transitioning between sleep stages.
        """)
        # -------ADDING--------
    # Create three columns but only use col1 and col3
    col1, col2 = st.columns([1, 1])
    # Participant demographics scorecard in column 1
    with col1:
        number_of_participants = 452  # Total number of participants
        age_range = "9 - 69 years"
        genders = {
            "Male": 228,
            "Female": 224,
            "Other": 0
        }
        # Title of the scorecard
        st.subheader("Participant Demographics")
        # Displaying number of participants
        st.metric(label="Number of Participants", value=number_of_participants)
        # Displaying age range
        st.metric(label="Age Range", value=age_range)
        # Displaying gender distribution
        st.subheader("Gender Distribution")
        for gender, count in genders.items():
            st.metric(label=gender, value=count)
        # Additional note

    # Average consumption metrics scorecard in column 3
    with col2:
        average_caffeine = 22.345133  # Average caffeine consumption in mg
        average_alcohol = 1.201327     # Average alcohol consumption in ounces
        # Title of the scorecard
        st.subheader("Average Consumption Metrics")
        # Displaying average caffeine consumption
        st.metric(label="Average Caffeine Consumption", value=f"{average_caffeine:.2f} mg")
        # Displaying average alcohol consumption
        st.metric(label="Average Alcohol Consumption", value=f"{average_alcohol:.2f} oz")
        # Key explaining the conversions
        st.subheader("Key:")
        st.write("1 oz of alcohol is approximately equal to 30 milliliters.")
        st.write("5 grams of caffeine is approximately equal to 30 mg of caffeine.")
        # Additional note


 #---------------------------------------------------
    #col1, col2=st.columns(2)
    # Key Insights section



    # ------------------------------------------

    # Deleted 3 graphs (scatter, candlestick, histogram)

    import pandas as pd
    import plotly.express as px
    import plotly.graph_objects as go
    import seaborn as sns
    import matplotlib.pyplot as plt
    import streamlit as st

    # Load the CSV file you uploaded (adjust the path if necessary)
    df = pd.read_csv("sleep_data_final.csv")  # Update the path

    # Define age ranges for filtering
    age_ranges = {
        "Teenagers": (9, 19),
        "20s": (20, 29),
        "30s": (30, 39),
        "40s": (40, 49),
        "50s": (50, 59),
        "60s": (60, 69)
    }

    # Add widgets for filtering the data
    st.sidebar.title("Filter Data")

    # Dropdown for Age Group
    age_group = st.sidebar.selectbox(
        'Age Group:', options=["All"] + list(age_ranges.keys()), index=0
    )

    # Dropdown for Gender
    gender = st.sidebar.selectbox(
        'Gender:', options=["All", "Male", "Female", "Other"], index=0
    )

    # Slider for Alcohol Consumption
    alcohol_range = st.sidebar.slider(
        'Alcohol Consumption:', min_value=0, max_value=int(df['Alcohol_consumption'].max()), value=(0, 5)
    )

    # Slider for Caffeine Consumption
    caffeine_range = st.sidebar.slider(
        'Caffeine Consumption:', min_value=0, max_value=int(df['Caffeine_consumption'].max()), value=(0, 200)
    )



 # -----------------------------
    # Function to filter data based on the selections
    def filter_data(df, age_group, gender, alcohol_range, caffeine_range):
        filtered_df = df.copy()

        # Filter by age group
        if age_group != "All":
            age_min, age_max = age_ranges[age_group]
            filtered_df = filtered_df[(filtered_df["Age"] >= age_min) & (filtered_df["Age"] <= age_max)]

        # Filter by gender
        if gender != "All":
            filtered_df = filtered_df[filtered_df["Gender"] == gender]

        # Filter by alcohol consumption
        filtered_df = filtered_df[
            (filtered_df["Alcohol_consumption"] >= alcohol_range[0]) &
            (filtered_df["Alcohol_consumption"] <= alcohol_range[1])
        ]

        # Filter by caffeine consumption
        filtered_df = filtered_df[
            (filtered_df["Caffeine_consumption"] >= caffeine_range[0]) &
            (filtered_df["Caffeine_consumption"] <= caffeine_range[1])
        ]

        return filtered_df

        # Apply the filters to the dataset
    filtered_df = filter_data(df, age_group, gender, alcohol_range, caffeine_range)
# ---------------Heatmap moved-------------

    # Apply the filters to the dataset
    #filtered_df = filter_data(df, age_group, gender, alcohol_range, caffeine_range)

    col1, col2, col3=st.columns(3)

    with col1:
        # Plot: Sleep Duration by Alcohol and Caffeine Levels (Bar Chart)
        fig_sleep_duration = px.bar(
            filtered_df, x="Alcohol_consumption", y="Sleep_Duration", color="Caffeine_consumption",
            title="Sleep Duration by Alcohol & Caffeine Levels",
             labels={
                "Alcohol_consumption": "Alcohol Consumption",   # Removing underscore in x-axis label
                "Sleep_Duration": "Sleep Duration",             # Removing underscore in y-axis label
                "Caffeine_consumption": "Caffeine Consumption"  # Removing underscore in legend label
            }
        )
        st.plotly_chart(fig_sleep_duration)

    # !! Deleted a line chart !!

    with col2:
        # ----------------------------ADDING-------------------------------------
        # Scatter Plot: Sleep Proportions (REM, Deep, Light) by Alcohol Consumption
        fig_sleep_proportions_alcohol = go.Figure()
        for sleep_type, color in zip(['Rem_Sleep_Duration', 'Deep_Sleep_Duration', 'Light_Sleep_Duration'],
                                      ['blue', 'green', 'orange']):
            fig_sleep_proportions_alcohol.add_trace(go.Scatter(
                x=filtered_df['Alcohol_consumption'], y=filtered_df[sleep_type],
                mode='markers', name=sleep_type.replace('_', ' ').capitalize(),
                marker=dict(size=8, opacity=0.6, color=color)
            ))
        # Update layout
        fig_sleep_proportions_alcohol.update_layout(
            title="Light, Deep, REM Sleep Durations by Alcohol Consumption",
            xaxis_title="Alcohol Consumption (ounces)",
            yaxis_title="Sleep Duration (hours)",
            showlegend=True
        )
        st.plotly_chart(fig_sleep_proportions_alcohol)

    with col3:
        # Scatter Plot: Sleep Proportions (REM, Deep, Light) by Caffeine Consumption
        fig_sleep_proportions_caffeine = go.Figure()
        for sleep_type, color in zip(['Rem_Sleep_Duration', 'Deep_Sleep_Duration', 'Light_Sleep_Duration'],
                                      ['purple', 'green', 'yellow']):
            fig_sleep_proportions_caffeine.add_trace(go.Scatter(
                x=filtered_df['Caffeine_consumption'], y=filtered_df[sleep_type],
                mode='markers', name=sleep_type.replace('_', ' ').capitalize(),
                marker=dict(size=8, opacity=0.6, color=color)
            ))
        # Update layout
        fig_sleep_proportions_caffeine.update_layout(
            title="Light, Deep, REM Sleep Durations by Caffeine Consumption",
            xaxis_title="Caffeine Consumption (mg)",
            yaxis_title="Sleep Duration (hours)",
            showlegend=True
        )
        st.plotly_chart(fig_sleep_proportions_caffeine)

    # -----------------------------------------------------------------------



    # Create 'Age_Group' if it doesn't exist
    if "Age_Group" not in filtered_df.columns:
        filtered_df["Age_Group"] = pd.cut(filtered_df["Age"], bins=[0, 19, 29, 39, 49, 59, 69],
                                           labels=["Teenagers", "20s", "30s", "40s", "50s", "60s"])

    # Create the pivot table for Sleep Efficiency
    heatmap_data = filtered_df.pivot_table(
        values='Sleep_efficiency_hours', index='Age_Group', columns='Gender', aggfunc='mean' #please add _hours to sleep efficiency so that it can be shown in hours not decimal
    )

    # Set up the heatmap
    plt.figure(figsize=(10, 6), facecolor="#FAD8D3")  # Light pink background for the figure
    ax = sns.heatmap(heatmap_data, annot=True, cmap="YlGnBu", cbar=True)

    # Set background color for the axes
    ax.set_facecolor("#FAD8D3")  # Light pink background for the axes

    # Title and labels
    plt.title('Sleep Efficiency by Age Group and Gender', fontsize=16)
    plt.xlabel('Gender', fontsize=12)
    plt.ylabel('Age Group', fontsize=12)


    # Show the heatmap using Streamlit
    st.pyplot(plt)

    st.subheader("Key Insights :mag:")
    col1, col2 = st.columns(2)
    with col1:
    
        st.markdown("""
        - **Caffeine’s Impact on REM Sleep**:
          - Moderate caffeine shows limited disruption, while higher levels show more interference with **REM Sleep**.
        - **Caffeine Consumption**:
          - Negative impact on **Light Sleep**.
          - **Stable Sleep Duration** with moderate caffeine intake.
          - High caffeine consumption (100 mg – 200 mg) negatively influences **Deep Sleep**.
        """)

    with col2:
        st.markdown("""
        - **Alcohol Consumption**:
          - Initial increase in **Light Sleep**.
          - Decrease in **Light Sleep** with higher alcohol consumption.
          - **Stable Sleep Duration** regardless of intake.
        """)
    # Display the filtered data summary
    #st.write(f"Filtered Data: {len(filtered_df)} Participants")
    #st.dataframe(filtered_df)


# ----------------------------------------------------------------------------------

# ----------------------------
# LIFESTYLE FACTORS AND STRESS
# ----------------------------
elif page == "Lifestyle Factors & Stress":
    st.markdown(
        """
        <style>
        /* Apply the background image to the entire app */
        .stApp {
            background: url('https://github.com/cnhannon/sleeeeeeeeep/raw/main/images/05.png');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }

        /* Optional: Customize the sidebar to have a slight transparency */
        .css-1d391kg {
            background: rgba(255, 255, 255, 0.1);  /* Adjust transparency */
        }

        /* Optional: Customize the main content area background (if needed) */
        .css-18e3th9 {
            background-color: transparent;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <h1 style='color:#d39c5d;'>Lifestyle Factors and Stress 🏃</h1>
        """, 
        unsafe_allow_html=True
    )

    #st.title("Lifestyle Factors and Stress :runner:")

    st.header("Dataset: Sleep, Health, and Lifestyle")
    # Button with an ":information_source:" icon and expander for definitions
    #st.write(":information_source: **Key Sleep Definitions**")


    col1, col2, col3 = st.columns(3)

    # Graph 4: Stress vs Sleep Quality - Scatter plot
    with col1:
        fig4 = px.scatter(health_and_lifestyle_data, x="Stress_Level", y="Quality_of_Sleep", trendline="ols", title="Stress Levels vs Quality of Sleep", color_discrete_sequence=["#32CD32"], labels={"Stress_Level": "Stress Level", "Quality_of_Sleep": "Quality of Sleep"})
        st.plotly_chart(fig4, use_container_width=True)

    # Graph 5: Physical Activity vs Sleep Quality - Bar plot (changed from line plot)
    with col2:
        fig100 = px.scatter_3d(health_and_lifestyle_data, x='Physical_Activity_Level', y='Stress_Level', z='Sleep_Duration',
            color='Physical_Activity_Level', title="Interaction of Physical Activity, Stress Level, and Sleep Duration with Age",
            labels={'Physical_Activity_Level': 'Physical Activity', 'Stress_Level': 'Stress Level', 'Sleep_Duration': 'Sleep Duration', 'Age': 'Age'})
        st.plotly_chart(fig100, use_container_width=True)

    vibrant_colors = px.colors.qualitative.Bold
    # Graph 6: Sleep Quality by Occupation - Bar chart
    with col3:
        # Use the correct columns from your dataset for the bubble chart
        fig6 = px.scatter(health_and_lifestyle_data,
                         x="Sleep_Duration",  # Correct column for sleep hours
                         y="Daily_Steps",  # Correct column for daily steps
                         size="Stress_Level",  # Correct column for stress level
                         color="Age",  # Correct column for age
                         hover_name="Gender",  # Correct column for gender
                         title="Sleep Duration vs Daily Steps with Stress Level",
                         labels={"Sleep_Duration": "Sleep Duration (hours)", "Daily_Steps": "Daily Steps"},
                         size_max=20,
                         color_discrete_sequence=vibrant_colors)  # Adjust max size of bubbles

        # Display the bubble chart in Streamlit
        st.plotly_chart(fig6)

        #Key Insights
    # --------------------------------------------------------------------------------------------------
    st.subheader("Key Insights :mag:")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        - **Higher stress levels are directly linked to poorer sleep quality**:
            - As stress increases, participants tend to experience shorter, lighter, and more fragmented sleep.
        - **Physical activity can help mitigate the negative effects of stress on sleep**:
            - Those who engage in regular physical activity, even at moderate levels, report better sleep quality and longer sleep duration, despite high stress levels.
        """)
    with col2:
        st.markdown("""
        - **Occupational impact on sleep**:
            - Certain high-stress jobs, particularly those with irregular schedules or high demands, are associated with lower sleep quality. Workers in these roles are more likely to report sleep disturbances.
        - **Balancing stress and activity is key**:
            - Individuals with lower stress levels and higher physical activity tend to fall into the “optimal sleep” category, getting the recommended 6-8 hours of sleep per night.
        """)
    # --------------------------------------------------------------------------------------------------





elif page == "Lifestyle Factors & Stress 2":
    st.header("Page 3.5: Lifestyle Factors and Stress")
    col1, col2, col3 = st.columns(3)



    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    import streamlit as st

    # Load the CSV file (adjust the path as necessary)
    df = pd.read_csv("lifestylewellbeingdata.csv")

    # Filter out invalid DAILY_STRESS values and convert to integer
    df_clean = df[df["DAILY_STRESS"] != '36526']
    df_clean["DAILY_STRESS"] = df_clean["DAILY_STRESS"].astype(int)

    # Converting 'Timestamp' column to datetime format and extracting Date
    df_clean['Date'] = df['Timestamp'].str.split(' ').str[0]
    df_clean = df_clean.drop_duplicates()

    # Moving 'Date' to the first column
    first_column = df_clean.pop('Date')
    df_clean.insert(0, 'Date', first_column)

    # Correlation Analysis
    lifestyle_columns = ['SLEEP_HOURS', 'DAILY_STRESS', 'DAILY_STEPS', 'WORK_LIFE_BALANCE_SCORE', 'TIME_FOR_PASSION']
    correlation_matrix = df_clean[lifestyle_columns].corr()

    # Page 6: Lifestyle and Wellbeing Analysis
    st.header("Lifestyle and Wellbeing Analysis")

    # Display the correlation matrix
    st.subheader("Correlation Matrix")
    st.write("Correlation between Sleep Hours and Lifestyle Variables:")
    st.dataframe(correlation_matrix)

    # Plotting the Distribution of Sleep Categories
    def categorize_sleep(hours):
        if hours < 6:
            return 'Short Sleep'
        elif 6 <= hours <= 8:
            return 'Optimal Sleep'
        else:
            return 'Long Sleep'

    df_clean['SLEEP_CATEGORY'] = df_clean['SLEEP_HOURS'].apply(categorize_sleep)

    st.subheader("Distribution of Sleep Categories")
    fig, ax = plt.subplots()
    sns.countplot(x='SLEEP_CATEGORY', data=df_clean, palette='Set3', ax=ax)
    ax.set_title("Distribution of Sleep Categories", fontsize=16)
    ax.set_xlabel("Sleep Category", fontsize=12)
    ax.set_ylabel("Count", fontsize=12)
    st.pyplot(fig)

    # Average Sleep Hours by Age and Gender
    st.subheader("Average Sleep Hours by Age and Gender")
    avg_sleep_by_age_gender = df_clean.groupby(['AGE', 'GENDER'])['SLEEP_HOURS'].mean().unstack()
    fig, ax = plt.subplots(figsize=(10, 6))
    avg_sleep_by_age_gender.plot(kind='bar', ax=ax)
    ax.set_title('Average Sleep Hours by Age and Gender', fontsize=14)
    ax.set_ylabel('Average Sleep Hours')
    ax.set_xlabel('Age Group')
    plt.xticks(rotation=0)
    st.pyplot(fig)

    # Regression Plot: Sleep Hours vs Work-Life Balance Score
    st.subheader("Sleep Hours vs Work-Life Balance Score")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.regplot(x=df_clean['SLEEP_HOURS'], y=df_clean['WORK_LIFE_BALANCE_SCORE'], scatter_kws={'s':50}, line_kws={'color':'red'}, ax=ax)
    ax.set_title('Sleep Hours vs Work-Life Balance', fontsize=14)
    ax.set_xlabel('Sleep Hours', fontsize=12)
    ax.set_ylabel('Work-Life Balance Score', fontsize=12)
    st.pyplot(fig)

    # Regression Plot: Sleep Hours vs Daily Stress
    st.subheader("Sleep Hours vs Daily Stress")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.regplot(x=df_clean['SLEEP_HOURS'], y=df_clean['DAILY_STRESS'], scatter_kws={'s':50}, line_kws={'color':'blue'}, ax=ax)
    ax.set_title('Sleep Hours vs Daily Stress', fontsize=14)
    ax.set_xlabel('Sleep Hours', fontsize=12)
    ax.set_ylabel('Daily Stress', fontsize=12)
    st.pyplot(fig)


# -----------------------------------------------------------------------------------


# --------LIFESTYLE AND WELLBEING ANALYSIS---------------
elif page == "Lifestyle and Wellbeing Analysis":
    st.markdown(
        """
        <style>
        /* Apply the background image to the entire app */
        .stApp {
            background: url('https://github.com/cnhannon/sleeeeeeeeep/raw/main/images/05.png');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }

        /* Optional: Customize the sidebar to have a slight transparency */
        .css-1d391kg {
            background: rgba(255, 255, 255, 0.1);  /* Adjust transparency */
        }

        /* Optional: Customize the main content area background (if needed) */
        .css-18e3th9 {
            background-color: transparent;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <h1 style='color:#d39c5d;'>Lifestyle and Wellbeing Analysis ☯️</h1>
        """, 
        unsafe_allow_html=True
    )

    #st.title("Lifestyle and Wellbeing Analysis :yin_yang:")
    st.header("Dataset: Lifestyle and Wellbeing")
    with st.expander("**Key Terms**"):
        st.markdown("""
        - **Daily Stress**: How much stress do you typically experience every day.
        - **Work Life Balance Score**: Score calculated by AH.COM algorithm.
        """)

# CHANGED TO 2 COL
    col1, col2 = st.columns(2)

    with col1:

        import pandas as pd
        import seaborn as sns
        import matplotlib.pyplot as plt
        import streamlit as st

        # Load the CSV file (adjust the path as necessary)
        df = pd.read_csv("lifestylewellbeingdata.csv")

        # Filter out invalid DAILY_STRESS values and convert to integer
        df_clean = df[df["DAILY_STRESS"] != '36526']
        df_clean["DAILY_STRESS"] = df_clean["DAILY_STRESS"].astype(int)

        # Converting 'Timestamp' column to datetime format and extracting Date
        df_clean['Date'] = df['Timestamp'].str.split(' ').str[0]
        df_clean = df_clean.drop_duplicates()

        # Moving 'Date' to the first column
        first_column = df_clean.pop('Date')
        df_clean.insert(0, 'Date', first_column)

        # Correlation Analysis
        lifestyle_columns = ['SLEEP_HOURS', 'DAILY_STRESS', 'DAILY_STEPS', 'WORK_LIFE_BALANCE_SCORE', 'TIME_FOR_PASSION']
        correlation_matrix = df_clean[lifestyle_columns].corr()


        # Display the correlation matrix
        # st.subheader("Correlation Matrix")
        # st.write("Correlation between Sleep Hours and Lifestyle Variables:")
        # st.dataframe(correlation_matrix)

        # Plotting the Distribution of Sleep Categories
        def categorize_sleep(hours):
            if hours < 6:
                return 'Short Sleep'
            elif 6 <= hours <= 8:
                return 'Optimal Sleep'
            else:
                return 'Long Sleep'

        df_clean['SLEEP_CATEGORY'] = df_clean['SLEEP_HOURS'].apply(categorize_sleep)

        #st.subheader("Distribution of Sleep Categories")
        # fig, ax = plt.subplots()
        # sns.countplot(x='SLEEP_CATEGORY', data=df_clean, palette='Set3', ax=ax)
        # ax.set_title("Distribution of Sleep Categories", fontsize=16)
        # ax.set_xlabel("Sleep Category", fontsize=12)
        # ax.set_ylabel("Count", fontsize=12)
        # st.pyplot(fig)
        # Assuming df_clean contains the 'SLEEP_CATEGORY' column
        fig = px.histogram(df_clean, x='SLEEP_CATEGORY', title='Distribution of Sleep Categories',
                        labels={'SLEEP_CATEGORY': 'Sleep Category'},
                        color_discrete_sequence=px.colors.qualitative.Set3)
        fig.update_layout(
                width=400,  # 8 inches approx
                height=300  # 6 inches approx
            )
        # Show the figure using Plotly
        st.plotly_chart(fig)

        # Average Sleep Hours by Age and Gender
        #st.subheader("Average Sleep Hours by Age and Gender")
        # avg_sleep_by_age_gender = df_clean.groupby(['AGE', 'GENDER'])['SLEEP_HOURS'].mean().unstack()
        # fig, ax = plt.subplots(figsize=(10, 6))
        # avg_sleep_by_age_gender.plot(kind='bar', ax=ax)
        # ax.set_title('Average Sleep Hours by Age and Gender', fontsize=14)
        # ax.set_ylabel('Average Sleep Hours')
        # ax.set_xlabel('Age Group')
        # plt.xticks(rotation=0)
        # st.pyplot(fig)

        avg_sleep_by_age_gender = df_clean.groupby(['AGE', 'GENDER'])['SLEEP_HOURS'].mean().unstack()


        fig = go.Figure()

        # Loop through each gender column and add a bar trace
        for gender in avg_sleep_by_age_gender.columns:
            fig.add_trace(go.Bar(
                x=avg_sleep_by_age_gender.index,  # Age groups
                y=avg_sleep_by_age_gender[gender],  # Average sleep hours
                name=gender  # Gender as the label for each trace
            ))

        # Set the title and labels
        fig.update_layout(
            title='Average Sleep Hours by Age and Gender',
            xaxis_title='Age Group',
            yaxis_title='Average Sleep Hours',
            barmode='group',
            width=400,  # 8 inches approx
            height=300# Grouped bar mode
        )

        st.plotly_chart(fig)


    with col2:
        # Regression Plot: Sleep Hours vs Work-Life Balance Score
        # st.subheader("Sleep Hours vs Work-Life Balance")
        # fig, ax = plt.subplots(figsize=(8, 6))
        # sns.regplot(x=df_clean['SLEEP_HOURS'], y=df_clean['WORK_LIFE_BALANCE_SCORE'], scatter_kws={'s':50}, line_kws={'color':'red'}, ax=ax)
        # ax.set_title('Sleep Hours vs Work-Life Balance', fontsize=14)
        # ax.set_xlabel('Sleep Hours', fontsize=12)
        # ax.set_ylabel('Work-Life Balance Score', fontsize=12)
        # st.pyplot(fig)

        fig = px.scatter(df_clean, x='SLEEP_HOURS', y='WORK_LIFE_BALANCE_SCORE',
                 trendline='ols',  # Ordinary least squares regression line
                 title='Sleep Hours vs Work-Life Balance',
                 labels={'SLEEP_HOURS': 'Sleep Hours', 'WORK_LIFE_BALANCE_SCORE': 'Work-Life Balance Score'},
                 trendline_color_override='red')

        fig.update_layout(
                width=400,  # 8 inches approx
                height=300  # 6 inches approx
            )

        st.plotly_chart(fig)


        # Regression Plot: Sleep Hours vs Daily Stress
        #st.subheader("Sleep Hours vs Daily Stress")

        # fig, ax = plt.subplots(figsize=(8, 6))
        # sns.regplot(x=df_clean['SLEEP_HOURS'], y=df_clean['DAILY_STRESS'], scatter_kws={'s':50}, line_kws={'color':'blue'}, ax=ax)
        # ax.set_title('Sleep Hours vs Daily Stress', fontsize=14)
        # ax.set_xlabel('Sleep Hours', fontsize=12)
        # ax.set_ylabel('Daily Stress', fontsize=12)
        # st.pyplot(fig)

        fig = px.scatter(df_clean, x='SLEEP_HOURS', y='DAILY_STRESS',
                 trendline='ols',  # Add regression line
                 title='Sleep Hours vs Daily Stress',
                 labels={'SLEEP_HOURS': 'Sleep Hours', 'DAILY_STRESS': 'Daily Stress'},
                 trendline_color_override='blue')

        fig.update_layout(
                width=400,  # 8 inches approx
                height=300  # 6 inches approx
            )

        st.plotly_chart(fig)

        # Key Insights section
    st.subheader("Key Insights :mag:")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        - **Key Insights for Lifestyle and Wellbeing Analysis**:
          - Differences in sleep patterns and stress levels across different groups.
        - **Gender Differences in Sleep**:
          - Highlighting variations in sleep habits and stress responses based on gender.
        """)
    with col2:
        st.markdown("""
        - **Sleep Categorization**:
          - **Short Sleepers**: Less than 6 hours of sleep.
          - **Adequate Sleepers**: 6 to 8 hours of sleep.
          - **Long Sleepers**: More than 8 hours of sleep.
        """)
    with col3:
        st.markdown("""
        - **High Stress and Sleep Disruptions**:
          - High stress leads to sleep disruptions or insufficient sleep.
        - **High Stress and Sleep Quality**:
          - Increased stress correlates with shorter sleep and poorer sleep quality.
        """)

# -----------------------------
# WORK-RELATED STRESS AND SLEEP
# -----------------------------
elif page == "Work-Related Stress & Sleep":
    st.markdown(
        """
        <style>
        /* Apply the background image to the entire app */
        .stApp {
            background: url('https://github.com/cnhannon/sleeeeeeeeep/raw/main/images/06.png');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }

        /* Optional: Customize the sidebar to have a slight transparency */
        .css-1d391kg {
            background: rgba(255, 255, 255, 0.1);  /* Adjust transparency */
        }

        /* Optional: Customize the main content area background (if needed) */
        .css-18e3th9 {
            background-color: transparent;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <h1 style='color:#d39c5d;'>Impact of Work-Related Stress on Sleep 👷</h1>
        """, 
        unsafe_allow_html=True
    )

    
    #st.title("Impact of Work-Related Stress on Sleep :construction_worker:")
    st.header("Dataset: Work Schedules and Sleep Patterns of Railroad Employees")

    # KEY TERMS
#------------
    with st.expander("**Key Terms**"):
        st.markdown("""
        - **Lack of Control**: Highlighting this as a primary contributor to stress impacting sleep loss.
        - **Time Off**: Emphasising the role of adequate rest periods in reducing sleep-related stress.
        - **Sleep Stress Correlation**: Summarising the relationship between work-related factors and sleep disturbances, especially focusing on stress levels.
        """)

#====================

    col1, col2 = st.columns(2)
    # Graph 7: Job Security vs Sleep Loss - Scatter plot
    with col1:

        import plotly.express as px
        import plotly.graph_objects as go

        # Load your newly uploaded rail workers dataset
        df_railworkers_clean = pd.read_csv("df_railworkers_clean(1).csv")

        # Dictionary for more descriptive labels
        variable_labels = {
            'Job_pressure': 'Job Pressure',
            'Emergencies': 'Emergencies',
            'Lack_of_control': 'Lack of Control',
            'Mgmt_policies': 'Management Policies',
            'Surges_in_work': 'Work Surges',
            'Communication': 'Communication',
            'Inadeq_Staff': 'Inadequate Staffing',
            'Resp_for_others_safety': 'Responsibility for Others\' Safety',
            'BreakTime': 'Break Time',
            'TimeOff': 'Time Off',
            'Sleep_loss': 'Sleep Loss'
        }

        # Correlation Analysis Function
        def perform_correlation_analysis(df, stress_columns):
            # Ensure all columns in the list exist in the DataFrame before performing correlation
            missing_columns = [col for col in stress_columns + ['Sleep_loss'] if col not in df.columns]
            if missing_columns:
                raise KeyError(f"The following columns are missing from the DataFrame: {missing_columns}")

            correlation_matrix = df[stress_columns + ['Sleep_loss']].corr()
            return correlation_matrix['Sleep_loss'].sort_values(ascending=False)

        # Full list of stress-related columns
        stress_columns = [
            'Job_pressure', 'Emergencies', 'Lack_of_control', 'Mgmt_policies',
            'Surges_in_work', 'Communication', 'Inadeq_Staff', 'Resp_for_others_safety',
            'BreakTime', 'TimeOff'
        ]

        # Run the correlation analysis
        try:
            sleep_loss_corr = perform_correlation_analysis(df_railworkers_clean, stress_columns)

            # Rename the index in the Series and convert it to a DataFrame with 'Sleep Loss' as the column name
            sleep_loss_corr_renamed = sleep_loss_corr.rename(index=variable_labels).to_frame()
            sleep_loss_corr_renamed.columns = ['Sleep Loss']

            # Remove 'Sleep Loss' from the x-axis variables
            stress_factors_without_sleep_loss = sleep_loss_corr_renamed.index.drop('Sleep Loss')

            # Plot the heatmap using Plotly
            fig = go.Figure(data=go.Heatmap(
                z=sleep_loss_corr_renamed['Sleep Loss'].values.reshape(1, -1),  # reshape for heatmap
                x=stress_factors_without_sleep_loss,
                y=['Sleep Loss'],
                colorscale=[[0, '#FFFFD9'], [1, '#1F80B8']],
                showscale=True,
                zmin=0.2,  # correlation ranges from -1 to 1
                zmax=0.6
            ))

            fig.update_layout(
                title="Correlation of Stress Factors with Sleep Loss",
                xaxis_title="Stress Factors",
                yaxis_title="",
                height=400
            )

            # Show the heatmap in Streamlit
            st.plotly_chart(fig)

        except KeyError as e:
            st.error(f"Error: {e}")






    # Graph 8: Work Surges vs Sleep Loss - Heatmap for correlation visualization
    with col2:
        from sklearn.linear_model import LinearRegression
        from sklearn.model_selection import train_test_split

        # Load the rail workers dataset


        # Define the stress-related columns and the target variable (Sleep_loss)
        stress_columns = [
            'Job_pressure', 'Emergencies', 'Lack_of_control', 'Mgmt_policies',
            'Surges_in_work', 'Communication', 'Inadeq_Staff', 'Resp_for_others_safety',
            'BreakTime', 'TimeOff'
        ]
        target_column = 'Sleep_loss'

        # Split the data into features (X) and target (y)
        X = df_railworkers_clean[stress_columns]
        y = df_railworkers_clean[target_column]

        # Train-test split for model training
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train a linear regression model
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Dictionary for more descriptive labels
        variable_labels = {
            'Job_pressure': 'Job Pressure',
            'Emergencies': 'Emergencies',
            'Lack_of_control': 'Lack of Control',
            'Mgmt_policies': 'Management Policies',
            'Surges_in_work': 'Work Surges',
            'Communication': 'Communication',
            'Inadeq_Staff': 'Inadequate Staffing',
            'Resp_for_others_safety': 'Responsibility for Others\' Safety',
            'BreakTime': 'Break Time',
            'TimeOff': 'Time Off'
        }

        # Display significant coefficients with readable labels
        significant_coeffs = pd.DataFrame({
            'Variable': stress_columns,
            'Coefficient': model.coef_
        }).sort_values(by='Coefficient', ascending=False)

        # Map the variables to more descriptive labels
        significant_coeffs['Variable'] = significant_coeffs['Variable'].map(variable_labels)

        # Plot the bar chart with the updated labels
        fig = px.bar(significant_coeffs.head(5),
                     x='Coefficient',
                     y='Variable',
                     orientation='h',
                     color_discrete_sequence=['#F9A002'],
                     title='Top 5 Predictors of Sleep Loss')

        # Show the updated plot in Streamlit
        st.plotly_chart(fig)

        # Key Insights section
    st.subheader("Key Insights :mag:")
    st.markdown("""
    - **High Stress Levels**:
      - Strong correlation with **Sleep Loss**, especially due to lack of control and time off.
    - **Sleep Loss Impact**:
      - Increased **Sleep Loss** leads to reduced **Alertness at Work**, creating a negative cycle between stress, poor sleep, and productivity.
    - **Key Contributors to Sleep Stress**:
      - Our regression analysis highlights **Lack of Control** and **Insufficient Time Off** as the largest contributors to sleep-related stress.
    """)


# ----------------------------------------------------------------------------------------------------

# ----------
# CONCLUSION
# ----------
elif page == "Conclusion":
    st.markdown(
        """
        <style>
        /* Apply the background image to the entire app */
        .stApp {
            background: url('https://github.com/cnhannon/sleeeeeeeeep/raw/main/images/06.png');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }

        /* Optional: Customize the sidebar to have a slight transparency */
        .css-1d391kg {
            background: rgba(255, 255, 255, 0.1);  /* Adjust transparency */
        }

        /* Optional: Customize the main content area background (if needed) */
        .css-18e3th9 {
            background-color: transparent;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <h1 style='color:#d39c5d;'>Conclusion 🛏️</h1>
        """, 
        unsafe_allow_html=True
    )

    
    #st.title("Conclusion :bed:")


    st.write("""
    Through this analysis, we have uncovered key insights about the various factors influencing sleep quality:
    """)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("""
        - **Caffeine and Alcohol Consumption:**
            - Both significantly impact sleep efficiency.
            - Alcohol shows a stronger negative correlation with sleep quality.
        """)
    with col2:
        st.write("""
        - **Stress Levels and Physical Activity:**
            - Higher stress levels are linked to poorer sleep outcomes.
            - Increased physical activity is associated with improved sleep quality.
        """)
    with col3:
        st.write("""
        - **Job-Related Stress in Rail Workers:**
            - Job insecurity and surges in workload directly contribute to reduced sleep quality.
            - Addressing job-related stress is crucial for enhancing sleep health.
        """)
    st.write(
        """
        - **Implications for Improvement:**
            - Recognising and addressing these factors can lead to better sleep health and overall well-being for individuals and organisations.
        """
    )

