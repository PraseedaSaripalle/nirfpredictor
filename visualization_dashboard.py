import streamlit as st
import pandas as pd
import os
import plotly.express as px
import matplotlib.pyplot as plt
import altair as alt
import numpy as np

def load_datasets(year):
    file_path = f"D:/BTech/Major_Project_2024Jan/Data/{year}.csv"  # Adjust the path as per your file location
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    return None




def visualization():
    selected_year = st.sidebar.selectbox(
            'Select Year:',
            ['2018', '2019', '2020', '2021', '2022', '2023']
            )
    data=load_datasets(selected_year)
    # Identify non-numeric columns
    non_numeric_columns = data.select_dtypes(exclude=['number']).columns
    # Data elements
    st.header("Data Overview")
    click_button = st.button("View Data")
    if click_button:
        st.subheader("Displaying Data")
        st.progress(90)
        with st.spinner("Waiting..."):
            st.write("Loading...")
        st.dataframe(data)
  

    # Plotting
    st.header('Relationship across different Metrics')

    # Select columns for scatter plot
    x_column = st.selectbox('Select X-axis column:', data.columns)
    y_column = st.selectbox('Select Y-axis column:', data.columns)
    # Create scatter plot
    scatter_plot = px.scatter(data, x=x_column, y=y_column, title=f'{x_column} vs {y_column}')
    st.plotly_chart(scatter_plot)
    # Explanation of the scatter plot
    st.subheader("Explanation:")

    # Calculate correlation coefficient
    correlation_coefficient = np.corrcoef(data[x_column], data[y_column])[0, 1]

    if correlation_coefficient > 0.7:
        explanation = "There is a strong positive correlation between {} and {}. This indicates that as {} increases, {} also tends to increase, and vice versa.".format(x_column, y_column, x_column, y_column)
    elif correlation_coefficient < -0.7:
        explanation = "There is a strong negative correlation between {} and {}. This indicates that as {} increases, {} tends to decrease, and vice versa.".format(x_column, y_column, x_column, y_column)
    elif correlation_coefficient > 0.3:
        explanation = "There is a moderate positive correlation between {} and {}. This indicates that as {} increases, {} also tends to increase, and vice versa, but the relationship is not as strong as in the case of a strong positive correlation.".format(x_column, y_column, x_column, y_column)
    elif correlation_coefficient < -0.3:
        explanation = "There is a moderate negative correlation between {} and {}. This indicates that as {} increases, {} tends to decrease, and vice versa, but the relationship is not as strong as in the case of a strong negative correlation.".format(x_column, y_column, x_column, y_column)
    else:
        explanation = "There is little to no correlation between {} and {}. This suggests that there is no clear relationship between the two variables.".format(x_column, y_column)
    st.write(explanation)

    #bar charts
    # Get unique list of universities
    st.header(f"Comparison of metrics Across Selected Universities")
    universities = data['UniversityName'].unique()

    # Select up to 10 universities
    selected_universities = st.multiselect("Select Universities (Max 10)", universities, universities[:5], help="Hold down 'Ctrl' (Windows) or 'Command' (Mac) to select multiple universities")

    # Select metric
    metric = st.selectbox("Select Metric", data.columns)

    # Filter data for selected universities
    selected_data = data[data['UniversityName'].isin(selected_universities)]

    # Create bar chart
    st.subheader(f"Comparison of {metric} Across Selected Universities")
    if len(selected_universities) > 0:
        bar_chart = px.bar(selected_data, x='UniversityName', y=metric, title=f"{metric} Across Selected Universities")
        st.plotly_chart(bar_chart)
    else:
        st.warning("Please select at least one university.")

    #Comparison of Multiple Metrics for a Single University
    st.header("Comparision of Multiple Metrics for Single University")
    # Get unique list of universities
    universities = data['UniversityName'].unique()

    # Select single university
    selected_university = st.selectbox("Select University", universities)

    # Select multiple metrics
    selected_metrics = st.multiselect("Select Metrics", data.columns)

    # Filter data for selected university
    selected_data = data[data['UniversityName'] == selected_university]

    # Prepare DataFrame for grouped bar chart
    metric_df = pd.DataFrame({
        'Metric': selected_metrics,
        'Value': selected_data[selected_metrics].values.flatten()
    })

    # Create grouped bar chart
    st.subheader(f"Comparison of Metrics for {selected_university}")
    if len(selected_metrics) > 0:
        grouped_bar_chart = px.bar(metric_df, x='Metric', y='Value', title=f"Metrics Comparison for {selected_university}", barmode='group')
        st.plotly_chart(grouped_bar_chart)
    else:
        st.warning("Please select at least one metric.")

    #vega lite chart
    # Get unique list of universities
    st.header("Ranking Comparision for a Metric for all the Universities")
    universities = data['UniversityName'].unique()

    # Select single metric
    selected_metric = st.selectbox("Select Metric", data.columns, key="select_metric")


    # Compute rankings for selected metric
    rankings = data.groupby('UniversityName')[selected_metric].mean().sort_values(ascending=False).reset_index()
    rankings['Rank'] = rankings.index + 1

    # Create Vega-Lite horizontal bar chart
    chart = alt.Chart(rankings).mark_bar().encode(
        x=alt.X('Rank:Q', title='Rank'),
        y=alt.Y('UniversityName:N', title='University'),
        tooltip=['UniversityName', 'Rank'],
        ).properties(
        title=f'Ranking Comparison for {selected_metric}'
        ).configure_axis(
        labelFontSize=12,
        titleFontSize=14
        ).configure_title(
        fontSize=16
        ).configure_legend(
        title=None,
        labelFontSize=12
        ).configure_axisY(
        labelFontSize=12
        ).interactive()

    # Display chart
    st.altair_chart(chart, use_container_width=True)    

    #line chart
    st.header("Line Chart")
    columns_to_display = ['UniversityName', 'SSValue', 'FSRValue', 'FQEValue', 'FRUValue', 'PUValue', 'QPValue', 'IPRValue',
                        'FPPPValue', 'GPHValue', 'GUEValue', 'MSValue', 'GPHDValue', 'RDValue', 'wDValue',
                        'PcsValue', 'PRValue']

    # Define a function to create line chart for a single metric
    def create_line_chart(data, university, metric):
        # Filter data by selected university
        data_filtered = data[data['UniversityName'].isin(university)]
        
        # Create line chart using Plotly Express
        line_chart = px.line(data_filtered, x='UniversityName', y=metric, title=f'{metric} for {", ".join(university)}')
        
        return line_chart

 

    # Create multiselect widget for selecting university
    selected_university = st.multiselect("Select University", data['UniversityName'].unique())

    # Create line chart for each metric
    if selected_university:
        for metric in columns_to_display[1:]:  # Exclude 'UniversityName'
            line_chart = create_line_chart(data, selected_university, metric)
            st.plotly_chart(line_chart)
    else:
        st.warning("Please select at least one university.")

    # Additional Components
    st.sidebar.header('About')
    st.sidebar.info('This is a dashboard to visualize university metrics.')
    