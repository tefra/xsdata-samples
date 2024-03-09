from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_structured_address_5 import TypeStructuredAddress5

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass
class LocationAddress4(TypeStructuredAddress5):
    class Meta:
        name = "LocationAddress"
        namespace = "http://www.travelport.com/schema/common_v37_0"
