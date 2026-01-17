from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_segment import AirSegment
from travelport.models.cabin_class_1 import CabinClass1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class ExchangeAirSegment:
    """
    A container to define segment and cabin class in order to process an
    exchange.

    Parameters
    ----------
    air_segment
    cabin_class
    fare_basis_code
        The fare basis code to be used for exchange of this segment.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_segment: None | AirSegment = field(
        default=None,
        metadata={
            "name": "AirSegment",
            "type": "Element",
            "required": True,
        },
    )
    cabin_class: None | CabinClass1 = field(
        default=None,
        metadata={
            "name": "CabinClass",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "required": True,
        },
    )
    fare_basis_code: None | str = field(
        default=None,
        metadata={
            "name": "FareBasisCode",
            "type": "Attribute",
        },
    )
