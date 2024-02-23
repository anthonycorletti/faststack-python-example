import os
from typing import List

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastui import AnyComponent, FastUI, prebuilt_html
from fastui import components as c

from app.router import router

os.environ["TZ"] = "UTC"


def create_fastapi_app() -> FastAPI:
    app = FastAPI(title="faststack-python-example")
    app.include_router(router)

    @app.get("/api/", response_model=FastUI, response_model_exclude_none=True)
    async def index() -> List[AnyComponent]:
        return [
            c.Page(
                components=[
                    c.PageTitle(
                        text="faststack-python-example",
                    ),
                    c.Heading(
                        text="It's the faststack-python-example",
                    ),
                ]
            )
        ]

    @app.get("/{path:path}")
    async def html_landing() -> HTMLResponse:
        return HTMLResponse(
            prebuilt_html(
                title="faststack-python-example",
            )
        )

    return app


app = create_fastapi_app()
