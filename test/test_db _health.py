import pytest
import httpx


@pytest.mark.anyio
async def test_health_endpoints():
    async with httpx.AsyncClient() as client:
        auth_response = await client.get("http://127.0.0.1:8001/db/health")
        assert auth_response.status_code == 200