from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_restriction_length_of_stay import (
    TypeRestrictionLengthOfStay,
)

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class RuleLengthOfStay:
    """
    Container for rules providing minimum and maximum stay requirements.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    minimum_stay: None | TypeRestrictionLengthOfStay = field(
        default=None,
        metadata={
            "name": "MinimumStay",
            "type": "Element",
        },
    )
    maximum_stay: None | TypeRestrictionLengthOfStay = field(
        default=None,
        metadata={
            "name": "MaximumStay",
            "type": "Element",
        },
    )
