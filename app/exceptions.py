from typing import Dict, Optional

from fastapi import HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse

from app.pages.not_found import NotFoundPage


async def not_found_error(
    request: Request, exc: HTTPException
) -> HTMLResponse | JSONResponse:
    """Handle 404 errors."""
    if request.headers.get("accept") == "application/json":
        return JSONResponse(
            status_code=404,
            content={"detail": "Not Found"},
        )
    else:
        return await NotFoundPage().doc.render_html()


exception_handlers: Optional[Dict] = {
    404: not_found_error,
}
