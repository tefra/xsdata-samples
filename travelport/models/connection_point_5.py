from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_location_5 import TypeLocation5

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class ConnectionPoint5(TypeLocation5):
    """
    A connection point can be eith an IATA airport or cir city code.
    """

    class Meta:
        name = "ConnectionPoint"
        namespace = "http://www.travelport.com/schema/common_v34_0"
