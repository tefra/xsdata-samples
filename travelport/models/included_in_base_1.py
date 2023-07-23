from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class IncludedInBase1:
    """Shows the taxes and fees included in the base fare.

    (ACH only)

    Parameters
    ----------
    amount
        this attribute shows the amount included in the base fare for the
        specific fee or tax
    """
    class Meta:
        name = "IncludedInBase"
        namespace = "http://www.travelport.com/schema/common_v52_0"

    amount: None | str = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
        }
    )
