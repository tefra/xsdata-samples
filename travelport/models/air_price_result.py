from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_pricing_solution import AirPricingSolution
from travelport.models.fare_rule import FareRule
from travelport.models.type_result_message_1 import TypeResultMessage1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirPriceResult:
    """A solution will be returned if one exists.

    Otherwise an error will be present

    Parameters
    ----------
    air_pricing_solution
    fare_rule
    air_price_error
    command_key
        The command identifier used when this is in response to an
        AirPricingCommand. Not used in any request processing.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_pricing_solution: list[AirPricingSolution] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingSolution",
            "type": "Element",
            "max_occurs": 99,
        },
    )
    fare_rule: list[FareRule] = field(
        default_factory=list,
        metadata={
            "name": "FareRule",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    air_price_error: None | TypeResultMessage1 = field(
        default=None,
        metadata={
            "name": "AirPriceError",
            "type": "Element",
        },
    )
    command_key: None | str = field(
        default=None,
        metadata={
            "name": "CommandKey",
            "type": "Attribute",
            "max_length": 10,
        },
    )
