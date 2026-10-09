from fastapi import FastAPI

from app.routers.students import router as students_router

app = FastAPI(
    title="Student Management System",
    description="A modular FastAPI application for managing students.",
    version="1.0.0",
)


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}


app.include_router(students_router)