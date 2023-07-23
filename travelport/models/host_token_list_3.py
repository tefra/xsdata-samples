from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.host_token_2 import HostToken2

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class HostTokenList3:
    """
    The shared object list of Host Tokens.
    """
    class Meta:
        name = "HostTokenList"
        namespace = "http://www.travelport.com/schema/common_v32_0"

    host_token: list[HostToken2] = field(
        default_factory=list,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
