import pytest
import httpx


@pytest.mark.anyio
async def test_health_nginx():
    """Простой тест health эндпоинтов"""
    async with httpx.AsyncClient() as client:
        response = await client.get("http://127.0.0.1:8080/health")
        assert response.status_code == 200


@pytest.mark.anyio
async def test_health_auth():
    """Простой тест health эндпоинтов"""
    async with httpx.AsyncClient() as client:
        response = await client.get("http://127.0.0.1:8001/health")
        assert response.status_code == 200


@pytest.mark.anyio
async def test_health_vpn():
    """Простой тест health эндпоинтов"""
    async with httpx.AsyncClient() as client:
        response = await client.get("http://127.0.0.1:8002/health")
        assert response.status_code == 200
       

@pytest.mark.anyio
async def test_health_tgbot():
    """Простой тест health эндпоинтов"""
    async with httpx.AsyncClient() as client:
        response = await client.get("http://127.0.0.1:8003/health")
        assert response.status_code == 200
       