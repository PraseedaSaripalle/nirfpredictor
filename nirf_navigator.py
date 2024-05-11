import streamlit as st

def project_showcase():
    # Table of contents
    toc = {
        'Step 1: Automating Image Downloading': 1,
        'Step 2: Converting Images to Text Data': 2,
        'Step 3: Visualization Dashboard': 3,
        'Step 4: Correlation Analysis': 4,
        'Step 5: Categorization': 5,
        'Step 6: Prediction': 6,
        'Step 7: ChatBot': 7,
        'Understanding NIRF Ranking': 8
    }

    # Add a title and brief description of your project
    st.header('Project Title: AI Assistant for Bechmarking and Comparative Analysis for NIRF Ranking ')
    st.write("""
    Welcome to the showcase of our project! We've developed an AI Assistant that automates benchmarking and comparative analysis for
             NIRF Ranking, enhancing efficiency and accuracy in educational institution assessment.
    """)
      # Display a table with project features
    feature_table_data = {
        'Feature': ['Automating Image Downloading', 'Converting Images to Text Data', 'Visualization Dashboard',
                    'Correlation Analysis', 'Categorization', 'Prediction', 'ChatBot', 'Understanding NIRF Ranking'],
        'Description': [
            'Automates the process of downloading images from the web to the local system.',
            'Reads image data and converts it into text data. This process is automated to form a dataset.',
            'Provides interactive visualizations to explore the dataset comprehensively.',
            'Identifies correlations within the dataset.',
            'Organizes data into meaningful groups.',
            'Utilizes machine learning algorithms to predict outcomes based on the dataset.',
            'Interacts with the system using a ChatBot feature.',
            'Ranks higher educational institutions based on various parameters such as teaching, learning, resources, research, etc.'
        ]
    }

    st.table(feature_table_data)

    # Create a slider for navigation
    selected_section = st.sidebar.select_slider('Navigate to:', options=list(toc.keys()))

    # Display the selected section
    if selected_section:
        section_number = toc[selected_section]
        st.sidebar.slider('Navigate:', min_value=1, max_value=len(toc), value=section_number, step=1)
        st.markdown("---")
        for section_title, number in toc.items():
            if section_number == number:
                st.markdown(f"## {section_title}")
                if section_number == 1:
                    st.write("""
                    Our project starts with automating the process of downloading images from the web to your local system. 
                    This ensures a seamless collection of data for analysis.
                    """)
                elif section_number == 2:
                    st.write("""
                    Once the images are downloaded, we read the image data and convert it into text data. 
                    This process is repeated for multiple images to form a dataset. All of this is automated to save time and effort.
                    """)
                elif section_number == 3:
                    st.write("""
                    Visualizing data is crucial for understanding patterns and trends. Our dashboard provides interactive visualizations 
                    to explore the dataset comprehensively.
                    """)
                elif section_number == 4:
                    st.write("""
                    Understanding the relationships between different variables is essential. Our correlation analysis feature helps 
                    in identifying correlations within the dataset.
                    """)
                elif section_number == 5:
                    st.write("""
                    Categorizing data can simplify complex datasets. Our categorization feature helps in organizing data into 
                    meaningful groups.
                    """)
                elif section_number == 6:
                    st.write("""
                    Predictive analytics plays a crucial role in decision-making. Our prediction feature utilizes machine learning 
                    algorithms to predict outcomes based on the dataset.
                    """)
                elif section_number == 7:
                    st.write("""
                    Interacting with the system is made easy with our ChatBot feature. Ask questions, get insights, and explore 
                    the capabilities of our project effortlessly.
                    """)
                elif section_number == 8:
                    st.write("""
                    NIRF stands for National Institutional Ranking Framework, which is an initiative by the Ministry of Education, 
                    Government of India, to rank higher educational institutions in India based on various parameters such as 
                    teaching, learning, resources, research, and more. The rankings provide valuable insights into the performance 
                    and quality of educational institutions across the country.
                    """)


