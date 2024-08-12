import streamlit as st
from gpt_data import get
from interface import main
from streamlit_option_menu  import option_menu
from interface import UserFace
def app():
    cnt5=0
    st.title("Electronics")
    if "ece_sub" not in st.session_state:
        st.session_state.ece_sub = None

    if cnt5==0:
        sh=st.text_input("Enter Any sub-hedder from chapters:")
        if sh!='':
            st.session_state.ece_sub=sh

    if "ece_msg" not in st.session_state:
        st.session_state.ece_msg = []
    if st.session_state.ece_sub is not None:
        prompt=f"""you are a Electronics and communication Engineering student assistant of ecet preparation aspirant,give detailed information and give possible examples on the specified topic.
        The topic is: "{st.session_state.ece_sub}"
        use your entire knowlade on ecet, and give only ecet related only.
        if the topic is not relateted to Electronics and Communication engineering like sattilite communication,electronics,power circuits etc related subjects  then specify to user that,"sorry it is not related to any chapter in Electronics and communication engineering,enter correct one."
        """

        data5=get(prompt)
        ecdata=data5
        if data5:
            st.session_state.ece_msg.append(data5)
            st.text_area("Generated Text", value=st.session_state.ece_msg[-1], height=400)
        ask4 = option_menu(menu_title="",options=["select","Ask followUp"])
        if ask4=="Ask followUp":
            cnt5=1
            main(ecdata)
            UserFace.clear_data(cnt5)