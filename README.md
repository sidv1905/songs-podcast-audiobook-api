# songs-podcast-audiobook-api
### Api made with Fastapi, Postgres for getting metadata of songs, podcasts, audiobooks. ###

Installation:
* pip install -r requirements.txt
* Set SECRET_KEY in .env  - "postgresql://user:password@postgresserver/db"
* uvicorn main:app --reload

For documentation:
* http://localhost:8000/docs
* http://localhost:8000/redoc
