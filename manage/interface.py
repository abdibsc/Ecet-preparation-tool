# chat_interface.py

import streamlit as st
from gpt_data import get

class UserFace:
    def __init__(self):
        self.initialize_session()
    def initialize_session(self):
        if 'messages' not in st.session_state:
            st.session_state.messages = []
        if 'recent_conversations' not in st.session_state:
            st.session_state.recent_conversations = []
    def clear_data(num):
        st.session_state.messages.clear()
        #st.session_state.recent_conversations.clear()
    def display_chat(self):
        for message in st.session_state.messages:
            role = message.get("role")
            with st.chat_message(role):
                st.write(message.get("content"))

    def get_last_n_conversations(self,n=3):
        # Get the last n conversations (each conversation includes a user and assistant message)
        if len(st.session_state.messages) < 2 * n:
            return st.session_state.messages
        else:
            return st.session_state.messages[-(2 * n):]
    def handle_input(self,add_info=None):
        if add_info:
            st.session_state.messages.append({"role":"assistant","content":add_info})
        prompt = st.chat_input("Ask me")
        if prompt:
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.session_state.recent_conversations = self.get_last_n_conversations(n=3)

            # Format the context for the chatbot
            context = "\n".join([f"{msg['role']}: {msg['content']}" for msg in st.session_state.recent_conversations])

            # Get bot response using the context
            response = get(f"{context}\nuser: {prompt}")
            with st.chat_message("user"):
                st.write(prompt)
            st.session_state.messages.append({"role": "assistant", "content": response})
            with st.chat_message("assistant"):
                st.markdown(response)

def main(add_info=None):
    #st.set_page_config(page_title="Chat Interface")
    user_face = UserFace()
    user_face.initialize_session()
    user_face.display_chat()
    user_face.handle_input(add_info)


