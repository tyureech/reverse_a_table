from app.tables.models import Table
from app.dao.base import BaseDAO


class TableDAO(BaseDAO):
    model = Table
