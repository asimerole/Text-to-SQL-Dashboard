import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def text_to_sql(user_text):
    prompt_text = f"""
    You are an SQL expert. We have an SQLite database. The table is called Users, 
    with the following columns: id (INTEGER), name (TEXT), city (TEXT), total_spent (INTEGER). 
    A user will ask a question.

    DATA SEARCH RULES:
    1. Data in the database is stored in English. If a user asks a question in Russian (e.g., searching for "София" or "Киев"), you MUST first translate the names and cities into English (e.g., Sophie, Kyiv).
    2. NEVER use strict equality (=) for text columns (name, city).
    3. ALWAYS use the LIKE operator with '%' wildcards for text searches to handle partial matches and variations (e.g., '%elena%', '%sophie%').
    4. Convert both sides to lowercase to ensure case-insensitive matching, for example: LOWER(name) LIKE LOWER('%sophie%') and LOWER(city) LIKE LOWER('%kyiv%').

    Your task is to write ONLY a valid SQL query. 
    No Markdown formatting (no ```sql), no explanations. Just the pure SQL code.
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