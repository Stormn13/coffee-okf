from others.state import State
from google import genai
import os
def final_output(state: State):
    client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))
    my_file = client.files.upload(file = state["selected_file"]) #type: ignore

    response = client.models.generate_content(model = "gemini-2.5-flash", contents=[my_file, f"based on the document provieded answer {state['initial_question']}"])
    return {"output": response.text}