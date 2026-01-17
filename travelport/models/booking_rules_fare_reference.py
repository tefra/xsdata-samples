from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class BookingRulesFareReference:
    """
    Fare Reference associated with the BookingRules.

    Containing a text container for vendor response text.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
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
    ticket_designator_code: None | str = field(
        default=None,
        metadata={
            "name": "TicketDesignatorCode",
            "type": "Attribute",
            "min_length": 0,
            "max_length": 20,
        },
    )
    account_code: None | str = field(
        default=None,
        metadata={
            "name": "AccountCode",
            "type": "Attribute",
        },
    )
    upgrage_allowed: None | bool = field(
        default=None,
        metadata={
            "name": "UpgrageAllowed",
            "type": "Attribute",
        },
    )
    upgrade_class_of_service: None | str = field(
        default=None,
        metadata={
            "name": "UpgradeClassOfService",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 2,
        },
    )
