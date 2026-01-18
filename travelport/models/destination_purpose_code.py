from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_destination_code import TypeDestinationCode
from travelport.models.type_purpose_code import TypePurposeCode

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class DestinationPurposeCode:
    """
    This code is required to indicate destination and purpose of Travel.

    It is applicable for Canada and Bermuda agency only. This is used by
    Worldspan.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    destination: TypeDestinationCode = field(
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "required": True,
        }
    )
    purpose: TypePurposeCode = field(
        metadata={
            "name": "Purpose",
            "type": "Attribute",
            "required": True,
        }
    )
