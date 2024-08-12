import streamlit as st
from gpt_data import get
from interface import main
from streamlit_option_menu  import option_menu
from interface import UserFace
def app():
    cnt2=0
    st.title("Computers")
    if "cse" not in st.session_state:
        st.session_state.cse = None

    if cnt2==0:
        sh=st.text_input("Enter Any sub-hedder from chapters:")
        if sh!='':
            st.session_state.cse=sh

    if "cmsg" not in st.session_state:
        st.session_state.cmsg = []
    if st.session_state.cse is not None:
        prompt=f"""you are a Computer science and engineers assistant of ecet preparation aspirant,give detailed information and give possible examples on the specified topic.
        The topic is: "{st.session_state.cse}"
        use your entire knowlade on ecet, and give only ecet related only.
        if the topic is not relateted to computer,programming,databases or subject etc, then specify to user that,"sorry it is not related to any chapter in computers,enter correct one."
        """

        data2=get(prompt)
        cdata=data2
        if data2:
            st.session_state.cmsg.append(data2)
            st.text_area("Generated Text", value=st.session_state.cmsg[-1], height=400)
        ask = option_menu(menu_title="",options=["select","Ask followUp"])
        if ask=="Ask followUp":
            cnt2=1
            main(cdata)
            UserFace.clear_data(cnt2)
