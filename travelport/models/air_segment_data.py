from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_segment_ref import AirSegmentRef
from travelport.models.baggage_allowance import BaggageAllowance
from travelport.models.brand import Brand

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirSegmentData:
    """
    The shared object list of AirsegmentData.

    Parameters
    ----------
    air_segment_ref
    baggage_allowance
    brand
    cabin_class
        Specifies Cabin class for a group of class of services. Cabin class
        is not identified if it is not present.
    class_of_service
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_segment_ref: list[AirSegmentRef] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentRef",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    baggage_allowance: list[BaggageAllowance] = field(
        default_factory=list,
        metadata={
            "name": "BaggageAllowance",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    brand: list[Brand] = field(
        default_factory=list,
        metadata={
            "name": "Brand",
            "type": "Element",
            "max_occurs": 99,
        },
    )
    cabin_class: None | str = field(
        default=None,
        metadata={
            "name": "CabinClass",
            "type": "Attribute",
        },
    )
    class_of_service: None | str = field(
        default=None,
        metadata={
            "name": "ClassOfService",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 2,
        },
    )
