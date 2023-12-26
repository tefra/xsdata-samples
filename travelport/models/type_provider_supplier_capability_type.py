from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


class TypeProviderSupplierCapabilityType(Enum):
    """
    Enumeration of ProviderSupplier capability.
    """

    YES = "Yes"
    NO = "No"
    PARTIAL = "Partial"
