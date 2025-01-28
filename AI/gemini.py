import google.generativeai as genai

genai.configure(api_key="AIzaSyCxlyyVQFb4ZOAi0LdGrYu3OnRdoGsaP3k")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Can you understand a pandas dataframe")
print(response.text)