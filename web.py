import streamlit as st
from ai_agent import data_to_text, text_to_sql
from database.dbconn import sqlExecute

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

st.title("🤖 AI Corporate Analyst")
st.markdown("Ask a question about the customer database using natural language.")

user_question = st.text_input("Your question:", placeholder="For example: Who from Berlin spent more than 1,000?")

if st.button("Check the database"):
    if user_question:
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
    else:
        st.warning("Please enter your question.")