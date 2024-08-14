from typing import Any, Optional, Tuple
from sqlalchemy.exc import SQLAlchemyError
from ..repositories.managers import MockManager


class MockController:
    manager = MockManager

    @classmethod
    def populate_database(cls) -> Tuple[Any, Optional[str]]:
        try:
            return cls.manager.populate_database(), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)