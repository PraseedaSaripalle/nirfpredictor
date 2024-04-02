import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_datasets(year):
    file_path = f"D:/BTech/Major_Project_2024Jan/Data/{year}.csv"  # Adjust the path as per your file location
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    return None

def corr(year):
    sub_options = {
    "Correlation Between Teaching Learning Resources and Research Professional Practice": {
        "set1": ['SSValue', 'FSRValue', 'FQEValue', 'FRUValue'],
        "set2": ['PUValue', 'QPValue', 'IPRValue', 'FPPPValue']
    },
    "Correlation Between Teaching Learning Resources and Graduation Outcomes": {
        "set1": ['SSValue', 'FSRValue', 'FQEValue', 'FRUValue'],
        "set2": ['GUEValue', 'MSValue', 'GPHDValue']
    },
    "Correlation Between Teaching Learning Resources and Outreach Inclusivity": {
        "set1": ['SSValue', 'FSRValue', 'FQEValue', 'FRUValue'],
        "set2": ['RDValue', 'wDValue', 'ESCSValue', 'PcsValue']
    },
    "Correlation Between Teaching Learning Resources and Perception": {
        "set1": ['SSValue', 'FSRValue', 'FQEValue', 'FRUValue'],
        "set2": ['PRValue']
    },
    "Correlation Between Research Professional Practice and Graduation Outcomes": {
        "set1": ['PUValue', 'QPValue', 'IPRValue', 'FPPPValue'],
        "set2": ['GUEValue', 'MSValue', 'GPHDValue']
    },
    "Correlation Between Research Professional Practice and Outreach Inclusivity": {
        "set1": ['PUValue', 'QPValue', 'IPRValue', 'FPPPValue'],
        "set2": ['RDValue', 'wDValue', 'ESCSValue', 'PcsValue']
    },
    "Correlation Between Research Professional Practice and Perception": {
        "set1": ['PUValue', 'QPValue', 'IPRValue', 'FPPPValue'],
        "set2": ['PRValue']
    },
    "Correlation Between Graduation Outcomes and Outreach Inclusivity": {
        "set1": ['GUEValue', 'MSValue', 'GPHDValue'],
        "set2": ['RDValue', 'wDValue', 'ESCSValue', 'PcsValue']
    },
    "Correlation Between Graduation Outcomes and Perception": {
        "set1": ['GUEValue', 'MSValue', 'GPHDValue'],
        "set2": ['PRValue']
    },
    "Correlation Between Outreach Inclusivity and Perception": {
        "set1": ['RDValue', 'wDValue', 'ESCSValue', 'PcsValue'],
        "set2": ['PRValue']
    }
}
    selected_sub_option = st.radio("Select Sub-option", list(sub_options.keys()))

    df = load_datasets(year)  # Load dataset for the selected year

    # Strip whitespace from column names
    df.columns = df.columns.str.strip()

    set1 = sub_options[selected_sub_option]["set1"]
    set2 = sub_options[selected_sub_option]["set2"]

    # Calculate correlation matrix between the two sets
    correlation_matrix = df[set1 + set2].corr()

    # Visualize the correlation matrix using a heatmap
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5, ax=ax)
    ax.set_title('Correlation Matrix')
    st.pyplot(fig)
    
    # Interpret the correlation coefficients
    threshold = 0.5  # You can adjust this threshold based on your criteria

    for i in range(len(set1)):
        for j in range(len(set1), len(set1) + len(set2)):
            param1 = set1[i]
            param2 = set2[j - len(set1)]  # Adjust the index for set2
            correlation_coefficient = correlation_matrix.loc[param1, param2]

            if correlation_coefficient > threshold:
                st.write(f"{param1} and {param2} are positively correlated (Coefficient: {correlation_coefficient:.2f})")
            elif correlation_coefficient < -threshold:
                st.write(f"{param1} and {param2} are negatively correlated (Coefficient: {correlation_coefficient:.2f})")
            else:
                st.write(f"{param1} and {param2} have no significant correlation (Coefficient: {correlation_coefficient:.2f})")