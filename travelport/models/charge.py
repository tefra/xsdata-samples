from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass(kw_only=True)
class Charge:
    """
    Charge information associated to Special Equipment.

    Parameters
    ----------
    amount
        Special Equipment Charge Amount.
    rate_period
        Rate Period associated to the Special Equipment Charge Amount.e.g.
        Daily, Weekly, Rental
    included_in_est_total_ind
        Special Equipment Amount is included in the Estimated Total Amount
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    amount: str = field(
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "required": True,
        }
    )
    rate_period: str = field(
        metadata={
            "name": "RatePeriod",
            "type": "Attribute",
            "required": True,
        }
    )
    included_in_est_total_ind: bool = field(
        metadata={
            "name": "IncludedInEstTotalInd",
            "type": "Attribute",
            "required": True,
        }
    )
