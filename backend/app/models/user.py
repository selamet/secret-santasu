from typing import Optional
from pydantic import EmailStr, constr, validator
from app.models.core import DateTimeModelMixin, IDModelMixin, CoreModel


class User(CoreModel):
    """
    Leaving off password and salt from base model
    """
    email: EmailStr
    username: str
    email_verified: bool = False
    is_active: bool = True
    is_superuser: bool = False

