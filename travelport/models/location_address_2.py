from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_structured_address_3 import TypeStructuredAddress3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass(kw_only=True)
class LocationAddress2(TypeStructuredAddress3):
    class Meta:
        name = "LocationAddress"
        namespace = "http://www.travelport.com/schema/common_v32_0"
