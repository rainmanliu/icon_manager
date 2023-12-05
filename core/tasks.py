# @Time : 10/18/23 2:30 PM
# @Author : HanyuLiu/Rainman
# @Email : rainman@ref.finance
# @File : tasks.py
import time
from celery.utils.log import get_logger
from core.celery_app import celery_app
from tortoise import run_async

logger = get_logger(__name__)


# @celery_app.task(acks_late=True)
# def test_data_celery(word: str) -> str:
#     for i in range(1, 11):
#         sleep(1)
#         current_task.update_state(state='PROGRESS',
#                                   meta={'process_percent': i * 10})
#     return f"test task return {word}"
