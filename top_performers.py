import streamlit as st
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

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

def top_performers_in_each_metric(year):
    metrics = ["TLR", "RP", "GO", "OI", "PR"]
    for metric in metrics:
        st.write(f"Top 10 performers in {metric} for the year {year}:")
        result = load_datasets(year, metric)
        if result is not None:
            top_10_result = dict(list(result.items())[:10])
            display_rankings(top_10_result)
            plot_top_10(top_10_result)
        else:
            st.write(f"No data available for {metric} in the year {year}")

# Function to display rankings in a table
def display_rankings(result_dict):
    df = pd.DataFrame(list(result_dict.items()), columns=['UniversityName', 'Total'])
    st.table(df)

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



