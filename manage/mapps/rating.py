import streamlit as st
import os
def app():
    st.subheader("Rate Us..!")
    name=st.text_input("Enter your Name:")
    branch=st.text_input("Enter your Branch:",value="ECE")
    stars = ["select",'⭐️',"⭐️⭐️","⭐️⭐️⭐️","⭐️⭐️⭐️⭐️","⭐️⭐️⭐️⭐️⭐️"]
    selected_star = st.selectbox('Rate this app:', options=stars)
    btn=st.button("Submit")
    feedback_style = """
                <style>
                .feedback-box {
                    border: 2px solid #4CAF50;
                    border-radius: 10px;
                    background-color: #f9f9f9;
                    padding: 15px;
                    margin-bottom: 10px;
                }
    
                .feedback-title {
                    font-weight: bold;
                    color: #333;
                    font-size: 18px;
                }
    
                .feedback-content {
                    color: #666;
                    font-size: 16px;
                }
                </style>
                """
    st.markdown(feedback_style, unsafe_allow_html=True)
    FEEDBACK_FILE="ratings.txt"
    def append_feedback(feedback):
        # Check if the file exists
        if os.path.exists(FEEDBACK_FILE):
            with open(FEEDBACK_FILE, 'r',encoding="utf-8") as file:
                existing_feedbacks = file.read()
        else:
            existing_feedbacks = ""

        # Write the new feedback at the top of the file
        with open(FEEDBACK_FILE, 'w',encoding="utf-8") as file:
            file.write(feedback + "\n" + existing_feedbacks)

    if btn:
        if selected_star!="select":
            if name !="" and branch!="":
               append_feedback(f'["{name}" ,"From {branch} Rated this app {selected_star} stars!"]')




    st.header("User Feedbacks")

    if os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, 'r',encoding="utf-8") as file:
            feedbacks = file.readlines()
            for feedback in feedbacks:
                feed_list=eval(feedback)
                st.markdown(f"""
        <div class="feedback-box">
            <div class="feedback-title">{feed_list[0]}</div>
            <div class="feedback-content">{feed_list[1]}</div>
        </div>
        """, unsafe_allow_html=True)
