from fastapi import APIRouter
from starlette.responses import HTMLResponse


router = APIRouter(
    prefix='/index',
    include_in_schema=False,
    default_response_class=HTMLResponse
)
