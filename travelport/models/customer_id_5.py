from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_remark_5 import TypeRemark5

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class CustomerId5(TypeRemark5):
    """
    A provider reservation field used to store customer information.

    It may be used to identify reservations which will/will not be
    available for access.
    """

    class Meta:
        name = "CustomerID"
        namespace = "http://www.travelport.com/schema/common_v34_0"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
