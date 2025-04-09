from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from contextlib import asynccontextmanager
from models.target.base import Base as TargetBase
from normalizer import Normalizer
from config import SQLITE_PATH, POSTGRES_CONFIG
from db.db_pg import engine as pg_engine, get_db as pg_get_db
from db.db_sqlite import get_db as sqlite_get_db
from models import tables_list as target_tables_list

@asynccontextmanager
async def lifespan(app: FastAPI):
    TargetBase.metadata.drop_all(pg_engine)
    TargetBase.metadata.create_all(bind=pg_engine, tables=target_tables_list)
    yield

app = FastAPI(lifespan=lifespan)

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