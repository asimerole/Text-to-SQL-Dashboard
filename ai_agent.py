import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def text_to_sql(user_text):
    prompt_text = """ 
    You're an SQL expert. We have an SQLite database. The table is called Users, 
    with the following columns: id (int), name (text), city (text), total_spent (int). A user will ask a question.
    Your task is to write ONLY a valid SQL query, without Markdown formatting, without explanations. Just the code.
    NOTE: City names in the database are stored in English (Kyiv, Berlin, Warsaw, Paris). 
    If a user searches for a city in Russian, be sure to translate it into English for the SQL query.
    """
    
    response = client.chat.completions.create(
        model="gpt-4o-mini", 
        messages=[
          {"role": "system", "content": prompt_text},
          {"role": "user", "content": user_text}
        ],
        temperature=0 
    )
   
    return response.choices[0].message.content

def data_to_text(user_question, raw_data):
    prompt_text = f"""
        You are a helpful business data assistant. 
        The user asked: "{user_question}".
        We queried the database and got this raw data back: {raw_data}.
        Your task is to analyze this raw data and provide a clear, natural, and polite answer to the user in English.
        If the raw data is empty, politely inform the user that no matching records were found.
        """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
          {"role": "system", "content": prompt_text}
        ],
        temperature=0.7 
    )
    
    return response.choices[0].message.content