import streamlit as st
import pandas as pd

# Load data
data = pd.read_csv("D:/BTech/Major_Project_2024Jan/Data/2023.csv")  # Replace with your dataset

def analyze_dataset(dataset):
    # Your dataset analysis code goes here
    # For simplicity, let's just assume the dataset is a DataFrame
    # You can replace this with your actual dataset analysis code
    summary = dataset.describe()
    return summary

def chatbot_response(question, dataset_summary):
    # Extracting column names from the summary
    column_names = dataset_summary.columns.tolist()

    # Check if the question is about mean, standard deviation, number of entries, maximum, or minimum
    if "mean" in question.lower():
        for col in column_names:
            if col.lower() in question.lower():
                return f"The mean of column {col} is {dataset_summary.loc['mean', col]}"
    elif "standard deviation" in question.lower():
        for col in column_names:
            if col.lower() in question.lower():
                return f"The standard deviation of column {col} is {dataset_summary.loc['std', col]}"
    elif "entries" in question.lower() or "rows" in question.lower():
        return f"The dataset contains {dataset_summary.shape[0]} entries."
    elif "maximum" in question.lower():
        for col in column_names:
            if col.lower() in question.lower():
                return f"The maximum value in column {col} is {dataset_summary.loc['max', col]}"
    elif "minimum" in question.lower():
        for col in column_names:
            if col.lower() in question.lower():
                return f"The minimum value in column {col} is {dataset_summary.loc['min', col]}"
    else:
        return "I'm sorry, I don't understand that question."
    
def questions():
    st.subheader("Some of the Sample Questions that can be asked are mentioned:")
    st.write("What is the mean of column X?")
    st.write("What is the standard deviation of column Y?")        
    st.write("How many entries are there in the dataset?")        
    st.write("What is the maximum value in column Z?")        
    st.write("What is the minimum value in column W?")        

    

