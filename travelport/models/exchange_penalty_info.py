from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.penalty_information import PenaltyInformation

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class ExchangePenaltyInfo:
    """
    Parameters
    ----------
    penalty_information
    ptc
    minimum_change_fee
        Minimum change fee for changes to the itinerary.
    maximum_change_fee
        Maximum change fee for changes  to the itinerary.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    penalty_information: list[PenaltyInformation] = field(
        default_factory=list,
        metadata={
            "name": "PenaltyInformation",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    ptc: None | str = field(
        default=None,
        metadata={
            "name": "PTC",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 5,
        }
    )
    minimum_change_fee: None | str = field(
        default=None,
        metadata={
            "name": "MinimumChangeFee",
            "type": "Attribute",
        }
    )
    maximum_change_fee: None | str = field(
        default=None,
        metadata={
            "name": "MaximumChangeFee",
            "type": "Attribute",
        }
    )
