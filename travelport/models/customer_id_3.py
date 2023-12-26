from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_remark_3 import TypeRemark3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class CustomerId3(TypeRemark3):
    """A provider reservation field used to store customer information.

    It may be used to identify reservations which will/will not be
    available for access.
    """

    class Meta:
        name = "CustomerID"
        namespace = "http://www.travelport.com/schema/common_v33_0"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
