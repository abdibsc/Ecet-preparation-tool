import streamlit  as st
import random
def app():
    st.subheader("Let's start preparation with AI")
    colors = [
    "#FFFFFF",  # White
    "#D3D3D3",  # Light Gray
    "#00FFFF",  # Cyan
    "#7DF9FF",  # Electric Blue
    "#FFA500",  # Orange
    "#FFFF00",  # Yellow
    "#32CD32",  # Lime Green
    "#FF00FF",  # Magenta
    "#FFD700",  # Gold
    "#FF4500",  # Red
    "#8A2BE2",  # Blue Violet
    "#FF1493",  # Deep Pink
    "#40E0D0",  # Turquoise
    "#DC143C",  # Crimson
    "#00FF7F",  # Spring Green
    "#1E90FF",  # Dodger Blue
    "#FF8C00",  # Dark Orange
    "#B22222",  # Firebrick
    "#ADFF2F",  # Green Yellow
    "#DA70D6"   # Orchid
    ]
    color = random.choice(colors)
    st.write(f"<h2 style='text-align: left;color: {color};font-size:15px;'>NOTE: Use Desktop Site in mobile for better experience.</h2>", unsafe_allow_html=True)
    st.write("""Welcome to your one-stop solution for preparing for the ECET exam! 
    Our platform is designed to help you excel in your chosen branch by providing easy access to subjects,
    study material, and an interactive AI-powered chatbot to assist with your queries.""")
    st.subheader("Chat With AI")
    st.write("Previous ECET questions Finder..")
    st.write("At your finger tips")
    st.link_button("Ecet qus Finder", "https://www.stack-ai.com/chat-assistant/bd4861f8-a9f9-4e41-aa4c-60c433d942c1/9139a0ba-3f45-416f-9ece-805c64ff2c80/6709520d7ad920be253c10ce")
    st.subheader("What is in this app.?")
    st.write(f"<h3 style='text-align: left;color:white;font-size:20px;'>Preparation Road Map.</h3>", unsafe_allow_html=True)
    st.write(f"<h4 style='text-align: left;color:white;font-size:20px;'>Q&A with choosen Subject.</h4>", unsafe_allow_html=True)
    st.write(f"<h5 style='text-align: left;color:white;font-size:20px;'>AI Chat for Doubt clarification.</h5>", unsafe_allow_html=True)
    st.write(f"<h6 style='text-align: left;color:white;font-size:20px;'>previous Question papers.</h6>", unsafe_allow_html=True)
    st.write(f"<h2 style='text-align: left;color:white;font-size:20px;'>Best learning Path way.</h2>", unsafe_allow_html=True)
    st.write(f"<h2 style='text-align: left;color:white;font-size:20px;'>Rate us your experience!</h2>", unsafe_allow_html=True)
    st.subheader("Choose Your Branch")
    st.write("""Get started by selecting your branch. Whether you're in ECE, CIVIL, MECH, CSE, or EEE, our tool allows you to explore the subjects relevant to your field. Simply click on your branch to view the subjects and begin your preparation.""")
    st.subheader("Ask Questions and Chat with AI")
    st.write("""- *Stuck on a topic?*
    - *Have a specific question? Our AI chatbot is here to help!*
    You can ask questions about your subjects and receive detailed answers,
    or simply chat with the AI to get more information and tips on how to prepare effectively.""")
    st.subheader("Benefits of Using the ECET Preparation Tool")
    st.write("""- *Comprehensive Coverage:* The tool covers all the necessary subjects for each branch, ensuring that students have access to the full spectrum of topics they need to study.
- *Interactive Learning:* The AI chatbot provides an interactive learning experience, making it easier for students to engage with complex topics and clarify their doubts.
- *Time Management:* The tool’s organized structure and personalized study tips help students manage their time effectively, which is crucial for exam preparation.""")







