import google.generativeai as genai
import streamlit as st
from PIL import Image


def main():
    st.set_page_config(page_title="Welcome to University of Jos", page_icon=":rocket:")

    # Load and resize the logo-=
    logo = Image.open("images/unijos_logo.jfif")
    logo_resized = logo.resize((150, 150))  # Adjust the dimensions as needed
    st.image(logo_resized, use_column_width=False)  # Set use_column_width to False to maintain the specified dimensions

    st.title("Welcome to Electrical Electronics Engineering Department")

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

    menu_options = {
        "About Us": about_us,
        "Programs": programs,
        "Faculty & Staff": faculty_staff,
        "Research & Innovation": research_innovation,
        "Student Resources": student_resources,
        "Events & News": events_news,
        "Contact Us": contact_us,
        "AI": {
            "AI PowerPoint": ai_powerpoint,
            "AI Chat": ai_chat
        }
    }

    selected_option = st.sidebar.radio("Menu", list(menu_options.keys()), index=0, help="Select a menu option", key="menu")

    if selected_option == "AI":
        selected_sub_option = st.sidebar.radio("Sub-menu", list(menu_options["AI"].keys()), index=0, help="Select a sub-menu option", key="ai_submenu")
        if selected_sub_option:
            st.markdown("---")
            menu_options["AI"][selected_sub_option]()
    elif selected_option:
        st.markdown("---")
        menu_options[selected_option]()

def about_us():
    st.write("## About Us")
    st.write("Welcome to the Department of Electrical and Electronic Engineering at the University of Jos! We are committed to excellence in education, research, and innovation in the field of electrical and electronics engineering. Let us introduce ourselves:")
    st.write("## Our Vision")
    st.write("Our vision is to be a leading center of excellence in electrical and electronic engineering education, research, and community service. We strive to produce graduates who are well-equipped to address real-world challenges and contribute to technological advancements.")
    st.write("## Our Mission")
    st.write("Our mission is to:")
    st.write("Educate: We provide high-quality education to our students, equipping them with the knowledge, skills, and ethical values necessary for successful careers in electrical and electronic engineering.")
    st.write("Research: We engage in cutting-edge research across various domains, including renewable energy, telecommunications, automation, and control systems. Our faculty members actively contribute to scientific advancements and collaborate with industry partners.")
    st.write("Innovate: We foster innovation and creativity among our students. Whether it’s designing circuits, developing software, or solving complex engineering problems, we encourage out-of-the-box thinking.")
    st.write("## Why Choose Us?")
    st.write("Expert Faculty: Our dedicated faculty members bring a wealth of experience and expertise to the classroom. They are passionate about teaching and mentoring students.")
    st.write("State-of-the-Art Facilities: Our department is equipped with modern laboratories, simulation tools, and resources that allow students to gain practical experience.")
    st.write("Industry Connections: We maintain strong ties with industry partners, ensuring that our curriculum aligns with real-world requirements. Internships, guest lectures, and industrial visits are integral parts of our programs.")
    st.write("Research Opportunities: Students have the chance to participate in research projects, collaborate with faculty, and contribute to scientific advancements.")

def programs():
    st.write("## Programs Offered")
    st.write("We offer a range of programs, including:")
    st.write("### Bachelor of Engineering (B.Eng.) in Electrical and Electronic Engineering:")
    st.write(" A comprehensive undergraduate program that covers fundamental principles, advanced topics, and practical applications.")
    st.write("### Master of Science (M.Sc.) in Electrical and Electronic Engineering:")
    st.write(" For those seeking specialized knowledge and research opportunities.")
    st.write("### Doctor of Philosophy (Ph.D.) in Electrical and Electronic Engineering:")
    st.write(" Our doctoral program encourages original research and scholarly contributions.")
    # Add content for Programs section

def faculty_staff():
    st.write("## Faculty & Staff")
    # Add content for Faculty & Staff section

def research_innovation():
    st.write("## Research & Innovation")
    # Add content for Research & Innovation section

def student_resources():
    st.write("## Student Resources")
    # Add content for Student Resources section

def events_news():
    st.write("## Events & News")
    # Add content for Events & News section

def contact_us():
    st.write("## Contact Us")
    # Add content for Contact Us section

def ai_powerpoint():
    st.write("## AI PowerPoint")
    # Add content for AI PowerPoint section

def ai_chat():
    st.write("## AI Chat")

    # Configure the API key
    API_KEY = 'AIzaSyDjhKotr-RgmQrGIDwIpixrtNWUZiV-0u0'
    genai.configure(api_key=API_KEY)

    # Initialize the Generative AI model
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])
    instruction = "In this chat, respond in Electrical and Electronics Engineering terms."

    # Initialize force_send if it doesn't exist
    if "force_send" not in st.session_state:
        st.session_state.force_send = False

    # Initialize counter for generating unique keys
    if "input_question_counter" not in st.session_state:
        st.session_state.input_question_counter = 0

    # Chat loop
    while True:
        # Generate a unique key for text input
        question_key = f"input_question_{st.session_state.input_question_counter}"
        question = st.text_input("You:", key=question_key)

        if st.button("Send") or st.session_state.force_send:
            st.session_state.force_send = False
            if question.strip() == '':
                break

            response = chat.send_message(instruction + question)
            st.write(f"Bot: {response.text}")

if __name__ == "__main__":
    main()