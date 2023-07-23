from __future__ import annotations
from dataclasses import dataclass
from travelport.models.type_structured_address_6 import TypeStructuredAddress6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class LocationAddress5(TypeStructuredAddress6):
    class Meta:
        name = "LocationAddress"
        namespace = "http://www.travelport.com/schema/common_v34_0"
