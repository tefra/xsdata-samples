from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.bag_details import BagDetails
from travelport.models.base_baggage_allowance_info import (
    BaseBaggageAllowanceInfo,
)

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class BaggageAllowanceInfo(BaseBaggageAllowanceInfo):
    """
    Information related to Baggage allowance like URL,Height,Weight etc.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    bag_details: list[BagDetails] = field(
        default_factory=list,
        metadata={
            "name": "BagDetails",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    traveler_type: None | str = field(
        default=None,
        metadata={
            "name": "TravelerType",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 5,
        },
    )
    fare_info_ref: None | str = field(
        default=None,
        metadata={
            "name": "FareInfoRef",
            "type": "Attribute",
        },
    )
