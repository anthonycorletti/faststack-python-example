import os

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from app.pages.index import IndexPage
from app.router import app_router

os.environ["TZ"] = "UTC"


def create_fastapi_app() -> FastAPI:
    app = FastAPI(title="faststack-python-example")
    app.include_router(app_router)

    # TODO: 404 handler, status code handlers (500, etc.) 🤔

    @app.get("/{path:path}")
    async def _index() -> HTMLResponse:
        return await IndexPage().doc.render_html()

    return app


app = create_fastapi_app()
