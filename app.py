import os
import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image



def main():
    st.title("Welcome to Electrical Electronics Engineering Resource Net (ELECRESOURCENET)")
    menu_options = {
        "About the App": about_app,
        "Document Resources": student_resources,
        "Time Table": timetable,
        "Graph Plotter": graph_plotter,
        "Events & News": events_news
    }

    selected_option = st.sidebar.radio("Menu", list(menu_options.keys()), index=0, help="Select a menu option",
                                       key="menu")

    if selected_option:
        st.sidebar.markdown(
            """<script>
            document.addEventListener('DOMContentLoaded', function() {
                const main = document.querySelector('.sidebar .block-container');
                const items = main.querySelectorAll('.block');

                items.forEach(item => {
                    item.addEventListener('click', function() {
                        main.style.display = 'none';
                    });
                });
            });
            </script>""",
            unsafe_allow_html=True
        )
        st.sidebar.markdown("---")
        menu_options[selected_option]()

def about_app():
    st.set_page_config(page_title="Welcome to University of Jos", page_icon=":school:")

    # Load and resize the logo-=
    logo = Image.open("images/unijos_logo.jfif")
    logo_resized = logo.resize((150, 150))  # Adjust the dimensions as needed
    st.image(logo_resized, use_column_width=False)  # Set use_column_width to False to maintain the specified dimensions

    st.title("Welcome to Electrical Electronics Engineering Resource Net (ELECRESOURCENET)")

    # Custom CSS to style the sidebar
    st.markdown(
        """
        <style>
        .sidebar .sidebar-content {
            background-color: skyblue;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.write("## About the App")
    st.write("ELECRESOURCENET is a Python-based web application designed to serve the Electrical Electronics Engineering (EEE) department at the University of Jos. Its primary goal is to provide a centralized platform for students and faculty members to access educational resources, manage timetables, and stay updated on the latest news and technological advancements in the field.")
    st.write("## Key features of ELECRESOURCENET include:")
    st.write("### Resource Upload")
    st.write("Students can easily upload resources such as PDF documents, lecture notes, and supplementary materials related to their coursework. This feature promotes knowledge sharing and collaboration among students and faculty members.")
    st.write("### Timetable Generation")
    st.write("The application offers a convenient way to generate timetables for courses and academic activities. Users can input course schedules, lecture timings, and other relevant information to create personalized timetables tailored to their academic needs.")
    st.write("### Graph Plotter")
    st.write("Easily plot graphs and visualize data with ELECRESOURCENET's graph plotting capabilities. Users can input data points and choose the type of graph (e.g., line plot, scatter plot) to generate. Additionally, the application provides functionalities to calculate slope, intercept, and other relevant parameters for the plotted graph.")
    st.write("### Real-time News Updates")
    st.write("ELECRESOURCENET provides access to real-time news and updates related to the Electrical Electronics Engineering field. Users can stay informed about industry trends, research developments, and technological innovations, enhancing their learning experience and professional growth.")
    st.write(" Overall, ELECRESOURCENET serves as a comprehensive platform that integrates educational resources, scheduling tools, and news updates to support the academic and professional endeavors of students and faculty members in the EEE department at the University of Jos.")


# Document Resources Code
# Function to handle file upload
def upload_file():
    uploaded_file = st.file_uploader("Choose a file", type=['pdf', 'txt', 'docx', 'pptx', 'xlsx', 'jpg', 'jpeg',
                                                            'png'])  # Add image formats
    if uploaded_file is not None:
        with open(os.path.join("uploads", uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success("File uploaded successfully!")


# Function to handle file download
def download_file(file_path):
    with open(file_path, "rb") as f:
        file_content = f.read()
    st.download_button(label="Download File", data=file_content, file_name=os.path.basename(file_path))


def student_resources():
    st.write("## Student Resources")
    st.write("### Upload Resources")
    upload_file()

    st.write("### Download Resources")
    resource_files = os.listdir("uploads")

    # Search bar
    search_query = st.text_input("Search uploaded files:", "")

    # Filter files based on search query
    filtered_files = [file for file in resource_files if search_query.lower() in file.lower()]

    if filtered_files:
        selected_file = st.selectbox("Select a file to download", filtered_files, index=0)
        if selected_file:
            file_path = os.path.join("uploads", selected_file)
            download_file(file_path)
    else:
        st.write("No files found matching the search criteria.")


# Create uploads directory if it doesn't exist
if not os.path.exists("uploads"):
    os.makedirs("uploads")

# Tech News Code
def events_news():
    st.write("## Events & News")
    display_tech_news()
def fetch_tech_news():
    # Provide your News API key
    NEWS_API_KEY = '0eb5fd64355e4a78868ca7a097398d56'

    # Set parameters for fetching tech news
    params = {
        'apiKey': NEWS_API_KEY,
        'category': 'Science',
        'language': 'en',
        'pageSize': 10  # Number of articles to fetch
    }

    # Make request to News API
    response = requests.get('https://newsapi.org/v2/top-headlines', params=params)

    # Parse response and extract articles
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        return articles
    else:
        return []

# Function to display technology news articles
def display_tech_news():
    st.write("## Science & Tech News")
    articles = fetch_tech_news()
    if articles:
        for article in articles:
            st.write(f"**{article['title']}**")
            # Check if 'urlToImage' exists and is not None
            if 'urlToImage' in article and article['urlToImage']:
                st.image(article['urlToImage'], caption='Image associated with the article', use_column_width=True)
            else:
                st.write("No image available.")
            st.write(f"Source: {article['source']['name']}")
            st.write(f"Published at: {article['publishedAt']}")
            st.write(article['description'])
            st.write(f"[Read more]({article['url']})")  # Create clickable "Read more" link
            st.write("---")
    else:
        st.error("Failed to fetch news. Please try again later.")

# Example usage in Streamlit app



# Time Table

def create_timetable():
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    hours = [f"{hour}:00" for hour in range(8, 18)]
    timetable = pd.DataFrame(index=weekdays, columns=hours)

    for day in weekdays:
        for hour in hours:
            subject = st.text_input(f"Enter subject for {day}, {hour}:")
            timetable.loc[day, hour] = subject
    return timetable


def save_timetable(timetable):
    timetable.to_csv("timetable.csv")
    st.success("Timetable saved successfully!")


def timetable():
    st.title("Timetable Creator")
    st.write(
        "Please enter subjects for each hour from 8:00 AM to 6:00 PM (1-hour interval) for each weekday (Monday to Saturday).")
    timetable = create_timetable()
    st.write("## Timetable")

    # Apply CSS to make cells responsive
    st.markdown(
        """
        <style>
        .dataframe tbody tr th {
            word-wrap: break-word;
            overflow-wrap: break-word;
            word-break: break-all;
        }
        .dataframe thead th {
            word-wrap: break-word;
            overflow-wrap: break-word;
            word-break: break-all;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.dataframe(timetable)

    if st.button("Save Timetable"):
        save_timetable(timetable)

# Graph Plotter Code
def plot_graph(x, y, xlabel, ylabel):
    # Fit a linear regression line
    slope, intercept = np.polyfit(x, y, 1)
    regression_line = slope * np.array(x) + intercept

    # Plot the graph
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(x, y, marker='o', linestyle='', label='Data')

    # Adjust regression line to touch the axes
    ax.plot([min(x), max(x)], [min(x) * slope + intercept, max(x) * slope + intercept], color='red', linestyle='-',
            label='Regression Line')

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title("Plot of Data with Regression Line")
    ax.grid(True)
    ax.legend()

    # Annotate the slope and intercept on the plot
    ax.annotate(f'Slope: {slope:.2f}', xy=(0.5, 0.9), xycoords='axes fraction', fontsize=12, color='red')
    ax.annotate(f'Intercept: {intercept:.2f}', xy=(0.5, 0.8), xycoords='axes fraction', fontsize=12, color='red')

    # Show plot
    st.pyplot(fig)


def graph_plotter():
    st.title("Graph Plotter with Slope Calculation")

    # Input data
    st.write("Enter the values to plot the graph:")
    x_values = st.text_input("Enter x values (comma-separated)", help="Example: 1, 2, 3")
    y_values = st.text_input("Enter y values (comma-separated)", help="Example: 4, 5, 6")

    # X and Y axis labels
    xlabel = st.text_input("Enter x-axis label", help="Example: Time")
    ylabel = st.text_input("Enter y-axis label", help="Example: Temperature")

    # Plot button
    if st.button("Plot Graph"):
        # Convert input strings to lists of floats
        x_values = [float(x.strip()) for x in x_values.split(",")]
        y_values = [float(y.strip()) for y in y_values.split(",")]

        # Check if the lengths of x and y match
        if len(x_values) != len(y_values):
            st.error("Error: Lengths of x and y values should be the same.")
        else:
            # Plot the graph
            plot_graph(x_values, y_values, xlabel, ylabel)


if __name__ == "__main__":
    main()