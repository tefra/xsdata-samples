from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_structured_address_4 import TypeStructuredAddress4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class LocationAddress3(TypeStructuredAddress4):
    class Meta:
        name = "LocationAddress"
        namespace = "http://www.travelport.com/schema/common_v33_0"
