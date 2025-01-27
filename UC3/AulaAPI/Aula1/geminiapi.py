import google.generativeai as genai

genai.configure(api_key="AIzaSyDuGxp2dnX9bPOK4lyBTANL2pbnjr5WoiA")


input = input("Digite o que você quer perguntar à API do gemini: ")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(input)
print(response.text)