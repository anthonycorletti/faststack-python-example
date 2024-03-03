import os

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.router import app_router

os.environ["TZ"] = "UTC"


def create_fastapi_app() -> FastAPI:
    app = FastAPI(title="faststack-python-example")
    app.include_router(app_router)

    # TODO: 404 handler

    @app.get("/{path:path}")
    async def _index(request: Request) -> HTMLResponse:
        return views.TemplateResponse(
            name="index.html",
            context={"request": request},
        )

    return app


views = Jinja2Templates(directory="app/views")
app = create_fastapi_app()
