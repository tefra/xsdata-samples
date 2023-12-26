from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass
class FareValidity:
    """
    Associates fare validity dates with journeys.

    Parameters
    ----------
    rail_journey_ref
        Reference to a journey to which this fare validity refers.
    not_valid_before
        Fare not valid before this date.
    not_valid_after
        Fare not valid after this date.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    rail_journey_ref: None | str = field(
        default=None,
        metadata={
            "name": "RailJourneyRef",
            "type": "Attribute",
            "required": True,
        },
    )
    not_valid_before: None | XmlDate = field(
        default=None,
        metadata={
            "name": "NotValidBefore",
            "type": "Attribute",
        },
    )
    not_valid_after: None | XmlDate = field(
        default=None,
        metadata={
            "name": "NotValidAfter",
            "type": "Attribute",
        },
    )
