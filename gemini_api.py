from google import genai


def AI_response_text(prompt:str):
    client = genai.Client(api_key="AQ.Ab8RN6I6eblupH2zFn68SNBF0Z854_HoIlkmBFUoCWVnAc3hGw")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents = f"{prompt} give me short and satisfying answer in 2-3 lines ."
    )
    
    return response.text