from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


class TypeMctConnection(StrEnum):
    """
    Enumeration of the types of MCT exceptions (domestic or international).
    """

    DD = "DD"
    DI = "DI"
    ID = "ID"
    II = "II"
