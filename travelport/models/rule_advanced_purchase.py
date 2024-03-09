from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_stay_unit import TypeStayUnit

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class RuleAdvancedPurchase:
    """Container for rules regarding advance purchase restrictions.

    TicketingEarliestDate and TicketingLatestDate are strings
    representing respective dates. If a year component is present then
    it signifies an exact date. If only day and month components are
    present then it signifies a seasonal date, which means applicable
    for that date in any year

    Parameters
    ----------
    reservation_latest_period
    reservation_latest_unit
    ticketing_earliest_date
    ticketing_latest_date
    more_rules_present
        If true, specifies that advance purchase information will be present
        in fare rules.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    reservation_latest_period: None | str = field(
        default=None,
        metadata={
            "name": "ReservationLatestPeriod",
            "type": "Attribute",
        },
    )
    reservation_latest_unit: None | TypeStayUnit = field(
        default=None,
        metadata={
            "name": "ReservationLatestUnit",
            "type": "Attribute",
        },
    )
    ticketing_earliest_date: None | str = field(
        default=None,
        metadata={
            "name": "TicketingEarliestDate",
            "type": "Attribute",
        },
    )
    ticketing_latest_date: None | str = field(
        default=None,
        metadata={
            "name": "TicketingLatestDate",
            "type": "Attribute",
        },
    )
    more_rules_present: None | bool = field(
        default=None,
        metadata={
            "name": "MoreRulesPresent",
            "type": "Attribute",
        },
    )
