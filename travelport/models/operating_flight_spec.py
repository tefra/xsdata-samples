from __future__ import annotations
from dataclasses import dataclass
from travelport.models.type_flight_spec import TypeFlightSpec

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class OperatingFlightSpec(TypeFlightSpec):
    """
    Marketing Flight number or Flight Range.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"
