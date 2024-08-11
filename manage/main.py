import streamlit as st
from mapps import electronics,cse,civil,home,mech,eee
from streamlit_option_menu import option_menu
st.set_page_config(page_title="ecet prep tool")
st.title("SuRaj ECET preparation Tool")
class MultiApp:
    def __init__(self):
        self.apps=[]
    def add_apps(self,title,function):
        self.apps.append({
            "title":title,
            "function":function
        })
    def run(self):
        with st.sidebar:
            app=option_menu(
                menu_title="choose your Bracnch",
                options=["Home","Electronics","Computers","Civil","Mech","EEE"],
                icons=["house-fill"],
                menu_icon="chat-text-fill",
                default_index=0
            )
            st.write("Note:Please click 2 times to take right action")
        if app=="Home":
            home.app()
        if app=="Electronics":
            electronics.app()
        if app=="Computers":
            cse.app()
        if app=="Civil":
            civil.app()
        if app=="Mech":
            mech.app()
        if app=="EEE":
            eee.app()
    run(self=None)
