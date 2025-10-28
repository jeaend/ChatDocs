import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

print("google-generativeai version:", genai.__version__)
print("\nModels accessible to this API key:\n")

for m in genai.list_models():
    if "generateContent" in m.supported_generation_methods:
        print("-", m.name)
