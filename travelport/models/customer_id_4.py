from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_remark_4 import TypeRemark4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass(kw_only=True)
class CustomerId4(TypeRemark4):
    """
    A provider reservation field used to store customer information.

    It may be used to identify reservations which will/will not be
    available for access.
    """

    class Meta:
        name = "CustomerID"
        namespace = "http://www.travelport.com/schema/common_v37_0"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
