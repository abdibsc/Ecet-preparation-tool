import streamlit as st
from streamlit_option_menu import option_menu
from subjects import chemistry, physics,maths,electronics_sub
from mapps import papers

def app():

    # Check if a subject is already selected
    if "selected_subject" not in st.session_state:
        st.session_state.selected_subject = None

    # Show the menu only if no subject has been selected yet
    if st.session_state.selected_subject is None:
        sub = option_menu(
            menu_title="Choose Subject here",
            options=["select","Chemistry", "Physics", "Maths", "Electronics","Previous Papers"],
            menu_icon="book-fill",
            default_index=0
        )

        if sub!="select":
            st.session_state.selected_subject = sub

    # Based on the selected subject, display the corresponding app
    if st.session_state.selected_subject == "Chemistry":
        chemistry.app()
    elif st.session_state.selected_subject == "Physics":
        physics.app()
    elif st.session_state.selected_subject == "Maths":
        maths.app()
    elif st.session_state.selected_subject == "Electronics":
        electronics_sub.app()
    elif st.session_state.selected_subject=="Previous Papers":
        papers.ece()
    # Add a reset button to clear the selection and show the menu again
    if st.session_state.selected_subject is not None:
        if st.button("Choose Another Subject"):
            st.session_state.selected_subject = None


if __name__ == "__main__":
    app()

