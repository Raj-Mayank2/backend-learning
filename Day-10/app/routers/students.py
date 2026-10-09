from fastapi import APIRouter, HTTPException, Query, status

from app.data.student_store import students
from app.schemas.student import (
    StudentCreate,
    StudentUpdate,
    StudentResponse,
)

router = APIRouter(
    prefix="/students",
    tags=["Students"],
)


@router.get("/", response_model=list[StudentResponse])
def list_students(
    search: str | None = None,
    course: str | None = None,
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1, le=100),
):
    results = list(students.values())

    if search:
        keyword = search.casefold()
        results = [
            student for student in results
            if keyword in student["name"].casefold()
            or keyword in student["email"].casefold()
        ]

    if course:
        results = [
            student for student in results
            if student["course"].casefold() == course.casefold()
        ]

    return results[skip:skip + limit]


@router.get("/{student_id}", response_model=StudentResponse)
def get_student(student_id: int):
    student = students.get(student_id)

    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )

    return student


@router.post(
    "/",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_student(student: StudentCreate):
    new_id = max(students.keys(), default=0) + 1

    new_student = {
        "id": new_id,
        **student.model_dump(),
    }

    students[new_id] = new_student
    return new_student


@router.put("/{student_id}", response_model=StudentResponse)
def replace_student(student_id: int, student: StudentCreate):
    if student_id not in students:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )

    updated_student = {
        "id": student_id,
        **student.model_dump(),
    }

    students[student_id] = updated_student
    return updated_student


@router.patch("/{student_id}", response_model=StudentResponse)
def update_student(student_id: int, student: StudentUpdate):
    existing_student = students.get(student_id)

    if existing_student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )

    changes = student.model_dump(exclude_unset=True)
    updated_student = {**existing_student, **changes}

    students[student_id] = updated_student
    return updated_student


@router.delete(
    "/{student_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_student(student_id: int):
    if student_id not in students:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )

    del students[student_id]
    return None