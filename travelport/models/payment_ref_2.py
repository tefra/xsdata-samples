from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class PaymentRef2:
    """
    Reference to one of the air reservation payments.
    """

    class Meta:
        name = "PaymentRef"
        namespace = "http://www.travelport.com/schema/air_v52_0"

    key: str = field(
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
