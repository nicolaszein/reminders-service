import pytest
from httpx import AsyncClient
from reminders.presentation.app import app


@pytest.mark.asyncio
async def test_health_ok(data_table):
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/health")

    assert response.status_code == 200
    assert response.json() == {"ok": True}


@pytest.mark.asyncio
async def test_health_error_when_data_table_does_not_exist():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/health")

    assert response.status_code == 500
    assert response.json() == {"detail": "table not found"}
