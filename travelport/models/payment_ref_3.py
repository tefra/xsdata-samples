from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class PaymentRef3:
    class Meta:
        name = "PaymentRef"
        namespace = "http://www.travelport.com/schema/common_v32_0"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        },
    )
