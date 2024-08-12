import streamlit as st
from gpt_data import get
from interface import main
from streamlit_option_menu  import option_menu
from interface import UserFace

def app():
    cnt=0
    st.title("Physics")
    if "contents" not in st.session_state:
        st.session_state.contents = None

    if cnt==0:
        sh=st.text_input("Enter Any sub-hedder from chapters:")
    if sh!='':
        st.session_state.contents=sh

    if "messagee" not in st.session_state:
        st.session_state.messagee = []
    if st.session_state.contents is not None:
        prompt=f"""you are a Physics assistant of ecet preparation aspirant,give detailed information and give possible examples on the specified topic.
        The topic is: "{st.session_state.contents}"
        use your entire knowlade on ecet, and give only ecet related only.
        if the topic is not relateted to Physics or subject  then specify to user that,"sorry it is not related to any chapter in chemistry,enter correct one."
        """

        py_data=get(prompt)
        adata=py_data
        if py_data:
            st.session_state.messagee.append(py_data)
            st.text_area("Generated Text", value=st.session_state.messagee[-1], height=400)
        ask = option_menu(menu_title="",options=["select","Ask for followUp"])
        if ask=="Ask followUp":
            cnt=1
            main(adata)
            UserFace.clear_data(cnt)
