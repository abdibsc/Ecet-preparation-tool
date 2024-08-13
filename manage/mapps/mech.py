import streamlit as st
from streamlit_option_menu import option_menu
from subjects import chemistry, physics,maths,mech_sub
from mapps import papers

def app():
    # Check if a subject is already selected
    if "mech" not in st.session_state:
        st.session_state.mech = None

    # Show the menu only if no subject has been selected yet
    if st.session_state.mech is None:
        sub = option_menu(
            menu_title="Choose Subject here",
            options=["select","Chemistry", "Physics", "Maths", "Mechanical","Previous Papers"],
            menu_icon="book-fill",
            default_index=0
        )

        if sub!="select":  # Update the session state when a subject is selected
            st.session_state.mech = sub

    # Based on the selected subject, display the corresponding app
    if st.session_state.mech == "Chemistry":
        chemistry.app()
    elif st.session_state.mech == "Physics":
        physics.app()
    elif st.session_state.mech == "Maths":
        maths.app()
    elif st.session_state.mech == "Mechanical":
        mech_sub.app()
    elif st.session_state.mech=="Previous Papers":
        papers.mech()
    # Add a reset button to clear the selection and show the menu again
    if st.session_state.mech is not None:
        if st.button("Choose Another Subject"):
            st.session_state.mech = None


if __name__ == "__main__":
    app()

