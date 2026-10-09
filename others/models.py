from langchain_google_genai import ChatGoogleGenerativeAI
from others.structure import filter_output


model = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')

filter_model = model.with_structured_output(filter_output)