from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.mcofee_info_fee_applies_to_ind_4 import (
    McofeeInfoFeeAppliesToInd4,
)

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass
class McofeeInfo4:
    """
    Information related to the PTA/TOD (Prepaid Ticket Advice / Ticket on
    Departure) related to the MCO.

    Parameters
    ----------
    amount
        The monetary amount.
    percentage
        The percentage.
    fee_applies_to_ind
        Indicates if PTA/TOD fee is for the entire MCO or is per person.
    """

    class Meta:
        name = "MCOFeeInfo"
        namespace = "http://www.travelport.com/schema/common_v37_0"

    amount: None | str = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
        },
    )
    percentage: None | str = field(
        default=None,
        metadata={
            "name": "Percentage",
            "type": "Attribute",
            "pattern": r"([0-9]{1,2}|100)\.[0-9]{1,2}",
        },
    )
    fee_applies_to_ind: None | McofeeInfoFeeAppliesToInd4 = field(
        default=None,
        metadata={
            "name": "FeeAppliesToInd",
            "type": "Attribute",
        },
    )
