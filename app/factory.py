from fastapi import FastAPI
from .config import get_settings


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI()

    @app.get("/")
    async def read_main():
        return {"msg": settings.app_name}

    return app
