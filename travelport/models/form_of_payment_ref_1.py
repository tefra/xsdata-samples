from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class FormOfPaymentRef1:
    """
    A reference to a Form of Payment in the existing UR.
    """

    class Meta:
        name = "FormOfPaymentRef"
        namespace = "http://www.travelport.com/schema/common_v52_0"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        },
    )
