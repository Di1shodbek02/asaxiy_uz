from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    id: int
    first_name: str
    last_mame: str
    email: str
    phone_number: str
    username: str
    is_active: bool
    is_superuser: bool
    is_verified: bool

    class Config:
        or_mode = True


class UserCreate(schemas.BaseUser):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    username: str
    password: str
    is_active: bool
    is_superuser: bool
    is_verified: bool
