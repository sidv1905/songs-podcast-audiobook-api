from sqlalchemy.orm import Session

import models, schemas

def create_audiobook(db:Session,audiobook):
   
    db_audiobook = models.Audiobook(title=audiobook["title"], duration = audiobook["duration"],  narrator = audiobook["narrator"], author= audiobook["author"])
    db.add(db_audiobook)

    db.commit()
    db.refresh(db_audiobook)

    return db_audiobook


def create_podcast(db:Session,podcast):
   
    db_podcast = models.Podcast(name=podcast["name"], duration = podcast["duration"],  host = podcast["host"], participants= podcast["participants"])
    db.add(db_podcast)

    db.commit()
    db.refresh(db_podcast)

    return db_podcast


def create_song(db:Session, song):
   
    db_song = models.Song(name = song["name"], duration = song["duration"])

    db.add(db_song)
    db.commit()
    db.refresh(db_song)

    return db_song

def get_songs(db:Session):
    return db.query(models.Song).all()

def get_song(db:Session,id:int):
    return db.query(models.Song).filter(models.Song.id == id).first()

def get_podcasts(db:Session):
    return db.query(models.Podcast).all()

def get_podcast(db:Session,id:int):
    return db.query(models.Podcast).filter(models.Podcast.id == id).first()

def get_audiobooks(db:Session):
    return db.query(models.Audiobook).all()

def get_audiobook(db:Session,id:int):
    return db.query(models.Audiobook).filter(models.Audiobook.id == id).first()







def delete_song(db:Session,id:int):
    db_song = db.query(models.Song).filter(models.Song.id == id)
    response = db_song.first()
    db_song.delete()
    db.commit()

    return response

def delete_podcast(db:Session,id:int):
    db_podcast = db.query(models.Podcast).filter(models.Podcast.id == id)
    response = db_podcast.first()
    db_podcast.delete()
    db.commit()
    return response


def delete_audiobook(db:Session,id:int):
    db_audio = db.query(models.Audiobook).filter(models.Audiobook.id == id)
    response =db_audio.first()
    db_audio.delete()
    db.commit()

    return response


def update_song(db:Session,id:int,song):
    
    updated_song = db.query(models.Song).filter(models.Song.id==id)
    response = updated_song.first()
    updated_song.update(song,synchronize_session=False)
    db.commit()

    return response


def update_podcast(db:Session,id:int,podcast):
    
    updated_podcast = db.query(models.Podcast).filter(models.Podcast.id==id)
    response = updated_podcast.first()
    update_podcast.update(podcast,synchronize_session=False)
    db.commit()

    return response


def update_audiobook(db:Session,id:int,audiobook):
    
    updated_audiobook = db.query(models.Audiobook).filter(models.Audiobook.id==id)
    response = updated_audiobook.first()
    updated_audiobook.update(audiobook,synchronize_session=False)
    
    db.commit()

    return response
