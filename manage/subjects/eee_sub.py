import streamlit as st
from gpt_data import get
from interface import main
from streamlit_option_menu  import option_menu
from interface import UserFace
def app():
    cnt6=0
    st.title("Electrical")
    if "eee_sub" not in st.session_state:
        st.session_state.eee_sub = None

    if cnt6==0:
        sh=st.text_input("Enter Any sub-hedder from chapters:")
        if sh!='':
            st.session_state.eee_sub=sh

    if "eee_msg" not in st.session_state:
        st.session_state.eee_msg = []
    if st.session_state.eee_sub is not None:
        prompt=f"""you are a Electrical and Electronics Engineering student assistant of ecet preparation aspirant,give detailed information and give possible examples on the specified topic.
        The topic is: "{st.session_state.eee_sub}"
        use your entire knowlade on ecet, and give only ecet related only.
        if the topic is not relateted to Electronics and Electrical engineering like electrical,power etc related subjects  then specify to user that,"sorry it is not related to any chapter in EEE engineering,enter correct one."
        """

        data=get(prompt)
        ndata=data
        if data:
            st.session_state.eee_msg.append(data)
            st.text_area("Generated Text", value=st.session_state.eee_msg[-1], height=400)
        ask6 = option_menu(menu_title="",options=["select","Ask followUp"])
        if ask6=="Ask followUp":
            cnt6=1
            main(ndata)
            UserFace.clear_data(cnt6)