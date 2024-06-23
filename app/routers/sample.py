from fastapi import APIRouter

sample_router = APIRouter(prefix="/sample", tags=["sample"])

@sample_router.get("/api/sample")
async def sample_function():
    return {"message": "Hello, World!"}
