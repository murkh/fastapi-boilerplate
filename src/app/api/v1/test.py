from fastapi import APIRouter
from ...core.exceptions import ForbiddenException

router = APIRouter(tags=["Test"])


@router.get("/test", summary="Test Endpoint")
async def test_endpoint():
    """
    A simple test endpoint to verify the API is working.
    Returns a success message.
    """
    return {"message": "Test endpoint is working!"}


@router.get("/error", summary="Error Endpoint")
async def error_endpoint():
    """
    An endpoint that raises an HTTP 500 error for testing error handling.
    Raises an HTTPException with status code 500.
    """
    raise ForbiddenException(status_code=500, detail="This is a test error endpoint.")
