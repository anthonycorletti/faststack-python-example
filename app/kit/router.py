from http.client import HTTPException
from typing import Any, Callable, Dict, Optional, Tuple

from fastapi import Request

from app.const import Format


async def format_method(request: Request) -> Format:
    v = request.headers.get("accept")
    if not v:
        return Format.default
    _accept = v.split(";")[0].split(",")[0]
    if _accept == "*/*":
        return Format.default
    elif _accept == "text/html":
        return Format.html
    elif _accept == "application/json":
        return Format.json
    else:
        return Format.default


async def respond_to(
    request: Request, response_options: Dict[Format, Tuple[Any, Optional[Callable]]]
) -> Any:
    _format = await format_method(request)
    if _format == Format.json:
        return response_options[_format]
    elif _format == Format.html or _format == Format.default:
        data, func = response_options[Format.html]
        return await func(data)
    else:
        raise HTTPException(
            status_code=406,
            detail=f"Unsupported accept header: {_format}",
        )
