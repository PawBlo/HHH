from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import uvicorn
import math
from dataset import Dataset
from recommendation_system import predict
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
app = FastAPI()
@app.get("/persons")
def get_persons():
    dataset = Dataset()
    persons = dataset.get_persons()
    persons = persons.to_dict('index')
    persons = {f'{i+1}': v for i, v in persons.items()}
    persons_info = dataset.get_personal_info_persons()
    for i,v in persons.items():
        persons[i] = {**persons[i], **persons_info[i]}
    return persons
@app.get("/volunteers")
def get_volunteers():
    dataset = Dataset()
    volunteers = dataset.get_volunteers()
    volunteers = volunteers.to_dict('index')
    volunteers = {f'{i+1}': v for i, v in volunteers.items()}
    volunteers_info = dataset.get_personal_info_volunteers()
    for i,v in volunteers.items():
        volunteers[i] = {**volunteers[i], **volunteers_info}
    return volunteers
@app.get("/predict")
def get_predict():
    pred = predict()
    return dict(enumerate(pred.flatten(),1))

@app.get("/get-image-person/{image_id}")
def get_image(image_id: int):
    image_folder = 'images'
    image_path = f"{image_folder}/person_{image_id}.jpg"
    try:
        return FileResponse(image_path)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Image not found")
    
@app.get("/get-image-volunteer/{image_id}")
def get_image(image_id: int):
    image_folder = 'images'
    image_path = f"{image_folder}/volunteer_{image_id}.jpg"
    try:
        return FileResponse(image_path)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Image not found")
