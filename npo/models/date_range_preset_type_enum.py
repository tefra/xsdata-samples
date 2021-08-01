from enum import Enum

__NAMESPACE__ = "urn:vpro:api:2013"


class DateRangePresetTypeEnum(Enum):
    BEFORE_LAST_YEAR = "BEFORE_LAST_YEAR"
    LAST_YEAR = "LAST_YEAR"
    LAST_MONTH = "LAST_MONTH"
    LAST_WEEK = "LAST_WEEK"
    YESTERDAY = "YESTERDAY"
    TODAY = "TODAY"
    THIS_WEEK = "THIS_WEEK"
    TOMORROW = "TOMORROW"
