import asyncio
import pytest
from httpx import AsyncClient
from app.main import app
from prepare_db import recreate_db


@pytest.fixture(scope="session", autouse=True)
async def run_recreate_db():
    await recreate_db()


@pytest.fixture(scope="session")
def event_loop():
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="function")
async def ac():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
