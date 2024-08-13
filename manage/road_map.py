import streamlit as st
from datetime import datetime, timedelta
import pandas as pd
def rmap():
    st.title('ECET Exam Preparation Roadmap')
    today=datetime.today().date()
    df=pd.read_excel(r"C:\Users\mahes\chemistry.xlsx")
    df1=pd.read_excel(r"C:\Users\mahes\physics.xlsx")
    st.markdown("### Select a Subject for the Roadmap:")

    subject=st.selectbox(options=["Select","Chemistry","Physics","Maths"],label="")
    if subject=="Chemistry":
        date = st.date_input('select starting date', value=today)
        new_dates=[]
        ndate=date
        for days in df['days']:
            ndate += timedelta(days=days)
            new_dates.append(ndate)

        # Add the new dates to the DataFrame
        df['Dates'] = new_dates
        st.write(df)
        st.subheader("Total Estimated Study Time")
        st.write(f"For Sem 1 Chapters: 18 days ({today+timedelta(days=18)})")
        st.write(f"For Sem 2 Chapters: 14 days ({new_dates[-1]})")
        st.write("Revision: Allocate at least 3-5 days for revision after completing the chapters.")
        st.write("Practice: Include time for solving previous exam papers and practice questions, which could take another 4-5 days.")
        st.subheader("Final Estimate")
        st.write("Total Preparation Time: 40-43 days")
        st.write(f"Final dates: {today+timedelta(days=40)}    To    {today+timedelta(days=43)} ")
    if subject=="Physics":
        date1 = st.date_input('select starting date', value=today)
        new_dates1 = []
        ndate1 = date1
        for days1 in df1['days']:
            ndate1 += timedelta(days=days1)
            new_dates1.append(ndate1)

        # Add the new dates to the DataFrame
        df1['Dates'] = new_dates1
        st.write(df1)
        st.subheader("Total Estimated Study Time")
        st.write(f"For Sem 1 Chapters: 16 days ({today + timedelta(days=16)})")
        st.write(f"For Sem 2 Chapters: 18 days ({new_dates1[-1]})")
        st.write("Revision: Allocate at least 3-5 days for revision after completing the chapters.")
        st.write("Practice: Include time for solving previous exam papers and practice questions, which could take another 4-5 days.")
        st.subheader("Final Estimate")
        st.write("Total Preparation Time: 44-59 days")
        st.write(f"Final dates: {today + timedelta(days=44)}    To    {today + timedelta(days=59)} ")

    if subject=="Maths":
        st.write("Maths road Map is under Construction")
    if subject=="Select":
        st.subheader("Select the subject to find best Road Map..")













