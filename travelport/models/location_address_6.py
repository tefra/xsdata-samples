from __future__ import annotations
from dataclasses import dataclass
from travelport.models.type_structured_address_7 import TypeStructuredAddress7

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class LocationAddress6(TypeStructuredAddress7):
    class Meta:
        name = "LocationAddress"
        namespace = "http://www.travelport.com/schema/common_v38_0"
