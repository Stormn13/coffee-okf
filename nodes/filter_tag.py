from others.state import State
from others.models import filter_model
from google import genai
import os
import time
from pathlib import Path
from langchain_core.messages import HumanMessage

def filter_tag(state: State):
    
    #add index.md in the model
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
    index_path = Path(__file__).resolve().parent.parent / "knowledge_base" / "index.md"
    my_file = client.files.upload(file=str(index_path))
    # Ensure the file is ready (best practice for larger files)
    while my_file.state.name == "PROCESSING":  # type: ignore
        time.sleep(2)
        my_file = client.files.get(name=my_file.name) # type: ignore
    message= HumanMessage(
        content=[
            {
            "type":"text",
            "text":"Look at the document and the question and then let us know which of the filters suit the incoming answer the most"
            },
            {
                "type":"media",
                "file_uri": my_file.uri,
                "mime_type" : "text/markdown"
            }
        ]

    )
    response = filter_model.invoke([message])
    return {"tag" : response.filters} #type: ignore
