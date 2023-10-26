from fastapi import FastAPI
from src.routers.superbom.superbom_router import superbom_router
from src.core.database import Base, engine

app = FastAPI(title='Cabrumco API', description='API PRICIPAL', version='0.1a')

app.include_router(superbom_router, prefix='/superbom', tags=['Superbom'])


@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(engine)
