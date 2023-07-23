from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.host_token_5 import HostToken5

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class HostTokenList6:
    """
    The shared object list of Host Tokens.
    """
    class Meta:
        name = "HostTokenList"
        namespace = "http://www.travelport.com/schema/common_v34_0"

    host_token: list[HostToken5] = field(
        default_factory=list,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
