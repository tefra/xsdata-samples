from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.fare_guarantee_info import FareGuaranteeInfo
from travelport.models.type_passenger_type_1 import TypePassengerType1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class PassengerType(TypePassengerType1):
    """
    The passenger type details associated to a fare.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    fare_guarantee_info: None | FareGuaranteeInfo = field(
        default=None,
        metadata={
            "name": "FareGuaranteeInfo",
            "type": "Element",
        },
    )
