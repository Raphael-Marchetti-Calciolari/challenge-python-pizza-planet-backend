from typing import Any, Optional, Tuple
from sqlalchemy.exc import SQLAlchemyError
from ..repositories.managers import ReportManager

class ReportController:
    manager = ReportManager


    @classmethod
    def get_report_per_month(cls) -> Tuple[Any, Optional[str]]:
        try:
            return cls.manager.get_report_per_month(), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)


    @classmethod
    def get_ordered_ingredients_count(cls) -> Tuple[Any, Optional[str]]:
        try:
            return cls.manager.get_ordered_ingredients_count(), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)


    @classmethod
    def get_costumers_order_count(cls) -> Tuple[Any, Optional[str]]:
        try:
            return cls.manager.get_costumers_order_count(), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)


    @classmethod
    def get_report_per_weekday(cls) -> Tuple[Any, Optional[str]]:
        try:
            return cls.manager.get_report_per_weekday(), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)


    @classmethod
    def get_report_per_hours(cls) -> Tuple[Any, Optional[str]]:
        try:
            return cls.manager.get_report_per_hours(), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)