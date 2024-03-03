from typing import Any, Callable, Dict, List

from fastapi import Request, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

from app.const import ResponseFormat


class RespondWith(BaseModel):
    data: BaseModel | Dict | List | None = None
    via: Callable | None = None


async def respond_to(
    request: Request,
    response_options: Dict[ResponseFormat, Dict] | None,
) -> Any:
    _format = await format_method(request=request)
    if response_options is None:
        _with = RespondWith(data=None, via=None)
    else:
        _with = RespondWith(**response_options.get(_format, {}))
    if _format == ResponseFormat.json:
        return _with.data
    elif _format == ResponseFormat.html or _format == ResponseFormat.default:
        if _with.via:
            return await _with.via(request, _with.data)
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"respond_to: no via method provided for {_format} format.",
            )
    else:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail=f"Unsupported accept header: {_format}",
        )


async def format_method(request: Request) -> ResponseFormat:
    v = request.headers.get("accept")
    if not v:
        return ResponseFormat.default
    _accept = v.split(";")[0].split(",")[0]
    if _accept == ResponseFormat.html.value:
        return ResponseFormat.html
    elif _accept == ResponseFormat.json.value:
        return ResponseFormat.json
    else:
        return ResponseFormat.default
