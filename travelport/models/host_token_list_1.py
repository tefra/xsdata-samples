from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.host_token_1 import HostToken1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass(kw_only=True)
class HostTokenList1:
    """
    The shared object list of Host Tokens.
    """

    class Meta:
        name = "HostTokenList"
        namespace = "http://www.travelport.com/schema/common_v52_0"

    host_token: list[HostToken1] = field(
        default_factory=list,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
