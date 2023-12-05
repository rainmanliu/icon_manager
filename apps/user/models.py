# @Time : 10/13/23 1:15 PM
# @Author : HanyuLiu/Rainman
# @Email : rainman@ref.finance
# @File : models.py
from enum import Enum

from tortoise import fields
from tortoise.fields.base import CASCADE

from core.base.base_models import BaseDBModel, BaseCreatedUpdatedAtModel, BaseCreatedAtModel


class UserInfo(BaseDBModel, BaseCreatedAtModel):
    class ChainTypeEnum(str, Enum):
        ETH = 'eth'
        OTHER = 'other'
    address = fields.CharField(max_length=50, unique=True, description="user's evm address")
    account_info = fields.CharField(max_length=25, null=True)
    chain_type = fields.CharEnumField(ChainTypeEnum, default=ChainTypeEnum.ETH)
    last_login = fields.DatetimeField(null=True)

    def __str__(self):
        return self.address

    class Meta:
        table = 'user_info'

class GroupInfo(BaseDBModel, BaseCreatedUpdatedAtModel):
    name = fields.CharField(max_length=100, unique=True, description="group name")
    title = fields.CharField(max_length=255, description="group title")
    users = fields.ManyToManyField("models.UserInfo", db_constraint=False, on_delete=CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        table = 'group_info'
