from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


class TypeFixedFieldDataFormat(StrEnum):
    """
    Data Type of the field.
    """

    STRING = "String"
    FLOAT = "Float"
    BOOLEAN = "Boolean"
    INTEGER = "Integer"
    DATE = "Date"
    MONEY = "Money"
    PERCENT = "Percent"
    REFERENCE = "Reference"
