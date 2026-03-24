import os
import streamlit as st
from ai_agent import data_to_text, text_to_sql
from database.dbconn import dbInit, sqlExecute
from dotenv import load_dotenv

load_dotenv()

adm_password = os.getenv('ADM_PWD')

dbInit()

st.set_page_config(page_title="AI Data Assistant", page_icon="📊")

st.sidebar.title("🗄️ Database Preview")
st.sidebar.markdown("Current data in the `Users` table:")

try:
    all_data = sqlExecute("SELECT * FROM Users")
    
    formatted_data = [
        {"ID": row[0], "Name": row[1], "City": row[2], "Total Spent": row[3]} 
        for row in all_data
    ]
    
    st.sidebar.dataframe(formatted_data, use_container_width=True)
except Exception as e:
    st.sidebar.error(f"Failed to load DB: {e}")

st.sidebar.markdown("---") 
st.sidebar.subheader("🔐  Access to the AI")

if "demo_count" not in st.session_state:
    st.session_state.demo_count = 0

access_password = st.sidebar.text_input("Access password:", type="password")

if access_password == "demo123":
    st.sidebar.info(f"Demo requests remaining: {10 - st.session_state.demo_count}")

st.title("🤖 AI Corporate Analyst")
st.markdown("Ask a question about the customer database using natural language.")

user_question = st.text_input("Your question:", placeholder="For example: Who from Berlin spent more than 1,000?")

if st.button("Check the database"):
    if not user_question:
        st.warning("Please enter your question.")
    else:
        is_allowed = False
        if access_password == adm_password:
            is_allowed = True
        elif access_password == "demo123":
            if st.session_state.demo_count < 10:
                is_allowed = True
                st.session_state.demo_count += 1
            else:
                st.error("❌ The demo access limit (10 requests) has been reached.")
                
        else:
            st.error("⚠️ Enter the correct password in the sidebar on the left.")
            
        if is_allowed:    
            with st.spinner("The AI is writing an SQL query..."):
                sql_query = text_to_sql(user_question)
                
            st.subheader("Generated SQL query:")
            st.code(sql_query, language="sql") 

            try:
                data = sqlExecute(sql_query)

                with st.expander("View Raw Database Output"):
                    st.write(data) 

                with st.spinner("Analyzing data..."):
                    human_answer = data_to_text(user_question, data)

                st.success(human_answer)

            except Exception as e:
                st.error(f"Database Error: {e}")
        