import streamlit as st
from gpt_data import get
from interface import main
from streamlit_option_menu  import option_menu
from interface import UserFace
def app():
    cnt1=0
    st.title("Mathematics")
    if "data" not in st.session_state:
        st.session_state.data = None

    if cnt1==0:
        sh=st.text_input("Enter Any sub-hedder from chapters:")
        if sh!='':
            st.session_state.data=sh

    if "maths" not in st.session_state:
        st.session_state.maths = []
    if st.session_state.data is not None:
        prompt=f"""you are a Mathematics assistant of ecet preparation aspirant,give detailed information and give possible examples on the specified topic.
        The topic is: "{st.session_state.data}"
        use your entire knowlade on ecet, and give only ecet related only.give problem step by steps and explanation.
        if the topic is not relateted to Mathematics or subject  then specify to user that,"sorry it is not related to any chapter in Maths,enter correct one."
        """

        data1=get(prompt)
        mdata=data1
        if data1:
            st.session_state.maths.append(data1)
            st.text_area("Generated Text", value=st.session_state.maths[-1], height=400)
        ask1 = option_menu(menu_title="",options=["select","Ask for followUp"])
        if ask1=="Ask followUp":
            cnt1=1
            main(mdata)
            UserFace.clear_data(cnt1)
