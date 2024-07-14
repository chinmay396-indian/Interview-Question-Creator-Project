from fastapi import FastAPI, Form, Request, Response, File, UploadFile, HTTPException, status
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
import uvicorn
import os
import aiofiles
import json
import csv
from src.helper import llm_pipeline

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload")
async def chat(request: Request, pdf_file: UploadFile = File(...), filename: str = Form(...)):
    base_folder = "/data/"
    if not os.path.isdir(base_folder):
        os.mkdir(base_folder)
    pdf_filename = os.path.join(base_folder, filename)

    async with aiofiles.open(pdf_filename, "wb") as f:
        content = await pdf_file.read()
        await f.write(content)

    response_data = jsonable_encoder({"msg": "success", "pdf_filename": pdf_filename})
    return Response(content=json.dumps(response_data), media_type="application/json")

def get_csv(file_path):
    question_list = llm_pipeline(file_path)
    base_folder = "/data/"
    if not os.path.isdir(base_folder):
        os.mkdir(base_folder)
    output_file = os.path.join(base_folder, "Questions.csv")
    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Question"])

        for question in question_list:
            csv_writer.writerow([question])

    return output_file

@app.post("/analyze")
async def analyze(request: Request, pdf_filename: str = Form(...)):
    output_file = get_csv(pdf_filename)
    response_data = jsonable_encoder({"output_file": output_file})
    return Response(content=json.dumps(response_data), media_type="application/json")

if __name__ == "__main__":
    uvicorn.run("app:app", host='0.0.0.0', port=8080, reload=True)
