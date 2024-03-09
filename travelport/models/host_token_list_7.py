from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.host_token_6 import HostToken6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class HostTokenList7:
    """
    The shared object list of Host Tokens.
    """

    class Meta:
        name = "HostTokenList"
        namespace = "http://www.travelport.com/schema/common_v38_0"

    host_token: list[HostToken6] = field(
        default_factory=list,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
