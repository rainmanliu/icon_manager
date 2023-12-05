import logging

from starlette.requests import Request

from apps.icon_collect.schema import IconDataIn
from core.utils.base_util import get_limiter
from fastapi import APIRouter, Depends

logger = logging.getLogger(__name__)
limiter = get_limiter()
# router = APIRouter(prefix="/api/action", dependencies=[Depends(get_current_user)],)
router = APIRouter(prefix="/api/action")


@router.post("/icon_data", tags=["icon"])
def icon_data(request: Request, icon_data: IconDataIn):
    name = icon_data.name
    print(name)
