from typing import List
import json
from fastapi import Depends, FastAPI, HTTPException, Request,UploadFile,File,Form
from sqlalchemy.orm import Session
import shutil
import crud, models, schemas
from database import SessionLocal, engine
from fastapi.staticfiles import StaticFiles



app = FastAPI()


models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




@app.post("/{audioFileType}/upload")
async def create_file(audioFileType:str,request:str = Form(...),db:Session = Depends(get_db),file: UploadFile = File(...)):
    
    request = json.loads(request)
    
    if audioFileType == "song":
        newItem = crud.create_song(db=db,song=request)

        id = newItem.id
        file_location = f"songs/{id}.mp3"
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return newItem
    elif audioFileType=="podcast":
        newItem = crud.create_podcast(db=db,song=request)

        id = newItem.id
        file_location = f"podcasts/{id}.mp3"
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return newItem
    elif audioFileType == "audiobook":
        newItem = crud.create_audiobook(db=db,song=request)

        id = newItem.id
        file_location = f"audiobook/{id}.mp3"
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return newItem
    else:
        raise HTTPException(status_code = 404,detail = "FileType not found")
    

@app.post("/{audioFileType}/")
async def creater_file(audioFileType:str,request:Request,db:Session = Depends(get_db)):
    
    request = await request.json()
    
    
    if audioFileType == "song":
        return crud.create_song(db=db,song=request)
    elif audioFileType=="podcast":
        return crud.create_podcast(db=db,podcast=request)
    elif audioFileType == "audiobook":
        return crud.create_audiobook(db = db, audiobook=request)
    else:
        raise HTTPException(status_code = 404,detail = "FileType not found")
    
    return request


@app.get("/{audioFileType}/")
async def get_data(audioFileType:str,db:Session = Depends(get_db)):
    
    if audioFileType == "song":
        return crud.get_songs(db=db)
    elif audioFileType=="podcast":
        return crud.get_podcasts(db=db)
    elif audioFileType == "audiobook":
        return crud.get_audiobooks(db = db)
    else:
        raise HTTPException(status_code = 404,detail = "FileType not found")





@app.get("/{audioFileType}/{file_id}")
def get_file(audioFileType:str,file_id:int,db:Session = Depends(get_db)):
    
    if audioFileType == "song":
        db_file = crud.get_song(db,id = file_id)
    elif audioFileType == "podcast":
        db_file = crud.get_podcast(db,id = file_id)
    elif audioFileType == "audiobook":
        db_file = crud.get_audiobook(db,id = file_id)
    else:
        raise HTTPException(status_code = 404,detail = "FileType not found")
    
    if db_file is None:
        raise HTTPException(status_code = 404,detail = "File not found")
    return db_file



@app.delete("/{audioFileType}/{file_id}")
def delete_file(audioFileType:str,file_id:int,db:Session = Depends(get_db)):
    if audioFileType == "song":
        db_file = crud.delete_song(db,id = file_id)
    elif audioFileType == "podcast":
        db_file = crud.delete_podcast(db,id = file_id)
    elif audioFileType == "audiobook":
        db_file = crud.delete_audiobook(db,id = file_id)
    else:
        raise HTTPException(status_code = 404,detail = "FileType not found")
    
    if db_file is None:
        raise HTTPException(status_code = 404,detail = "File not found")
    return db_file

@app.put("/{audioFileType}/{file_id}")
async def create_file(file_id:int,audioFileType:str,request:Request,db:Session = Depends(get_db)):
    request =await request.json()
    
    if audioFileType == "song":
        db_file  = crud.update_song(db=db,id= file_id,song=request)

    elif audioFileType == "audiobook":
        db_file =  crud.update_audiobook(db=db,id= file_id,audiobook=request)
        
    elif audioFileType == "podcast":
        db_file =  crud.update_podcast(db=db,id= file_id,podcast=request)    
    else:
        raise HTTPException(status_code = 404,detail = "FileType not found")
    if db_file is None:
        raise HTTPException(status_code = 404,detail = "File not found")
    return db_file
        