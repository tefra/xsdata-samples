from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


class TypeCustomFieldDataFormat2(Enum):
    """
    Data Type of the field.
    """
    ALPHA_NUMERIC = "Alpha Numeric"
    FREEFORM_TEXT = "Freeform Text"
    TEXT = "Text"
    DECIMAL = "Decimal"
    WHOLE_NUMBER = "Whole Number"
    PERCENTAGE = "Percentage"
    TRUE_FALSE = "True/False"
    EMAIL_ADDRESS = "Email Address"
    URL = "URL"
    DATE_YEAR = "Date Year"
    DATE_MONTH_YEAR = "Date Month Year"
    DATE_DAY_MONTH_YEAR = "Date Day Month Year"
    DATE_DAY_MONTH_YEAR_TIME = "Date Day Month Year Time"
    TIME_IN_MINUTES = "Time in Minutes"
    TIME_IN_HOUR_MINUTE = "Time in Hour &amp; Minute"
    TIME_IN_MILLISECONDS_WITH_TIME_ZONE = "Time in Milliseconds with Time Zone"
