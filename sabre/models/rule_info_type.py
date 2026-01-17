from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.adv_res_ticketing_type import AdvResTicketingType
from sabre.models.stay_restrictions_type import StayRestrictionsType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class RuleInfoType:
    """
    Contains summary fare rule information as well as detailed Rule
    Information for Fare Basis Codes.

    Information may be actual rules data or the results returned from a
    rules-based inquiry.

    Attributes:
        res_ticketing_rules: General container for rules regarding fare
            reservation,  ticketing and sale restrictions
        length_of_stay_rules: Rules providing minimum or maximum stay
            restrictions.
    """

    res_ticketing_rules: None | RuleInfoType.ResTicketingRules = field(
        default=None,
        metadata={
            "name": "ResTicketingRules",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    length_of_stay_rules: None | StayRestrictionsType = field(
        default=None,
        metadata={
            "name": "LengthOfStayRules",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )

    @dataclass
    class ResTicketingRules:
        """
        Attributes:
            adv_res_ticketing: Container for holding rules regarding
                advance reservation or ticketing restrictions.
        """

        adv_res_ticketing: None | AdvResTicketingType = field(
            default=None,
            metadata={
                "name": "AdvResTicketing",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
