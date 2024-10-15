from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from txt_summarizer.pipeline.predict import PredictionPipeline


text:str = "What is Text Summarization?"

app = FastAPI()

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")



@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training successful !!")

    except Exception as e:
        return Response(f"Error Occurred! {e}")

from pydantic import BaseModel
class PredictionRequest(BaseModel):
    text: str
    count: int


@app.post("/predict")
async def predict_route(text, count: int):
    try:

        obj = PredictionPipeline()
        text = obj.predict(text, count)
        return text
    except Exception as e:
        raise e
    

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)