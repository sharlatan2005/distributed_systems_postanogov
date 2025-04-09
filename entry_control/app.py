from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models.target.base import Base as TargetBase
from normalizer import Normalizer
from db.db_pg import engine as pg_engine, get_db as pg_get_db
from db.db_sqlite import get_db as sqlite_get_db
from models import tables_list as target_tables_list

def init_target_db():
    TargetBase.metadata.drop_all(pg_engine) 
    TargetBase.metadata.create_all(bind=pg_engine, tables=target_tables_list)

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_target_db()

@app.post("/normalize")
def normalize(
    sqlite_session: Session = Depends(sqlite_get_db),
    postgres_session: Session = Depends(pg_get_db)
):
    try:
        normalizer = Normalizer(sqlite_session, postgres_session)
        normalizer.normalize()
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Normalization failed: {e}")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)