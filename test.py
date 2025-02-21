import google.generativeai as genai
genai.configure(api_key='AIzaSyBEblD4B-gLYkR3fSK6i2AFefT_WMo5JsQ')
sample_file = genai.upload_file(path=r"C:\Users\HP\Downloads\Images\96399948_b86c61bfe6.jpg",
                            display_name="Jetpack drawing")
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")

# Prompt the model with text and the previously uploaded image.
response = model.generate_content([sample_file, "Can you give me the caption of the full image within 15 words?"])
print(response.text)