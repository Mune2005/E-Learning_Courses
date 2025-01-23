import streamlit as st
import openai
import pandas as pd

# Load course dataset
data = pd.read_csv(r"C:\Users\nothi\OneDrive\Desktop\AI-ML\AI-ML\All dataset\Coursera.csv")

# Initialize OpenAI API (Replace 'your-api-key' with your actual API key)
openai.api_key = 

# Function to generate course recommendations
def recommend_courses(query, n=5):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an assistant specialized in e-learning platforms."},
            {"role": "user", "content": f"Based on the dataset, recommend {n} courses for: {query}"}
        ]
    )
    return response['choices'][0]['message']['content']

# Function to summarize a course
def summarize_course(course_name):
    course_info = data[data['course'] == course_name]
    if course_info.empty:
        return "Course not found."
    details = course_info.iloc[0].to_dict()
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You summarize course details."},
            {"role": "user", "content": f"Summarize this course: {details}"}
        ]
    )
    return response['choices'][0]['message']['content']

# Function to answer user questions about e-learning
def answer_question(question):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert in e-learning platforms."},
            {"role": "user", "content": question}
        ]
    )
    return response['choices'][0]['message']['content']

# Streamlit App
st.title("E-Learning Assistant")
st.write("Ask questions, get course recommendations, or summarize courses interactively.")

# Sidebar options
option = st.sidebar.selectbox(
    "Choose an Action",
    ["Recommend Courses", "Summarize a Course", "Ask a Question"]
)

# Handle user input and display results based on the chosen action
if option == "Recommend Courses":
    query = st.text_input("Enter your area of interest (e.g., 'data science and machine learning'):")
    n = st.slider("Number of courses to recommend:", min_value=1, max_value=10, value=5)
    if st.button("Recommend"):
        if query:
            recommendations = recommend_courses(query, n)
            st.subheader("Recommended Courses:")
            st.write(recommendations)
        else:
            st.warning("Please enter a query.")

elif option == "Summarize a Course":
    course_name = st.text_input("Enter the course name to summarize:")
    if st.button("Summarize"):
        if course_name:
            summary = summarize_course(course_name)
            st.subheader("Course Summary:")
            st.write(summary)
        else:
            st.warning("Please enter a course name.")

elif option == "Ask a Question":
    question = st.text_input("Enter your question about e-learning:")
    if st.button("Ask"):
        if question:
            answer = answer_question(question)
            st.subheader("Answer:")
            st.write(answer)
        else:
            st.warning("Please enter a question.")
