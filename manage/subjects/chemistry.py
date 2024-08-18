import streamlit as st
from gpt_data import get
from interface import main
from streamlit_option_menu  import option_menu
from interface import UserFace
def app():
    cnt=0
    st.title("chemistry")
    if "content" not in st.session_state:
        st.session_state.content = None

    if cnt==0:
        sh=st.text_input("Enter Any sub-hedder from chapters:")
        if sh!='':
            st.session_state.content=sh

    if "message" not in st.session_state:
        st.session_state.message = []
    if st.session_state.content is not None:
        prompt=f"""you are a chemistry assistant of ecet preparation aspirant,give detailed information and give possible examples on the specified topic.give only useful information avoid giving much matter.
        The topic is: "{st.session_state.content}"
        use your entire knowlade on ecet, and give only ecet related only.
        if the topic is not relateted to chemistry or subject  then specify to user that,"sorry it is not related to any chapter in chemistry,enter correct one."
        """

        data=get(prompt)
        ndata=data
        if data:
            st.session_state.message.append(data)
            st.text_area("Generated Text", value=st.session_state.message[-1], height=400)
        ask = option_menu(menu_title="",options=["select","Ask followUp"])
        if ask=="Ask followUp":
            cnt=1
            main(ndata)
            UserFace.clear_data(cnt)
