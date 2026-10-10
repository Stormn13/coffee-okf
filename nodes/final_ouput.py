from others.state import State
from google import genai
import os
def final_output(state: State):
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError("Set GEMINI_API_KEY or GOOGLE_API_KEY in the project .env file.")
    client = genai.Client(api_key=api_key)
    my_file = client.files.upload(file = state["selected_file"]) #type: ignore

    response = client.models.generate_content(model = "gemini-2.5-flash", contents=[my_file, f"based on the document provieded answer {state['initial_question']}"])
    return {"output": response.text}