from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from models.target.base import Base as TargetBase
from normalizer import Normalizer
from db.db_pg import engine as pg_engine, get_db as pg_get_db
from db.db_sqlite import get_db as sqlite_get_db
from models import tables_list as target_tables_list
from datetime import datetime

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

@app.get("/count_all_attendance")
def count_all_attendance(
    start_timestamp: str,
    end_timestamp: str,
    postgres_session: Session = Depends(pg_get_db)
):
    try:
        start_timestamp = datetime.strptime(start_timestamp, "%Y-%m-%d %H:%M:%S")
        end_timestamp = datetime.strptime(end_timestamp, "%Y-%m-%d %H:%M:%S")

        func_name = 'get_attendance_count'
        result = postgres_session.execute(
            text(f"SELECT {func_name}(:start, :end)"),
            {"start": start_timestamp, "end": end_timestamp}
        ).scalar_one()
        return {
            "count": result,
            "period": f"{start_timestamp} - {end_timestamp}",
        }
    except ValueError as e:
        raise HTTPException(400, detail=str(e))
    except Exception as e:
        raise HTTPException(500, detail="Internal server error")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)