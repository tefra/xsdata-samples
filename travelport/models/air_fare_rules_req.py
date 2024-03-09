from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_fare_display_rule_key import AirFareDisplayRuleKey
from travelport.models.air_fare_rules_modifier import AirFareRulesModifier
from travelport.models.base_req_1 import BaseReq1
from travelport.models.fare_info_ref import FareInfoRef
from travelport.models.fare_rule_key import FareRuleKey
from travelport.models.fare_rule_lookup import FareRuleLookup
from travelport.models.type_fare_rule_type import TypeFareRuleType

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirFareRulesReq(BaseReq1):
    """
    Request to display the full text fare rules.

    Parameters
    ----------
    air_reservation_selector
        Provider: 1G,1V,1P,ACH-Parameters to use for a fare rule lookup
        associated with an Air Reservation Locator Code
    fare_rule_lookup
        Used to look up fare rules based on the origin, destination, and
        carrier of the air segment, the fare basis code and the provider
        code.  Providers: 1P.
    fare_rule_key
        Used to look up fare rules based on a fare rule key. Providers: 1G,
        1V, 1P, ACH.
    air_fare_display_rule_key
        Provider: 1G,1V,1P.
    air_fare_rules_modifier
        Provider: 1G,1V.
    fare_rules_filter_category
        Structured Fare Rules Filter if requested will return rules for
        requested categories in the response. Applicable for providers 1G,
        1V.
    fare_rule_type
        Provider: 1G,1V,1P,ACH.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_reservation_selector: None | AirFareRulesReq.AirReservationSelector = (
        field(
            default=None,
            metadata={
                "name": "AirReservationSelector",
                "type": "Element",
            },
        )
    )
    fare_rule_lookup: None | FareRuleLookup = field(
        default=None,
        metadata={
            "name": "FareRuleLookup",
            "type": "Element",
        },
    )
    fare_rule_key: list[FareRuleKey] = field(
        default_factory=list,
        metadata={
            "name": "FareRuleKey",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    air_fare_display_rule_key: None | AirFareDisplayRuleKey = field(
        default=None,
        metadata={
            "name": "AirFareDisplayRuleKey",
            "type": "Element",
        },
    )
    air_fare_rules_modifier: None | AirFareRulesModifier = field(
        default=None,
        metadata={
            "name": "AirFareRulesModifier",
            "type": "Element",
        },
    )
    fare_rules_filter_category: list[
        AirFareRulesReq.FareRulesFilterCategory
    ] = field(
        default_factory=list,
        metadata={
            "name": "FareRulesFilterCategory",
            "type": "Element",
            "max_occurs": 16,
        },
    )
    fare_rule_type: TypeFareRuleType = field(
        default=TypeFareRuleType.LONG,
        metadata={
            "name": "FareRuleType",
            "type": "Attribute",
        },
    )

    @dataclass
    class FareRulesFilterCategory:
        """
        Parameters
        ----------
        category_code
            Structured Fare Rules can be requested for "ADV", "MIN", "MAX",
            "STP", and "CHG".
        fare_info_ref
            Key reference for multiple fare rule
        """

        category_code: list[object] = field(
            default_factory=list,
            metadata={
                "name": "CategoryCode",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 35,
            },
        )
        fare_info_ref: None | str = field(
            default=None,
            metadata={
                "name": "FareInfoRef",
                "type": "Attribute",
            },
        )

    @dataclass
    class AirReservationSelector:
        """
        Parameters
        ----------
        fare_info_ref
        air_reservation_locator_code
            The Air Reservation locator code which is an unique identifier
            for the reservation
        """

        fare_info_ref: list[FareInfoRef] = field(
            default_factory=list,
            metadata={
                "name": "FareInfoRef",
                "type": "Element",
                "max_occurs": 999,
            },
        )
        air_reservation_locator_code: None | str = field(
            default=None,
            metadata={
                "name": "AirReservationLocatorCode",
                "type": "Attribute",
                "required": True,
                "min_length": 5,
                "max_length": 8,
            },
        )
