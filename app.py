import streamlit as st
import pandas as pd
import os
import plotly.express as px
import matplotlib.pyplot as plt
import altair as alt
import numpy as np
from chatbot import analyze_dataset,chatbot_response,questions
#from motivation import display_motivation
from category_metric import category_wise_ranking
from correlation_metric import corr
from prediction import load_dataset,train_model,predict_rank
from top_performers import top_performers_in_each_metric
from visualization_dashboard import visualization
from nirf_navigator import project_showcase

#from chatbot import process_query

def load_datasets(year):
    file_path = f"D:/BTech/Major_Project_2024Jan/Data/{year}.csv"  # Adjust the path as per your file location
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    return None

def main():
    st.title("Gayatri Vidya Parishad College of Engineering for Women")
    #st.subheader("Analysis Dashboard")

    
    st.sidebar.title("NIRF Navigator")
    selected_section = st.sidebar.radio("Go to", ("Project Overview", "Benchmarking","Visualization Dashboard","Admission AI Assistant"))

    if selected_section == "Project Overview":
        st.sidebar.header("**Project Overview**")
        project_option = st.sidebar.selectbox("Select Option", ("NIRF Navigator", "Motivation and Problem Definition", 
                                                                "Literature Survey", "Objectives", 
                                                                "Advantages and Limitations", "Project Architecture"))
        if project_option == "Motivation and Problem Definition":
            st.write("**Motivation and Problem Definition**")
            st.write("Welcome to Motivation and Problem Definition section")
            #display_motivation()
        elif project_option == "Literature Survey":
            st.write("**Literature Survey**")
            st.write("Welcome to Literature Survey section")
        elif project_option == "Objectives":
            st.write("**Objectives**")
            st.write("Welcome to Objectives section")
        elif project_option == "Advantages and Limitations":
            st.write("**Advantages and Limitations**")
            st.write("Welcome to Advantages and Limitations section")
        elif project_option == "Project Architecture":
            st.write("**Project Architecture**")
            st.write("Welcome to Project Architecture section")
        else:
            #st.write("**NIRF Navigator**")
            #st.write("Welcome to NIRF Navigator section")
            project_showcase()

    elif selected_section == "Benchmarking":
        st.sidebar.header("**Benchmarking**")
        selected_year = st.sidebar.radio("Select Year", ("2018", "2019", "2020", "2021", "2022", "2023"))

        # Initialize selected_year in session state
        st.session_state.selected_year = selected_year

        dataset = load_datasets(selected_year)
        if dataset is not None:
            st.write(f"Welcome to **{selected_year}** section")
            st.write("Top of the dataset:")
            st.write(dataset.head())
            st.write("Select an option:")
            benchmarking_options = ("Category-wise Ranking Grouping",
                                    "Top Performers in Each Metric",
                                    "Correlation Analysis",
                                    "Visualization of Metrics",
                                    "Trend Analysis Over Time")
            selected_option = st.selectbox("List of different Parameters are displayed here", benchmarking_options)

            if selected_option == "Category-wise Ranking Grouping":
                st.write("Displaying Category-wise Ranking Grouping")
                category_wise_ranking()
                # Implement logic for this option
            elif selected_option == "Top Performers in Each Metric":
                st.write("Displaying Top Performers in Each Metric")
                years = ["2018", "2019", "2020", "2021", "2022", "2023"]
                for year in years:
                    top_performers_in_each_metric(year)
                

                # Implement logic for this option
            elif selected_option == "Correlation Analysis":
                st.write("Displaying Correlation Analysis")
                corr(selected_year)
                # Implement logic for this option
            elif selected_option == "Visualization of Metrics":
                st.write("Displaying Visualization of Metrics")
                # Implement logic for this option
            elif selected_option == "Trend Analysis Over Time":
                st.write("Displaying Trend Analysis Over Time")
                st.header("Rank Prediction")
                # Load dataset
                data = pd.read_csv("D:\BTech\Major_Project_2024Jan\Prediction\AllYearsData.csv")
                from sklearn.model_selection import train_test_split
                # Split data into features (X) and target variable (y)
                X = data.drop(columns=['Rank'])
                y = data['Rank']

                # Split data into train and test sets
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

                # Train model
                models = train_model(data)
                st.write("Enter values for prediction:")
                # Input fields for SSValue, FSRValue, FQEValue, etc.
                ss_value = st.number_input("Student Strength including Doctoral Students (SS Value)", value=20.0)
                fsr_value = st.number_input("Faculty-student ratio with emphasis on permanent faculty (FSR Value)", value=30.0)
                fqe_value = st.number_input("Combined metric for Faculty with PhD (or equivalent) and Experience (FQE Value)", value=20.0)
                fru_value = st.number_input("Financial Resources and their Utilisation (FRU Value)", value=30.0)
                pu_value = st.number_input("Combined metric for Publications (PU Value)", value=35.0)
                qp_value = st.number_input("Combined metric for Quality of Publications (QP Value)", value=40.0)
                ipr_value = st.number_input("IPR and Patents: Published and Granted (IPR Value)", value=15.0)
                fppp_value = st.number_input("Footprint of Projects and Professional Practice (FPPP Value)", value=10.0)
                gph_value = st.number_input("GPH Value", value=40.0)
                gue_value = st.number_input("Metric for University Examinations (GUE Value)", value=15.0)
                ms_value = st.number_input("MS Value", value=25.0)
                gphd_value = st.number_input("Metric for Number of Ph.D. Students Graduated (GPHD Value)", value=20.0)
                rd_value = st.number_input("Percentage of Students from Other States/Countries (Region Diversity RD Value)", value=30.0)
                wd_value = st.number_input("Percentage of Women - Women Diversity (WD Value)", value=30.0)
                escs_value = st.number_input("Economically and Socially Challenged Students (ESCS Value)", value=20.0)
                pcs_value = st.number_input("Facilities for Physically Challenged Students (PCS Value)", value=20.0)
                pr_value = st.number_input("Perception (PR Value)", value=100.0)

                # Collect user inputs into a DataFrame
                user_input = pd.DataFrame({
                    "SSValue": [ss_value],
                    "FSRValue": [fsr_value],
                    "FQEValue": [fqe_value],
                    "FRUValue": [fru_value],
                    "PUValue": [pu_value],
                    "QPValue": [qp_value],
                    "IPRValue": [ipr_value],
                    "FPPPValue": [fppp_value],
                    "GPHValue": [gph_value],
                    "GUEValue": [gue_value],
                    "MSValue": [ms_value],
                    "GPHDValue": [gphd_value],
                    "RDValue": [rd_value],
                    "WDValue": [wd_value],
                    "ESCSValue": [escs_value],
                    "PCSValue": [pcs_value],
                    "PRValue": [pr_value]
                })

                 # Call predict_rank function
                prediction_results = predict_rank(models, user_input, X_test, y_test)

                # Display predicted rank
                st.write("Prediction Results:")
                st.write(prediction_results)
                
    elif selected_section=="Visualization Dashboard":
        visualization()
    
    elif selected_section=="Admission AI Assistant":
        st.title('Dataset Analysis and Chatbot')

        # Fixed dataset path
        dataset_path = "D:/BTech/Major_Project_2024Jan/Data/2023.csv"

        # Load dataset
        df = pd.read_csv(dataset_path)

        # Analyze dataset
        dataset_summary = analyze_dataset(df)

        # Display dataset summary
        st.subheader("Dataset Summary")
        st.write(dataset_summary)
        questions()

        # Chatbot
        st.subheader("Chatbot")
        user_question = st.text_input("Ask a question:")
        if st.button("Ask"):
            if user_question:
                response = chatbot_response(user_question, dataset_summary)
                st.write("Bot:", response)
            else:
                st.write("Bot:", "Please ask a question.")
            
        
if __name__ == "__main__":
    main()

