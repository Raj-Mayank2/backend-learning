from pydantic import BaseModel, Field


class StudentCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: str = Field(min_length=5, max_length=150)
    course: str = Field(min_length=2, max_length=100)
    year: int = Field(ge=1, le=6)


class StudentUpdate(BaseModel):
    name: str | None = Field(
        default=None, min_length=2, max_length=100
    )
    email: str | None = Field(
        default=None, min_length=5, max_length=150
    )
    course: str | None = Field(
        default=None, min_length=2, max_length=100
    )
    year: int | None = Field(default=None, ge=1, le=6)


class StudentResponse(BaseModel):
    id: int
    name: str
    email: str
    course: str
    year: int