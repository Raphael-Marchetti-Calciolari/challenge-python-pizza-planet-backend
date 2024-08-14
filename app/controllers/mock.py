from typing import Any, Optional, Tuple
from sqlalchemy.exc import SQLAlchemyError
from ..repositories.managers import MockManager

class MockController:
    manager = MockManager

    @classmethod
    def fill_mock_data(cls) -> Tuple[Any, Optional[str]]:
        try:
            return cls.manager.fill_mock_data(), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)
        
    @classmethod
    def clear_mock_data(cls) -> Tuple[Any, Optional[str]]:
        try:
            return cls.manager.clear_mock_data(), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)