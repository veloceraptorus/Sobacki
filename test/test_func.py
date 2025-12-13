import pytest
from httpx import AsyncClient, ASGITransport

# from func import my_factorial
from src.routers.client import get
from src.main import app



class TestClient:
    uid = ''
    @pytest.mark.run(order=1)
    @pytest.mark.asyncio
    async def test_create(self):
        async_client = AsyncClient(
            transport=ASGITransport(app=app),
            base_url='http://test'
        )
        async with async_client as ac:
            response = await ac.post('/api/v1/client/create', 
                                    json={"name": "test","telephone_number": "+7999999999","email": "text@test.test"})
            name = response.json()['name']
            assert name == 'test'
            TestClient.uid = response.json()['uid']
            assert response.status_code == 200
    
    @pytest.mark.run(order=2)
    @pytest.mark.asyncio
    async def test_update(self):
        async_client = AsyncClient(
            transport=ASGITransport(app=app),
            base_url='http://test'
        )
        async with async_client as ac:
            response = await ac.put('/api/v1/client/update', 
                                    json={"uid": TestClient.uid, "name": "testik","telephone_number": "+7999999999", "email": "text@test.test"})
            assert response.status_code == 200
            name = response.json()['name']
            assert name == 'testik'

    @pytest.mark.asyncio
    @pytest.mark.run(order=2)
    async def test_list(self):
        async_client = AsyncClient(
            transport=ASGITransport(app=app),
            base_url='http://test'
        )
        async with async_client as ac:
            response = await ac.get('/api/v1/client/list')
            assert response.status_code == 200

    @pytest.mark.asyncio
    @pytest.mark.run(order=2)
    async def test_get(self):
        async_client = AsyncClient(
            transport=ASGITransport(app=app),
            base_url='http://test'
        )
        async with async_client as ac:
            response = await ac.get(f'/api/v1/client/{TestClient.uid}')
            assert response.status_code == 200
