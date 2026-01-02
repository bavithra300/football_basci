from gemini_client import get_model

model = get_model()
res = model.generate_content("Say READY if you are alive")
print(res.text)
