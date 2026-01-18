from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class TypeBulkTicketModifierType:
    """
    Bulk ticketing modifier type.

    Parameters
    ----------
    suppress_on_fare_calc
        Optional attribute to allow a modifier impact such as Bulk Ticketing
        to have information suppressed on the Fare Calc when generating
        supporting documents Check the specific host system which may or may
        not support this function
    """

    class Meta:
        name = "typeBulkTicketModifierType"

    suppress_on_fare_calc: None | bool = field(
        default=None,
        metadata={
            "name": "SuppressOnFareCalc",
            "type": "Attribute",
        },
    )
