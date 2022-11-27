from fastapi import FastAPI, Depends
from tortoise.contrib.fastapi import register_tortoise
from app.config import Settings, get_settings
import os

app = FastAPI()

register_tortoise(
    app,
    db_url=os.environ.get('DATABASE_URL'),
    modules={"models": ["app.models.wallet"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

@app.get('/ping')
async def pong(settings: Settings = Depends(get_settings)):
    return {
        'ping': 'pong',
        'environment': settings.environment,
        'test': settings.testing,
    }
