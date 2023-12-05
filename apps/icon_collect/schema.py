
import uuid
from typing import Optional
from pydantic import BaseModel, validator
from tortoise.contrib.pydantic import pydantic_model_creator

class BaseProperties(BaseModel):
    @validator("hashed_id", pre=True, always=True, check_fields=False)
    def default_hashed_id(cls, v):
        return v or uuid.uuid4()

    def create_update_dict(self):
        return self.model_dump(
            exclude_unset=True,
            exclude={"id", "is_superuser", "is_active"},
        )

    def create_update_dict_superuser(self):
        return self.model_dump(exclude_unset=True, exclude={"id"})


class IconDataIn(BaseModel):
    name: Optional[str]
    # address: Optional[str]
    # code: Optional[str]