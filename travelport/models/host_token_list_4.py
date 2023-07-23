from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.host_token_3 import HostToken3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class HostTokenList4:
    """
    The shared object list of Host Tokens.
    """
    class Meta:
        name = "HostTokenList"
        namespace = "http://www.travelport.com/schema/common_v33_0"

    host_token: list[HostToken3] = field(
        default_factory=list,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
