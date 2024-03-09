from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_structured_address_1 import TypeStructuredAddress1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class LocationAddress1(TypeStructuredAddress1):
    class Meta:
        name = "LocationAddress"
        namespace = "http://www.travelport.com/schema/common_v52_0"
