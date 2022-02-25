# jellysmack

Define .env file as following:
```
SECRET_KEY=...

POSTGRES_USER=...
POSTGRES_PASSWORD=...
POSTGRES_SERVER=...
POSTGRES_PORT=5432
POSTGRES_DB=...

PYTHONPATH=/backend
``` 

`alembic upgrade head`

`python app/initial_data.py`

`psql -h localhost -U user --dbname=dbname`

`SELECT * FROM character_episode;`


