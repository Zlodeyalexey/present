from starlette.requests import Request

from .router import router
from ..settings import templating


@router.get('/', name='index_index')
async def index(request: Request):
    return templating.TemplateResponse(
        name='index/index.html',
        context={
            'request': request
        }
    )