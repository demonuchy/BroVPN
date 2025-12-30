import pytest
import httpx


@pytest.mark.anyio
async def test_health_endpoints():
    """Простой тест health эндпоинтов"""
    async with httpx.AsyncClient() as client:
        # Auth сервис
        auth_response = await client.get("http://127.0.0.1:8001/health")
        assert auth_response.status_code == 200
        
        # VPN сервис
        vpn_response = await client.get("http://127.0.0.1:8002/health")
        assert vpn_response.status_code == 200
    
        # Можно добавить проверки через nginx
        nginx_response = await client.get("http://127.0.0.1:8080/health")
        assert nginx_response.status_code == 200