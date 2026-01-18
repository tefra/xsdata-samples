from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_location_6 import TypeLocation6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass(kw_only=True)
class ConnectionPoint6(TypeLocation6):
    """
    A connection point can be eith an IATA airport or cir city code.
    """

    class Meta:
        name = "ConnectionPoint"
        namespace = "http://www.travelport.com/schema/common_v38_0"
