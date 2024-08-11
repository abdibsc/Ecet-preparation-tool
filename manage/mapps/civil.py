import streamlit as st
from streamlit_option_menu import option_menu
from subjects import chemistry, physics,maths


def app():
    # Check if a subject is already selected
    if "subject" not in st.session_state:
        st.session_state.subject = None

    # Show the menu only if no subject has been selected yet
    if st.session_state.subject is None:
        sub = option_menu(
            menu_title="Choose Subject here",
            options=["select","Chemistry", "Physics", "Maths", "Civil"],
            menu_icon="book-fill",
            default_index=0
        )

        if sub!="select":  # Update the session state when a subject is selected
            st.session_state.subject = sub

    # Based on the selected subject, display the corresponding app
    if st.session_state.subject == "Chemistry":
        chemistry.app()
    elif st.session_state.subject == "Physics":
        physics.app()
    elif st.session_state.subject == "Maths":
        maths.app()
    elif st.session_state.subject == "Civil":
        # Placeholder for Electronics app
        st.write("Civil app is under construction.")

    # Add a reset button to clear the selection and show the menu again
    if st.session_state.subject is not None:
        if st.button("Choose Another Subject"):
            st.session_state.subject = None


if __name__ == "__main__":
    app()

