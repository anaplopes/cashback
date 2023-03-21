from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse


async def http_exception_handler(
    _: Request,
    exc: HTTPException,
) -> JSONResponse:
    response = JSONResponse(
        content={"successful": False, "detail": exc.detail},
        status_code=exc.status_code,
    )
    if exc.headers is not None:
        response.init_headers(exc.headers)

    return response
