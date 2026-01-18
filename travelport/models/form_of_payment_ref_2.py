from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass(kw_only=True)
class FormOfPaymentRef2:
    """
    A reference to a Form of Payment in the existing UR.
    """

    class Meta:
        name = "FormOfPaymentRef"
        namespace = "http://www.travelport.com/schema/common_v32_0"

    key: str = field(
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
