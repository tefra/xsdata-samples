from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


class TypeFuel(Enum):
    PETROL = "Petrol"
    DIESEL = "Diesel"
    HYBRID = "Hybrid"
    ELECTRIC = "Electric"
    LPGCNG = "LPGCNG"
    HYDROGEN = "Hydrogen"
    MULTI_FUEL = "MultiFuel"
    ETHANOL = "Ethanol"
