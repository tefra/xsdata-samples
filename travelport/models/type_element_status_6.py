from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


class TypeElementStatus6(Enum):
    """Values to specify the state of the element.

    "A" refers to "Add" , "M" refers to "Modified" and "C" refers to
    error conditions when value provided in "Key" attribute is not
    retained in response
    """

    A = "A"
    M = "M"
    C = "C"