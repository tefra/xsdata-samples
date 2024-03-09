from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.other_guarantee_info_type_6 import (
    OtherGuaranteeInfoType6,
)

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class OtherGuaranteeInfo6:
    """
    Parameters
    ----------
    value
    type_value
        1) IATA/ARC Number 2) Agency Address 2) Deposit Taken 3) Others
    """

    class Meta:
        name = "OtherGuaranteeInfo"
        namespace = "http://www.travelport.com/schema/common_v38_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    type_value: None | OtherGuaranteeInfoType6 = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )
