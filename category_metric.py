import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to process TLR dataset
def process_csv_tlr(file_path):
    columns_to_use = ['UniversityName', 'SSValue', 'FSRValue', 'FQEValue', 'FRUValue']
    df = pd.read_csv(file_path, usecols=columns_to_use)
    df['UniversityName'] = df['UniversityName'].str.strip()
    df['total'] = df[['SSValue', 'FSRValue', 'FQEValue', 'FRUValue']].sum(axis=1)
    result_dict = df.set_index('UniversityName')['total'].to_dict()
    sorted_result = dict(sorted(result_dict.items(), key=lambda x: x[1], reverse=True))
    return sorted_result

# Function to process RP dataset
def process_csv_rp(file_path):
    columns_to_use = ['UniversityName', 'PUValue', 'QPValue', 'IPRValue', 'FPPPValue']
    df = pd.read_csv(file_path, usecols=columns_to_use)
    df['UniversityName'] = df['UniversityName'].str.strip()
    df['total'] = df[['PUValue', 'QPValue', 'IPRValue', 'FPPPValue']].sum(axis=1)
    result_dict = df.set_index('UniversityName')['total'].to_dict()
    sorted_result = dict(sorted(result_dict.items(), key=lambda x: x[1], reverse=True))
    return sorted_result

# Function to process GO dataset
def process_csv_go(file_path):
    columns_to_use = ['UniversityName', 'GPHValue', 'GUEValue', 'MSValue', 'GPHDValue']
    df = pd.read_csv(file_path, usecols=columns_to_use)
    df['UniversityName'] = df['UniversityName'].str.strip()
    df['total'] = df[['GPHValue', 'GUEValue', 'MSValue', 'GPHDValue']].sum(axis=1)
    result_dict = df.set_index('UniversityName')['total'].to_dict()
    sorted_result = dict(sorted(result_dict.items(), key=lambda x: x[1], reverse=True))
    return sorted_result

# Function to process OI dataset
def process_csv_oi(file_path):
    columns_to_use = ['UniversityName', 'RDValue', 'wDValue', 'ESCSValue', 'PcsValue']
    df = pd.read_csv(file_path, usecols=columns_to_use)
    df['UniversityName'] = df['UniversityName'].str.strip()
    df['total'] = df[['RDValue', 'wDValue', 'ESCSValue', 'PcsValue']].sum(axis=1)
    result_dict = df.set_index('UniversityName')['total'].to_dict()
    sorted_result = dict(sorted(result_dict.items(), key=lambda x: x[1], reverse=True))
    return sorted_result

# Function to process PR dataset
def process_csv_pr(file_path):
    columns_to_use = ['UniversityName', 'PRValue']
    df = pd.read_csv(file_path, usecols=columns_to_use)
    df['UniversityName'] = df['UniversityName'].str.strip()
    df['total'] = df[['PRValue']].sum(axis=1)
    result_dict = df.set_index('UniversityName')['total'].to_dict()
    sorted_result = dict(sorted(result_dict.items(), key=lambda x: x[1], reverse=True))
    return sorted_result

# Function to display rankings in a table
def display_rankings(result_dict):
    df = pd.DataFrame(list(result_dict.items()), columns=['UniversityName', 'Total'])
    st.table(df)

# Function to query rank for a university
def query_rank(sorted_dict, university_name):
    university_name = university_name.strip().lower()
    for rank, (uni, total) in enumerate(sorted_dict.items(), start=1):
        if university_name in uni.lower():
            return f'The rank of {uni.strip()} is {rank}'
    return f'University {university_name} not found in the dataset.'

# Function to plot top 10 universities
def plot_top_10(result):
    top_10_result = dict(list(result.items())[:10])
    universities = list(top_10_result.keys())
    totals = list(top_10_result.values())
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(universities, totals, color='skyblue')
    ax.set_xlabel('Total Value')
    ax.set_title('Top 10 Universities by Each Individual Values')
    ax.invert_yaxis()
    st.pyplot(fig)

# Function to load datasets dynamically
def load_datasets(year, metric):
    file_path = f"D:/BTech/Major_Project_2024Jan/Data/{year}.csv"
    if metric == "TLR":
        return process_csv_tlr(file_path)
    elif metric == "RP":
        return process_csv_rp(file_path)
    elif metric == "GO":
        return process_csv_go(file_path)
    elif metric == "OI":
        return process_csv_oi(file_path)
    elif metric == "PR":
        return process_csv_pr(file_path)
    return None

# Function to display category-wise ranking
def category_wise_ranking():
    sub_options = ("Top Universities Exceled in Teaching Learning Resources",
                   "Top Universities Exceled in Research and Professional Practice",
                   "Top Universities Exceled in Graduation Outcomes",
                   "Top Universities Exceled in Outreach and Inclusivity",
                   "Top Universities Exceled in Perception")
    selected_sub_option = st.radio("Select Sub-option", sub_options)
    selected_metric = ""
    if selected_sub_option == "Top Universities Exceled in Teaching Learning Resources":
        selected_metric = "TLR"
    elif selected_sub_option == "Top Universities Exceled in Research and Professional Practice":
        selected_metric = "RP"
    elif selected_sub_option == "Top Universities Exceled in Graduation Outcomes":
        selected_metric = "GO"
    elif selected_sub_option == "Top Universities Exceled in Outreach and Inclusivity":
        selected_metric = "OI"
    elif selected_sub_option == "Top Universities Exceled in Perception":
        selected_metric = "PR"

    if selected_metric:
        st.write(f"Displaying top universities excelled in {selected_sub_option}")
        selected_year = st.session_state.selected_year  # Access selected year from session state
        file_path = f"D:/BTech/Major_Project_2024Jan/Data/{selected_year}.csv"
        st.write(f"Loading data for year {selected_year} from {file_path}")
        result = load_datasets(str(selected_year), selected_metric)
        if result:
            st.write(f"Year {selected_year}:")
            display_rankings(result)
            query_university = st.text_input("Enter the university name to query rank:")
            if query_university:
                rank = query_rank(result, query_university)
                st.write(f"Rank for {query_university} in {selected_year}: {rank}")
            if st.button("Show Visualization"):
                plot_top_10(result)
        else:
            st.write(f"No data found for year {selected_year}")
