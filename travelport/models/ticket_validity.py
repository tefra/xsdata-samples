from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class TicketValidity:
    """
    To be used to pass the selected segment.

    Parameters
    ----------
    not_valid_before
        Fare not valid before this date.
    not_valid_after
        Fare not valid after this date.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    not_valid_before: None | XmlDate = field(
        default=None,
        metadata={
            "name": "NotValidBefore",
            "type": "Attribute",
        }
    )
    not_valid_after: None | XmlDate = field(
        default=None,
        metadata={
            "name": "NotValidAfter",
            "type": "Attribute",
        }
    )
