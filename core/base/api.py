# @Time : 10/8/23 9:51 AM
# @Author : HanyuLiu/Rainman
# @Email : rainman@ref.finance
# @File : api.py
import logging
from fastapi import APIRouter, Depends, Response
from starlette.requests import Request

from core.auth.utils import get_current_user
from core.utils.base_util import get_limiter
logger = logging.getLogger(__name__)
limiter = get_limiter()
router = APIRouter()


# @router.get('/', tags=['invite check code'])
# async def root():
#     return {"message": "welcome to dapdap"}


@router.get('/health_check', tags=['base'])
@limiter.limit('5/second')
async def health_check(request: Request):
    logger.info(request)
    return {"message": "Running!"}



