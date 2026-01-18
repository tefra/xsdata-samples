from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.rate_match_indicator_status import (
    RateMatchIndicatorStatus,
)
from travelport.models.rate_match_indicator_type import RateMatchIndicatorType

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass(kw_only=True)
class RateMatchIndicator:
    """
    "Match" Indicators for certain request parameters, e.g.

    Child Count, Extra Adults etc.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    type_value: RateMatchIndicatorType = field(
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    status: RateMatchIndicatorStatus = field(
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
        }
    )
    value: None | str = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
        },
    )
