import pytest
import httpx


@pytest.mark.anyio
async def test_health_db_auth():
    async with httpx.AsyncClient() as client:
        auth_response = await client.get("http://127.0.0.1:8001/api/v1/auth/test")
        assert auth_response.status_code == 400