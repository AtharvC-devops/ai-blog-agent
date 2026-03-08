import google.generativeai as genai

genai.configure(api_key="AIzaSyB9aUKTsR9Bamt8jBvRSzLvpB6F4JNZRRo")

models = genai.list_models()

for m in models:
    print(m.name)