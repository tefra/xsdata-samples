from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


class TypeMctConnection(Enum):
    """
    Enumeration of the types of MCT exceptions (domestic or international)
    """
    DD = "DD"
    DI = "DI"
    ID = "ID"
    II = "II"
