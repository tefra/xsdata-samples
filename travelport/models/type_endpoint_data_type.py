from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


class TypeEndpointDataType(Enum):
    """
    Specify the Data type for an Endpoint (ex, Boolean, Integer, String, etc)
    """

    STRING = "String"
    FLOAT = "Float"
    DATE = "Date"
    DATE_TIME = "DateTime"
    MONEY = "Money"
    BOOLEAN = "Boolean"
    INTEGER = "Integer"
