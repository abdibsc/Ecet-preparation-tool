import streamlit as st
from gpt_data import get
from interface import main
from streamlit_option_menu import option_menu
from interface import UserFace

def app():
    # Initialize cnt in session state to persist between reruns
    if "cnt" not in st.session_state:
        st.session_state.cnt = 0

    st.title("Chemistry")

    # Reset content when "Ask followUp" is clicked
    if st.session_state.cnt == 1:
        st.session_state.clear()
        st.session_state.cnt = 0
        st.experimental_rerun()  # Force a rerun to clear the screen

    # Check if 'content' is in session state
    if "content" not in st.session_state:
        st.session_state.content = None

    # User input for sub-header
    if st.session_state.cnt == 0:
        sh = st.text_input("Enter Any sub-header from chapters:")
        if sh:
            st.session_state.content = sh

    # Check if 'message' is in session state
    if "message" not in st.session_state:
        st.session_state.message = []

    # If content is available, generate and display the information
    if st.session_state.content is not None:
        prompt = f"""You are a chemistry assistant of ECET preparation aspirant. Give detailed information and provide possible examples on the specified topic. The topic is: "{st.session_state.content}" Use your entire knowledge on ECET and give only ECET-related information. If the topic is not related to chemistry, specify that it is not related to any chapter in chemistry."""
        
        data = get(prompt)
        if data:
            st.session_state.message.append(data)
            st.text_area("Generated Text", value=st.session_state.message[-1], height=400)

    # Option menu for follow-up
    ask = option_menu(menu_title="", options=["Select", "Ask followUp"])

    if ask == "Ask followUp":
        st.session_state.cnt = 1
        st.experimental_rerun()  # Force a rerun to clear the screen
        main(data)
        UserFace.clear_data(st.session_state.cnt)
