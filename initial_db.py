import asyncio

from app.prepare_db import recreate_db


asyncio.run(recreate_db())
