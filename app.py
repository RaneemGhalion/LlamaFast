import time
import copy
import asyncio
import requests

from fastapi import FastAPI, Request
from llama_cpp import Llama
from sse_starlette import EventSourceResponse
from llama_cpp import Llama
from langchain_community.embeddings import LlamaCppEmbeddings

# Load the model
print("Loading model...")
llm = Llama(model_path="/home/ranem/llm_fast_api/codellama-7b.Q2_K.gguf") # change based on the location of models
print("Model loaded!")
from fastapi import FastAPI, Form
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Serve static files (e.g., CSS, JS, images)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return FileResponse("static/index.html")

@app.post("/get_answer")
def get_answer(question: str = Form(...)):
    # Your code to interact with LLAMA2 and get answers
    # Replace the following line with your actual LLAMA2 integration logic
    # answer = f"Answer from LLAMA2 for: {question}"
    prompt = question

# generate a response (takes several seconds)
    output = llm(prompt)
    
    return {"answer": output["choices"][0]["text"]}
