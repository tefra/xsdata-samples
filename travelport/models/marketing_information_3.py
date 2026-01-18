from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass(kw_only=True)
class MarketingInformation3:
    """
    Marketing text or Notices for Suppliers.
    """

    class Meta:
        name = "MarketingInformation"
        namespace = "http://www.travelport.com/schema/common_v33_0"

    text: list[object] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
