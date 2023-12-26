from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class DirectPayment4:
    """
    Direct Payment Form of Payments.
    """

    class Meta:
        name = "DirectPayment"
        namespace = "http://www.travelport.com/schema/common_v33_0"

    text: None | str = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Attribute",
        },
    )
