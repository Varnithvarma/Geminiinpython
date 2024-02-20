import pathlib
import textwrap
import google.generativeai as genai

user_data = "AIzaSyCA2tZgfTMFQgcMH-_DMkYDk0v7pL2vGF4"
GOOGLE_API_KEY = user_data
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("How do you feel?", stream=True)
for chuck in response:
    print(chuck.text)
    print("_"*80)