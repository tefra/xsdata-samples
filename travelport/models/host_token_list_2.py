from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.host_token_1 import HostToken1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class HostTokenList2:
    """
    The shared object list of Host Tokens.
    """
    class Meta:
        name = "HostTokenList"
        namespace = "http://www.travelport.com/schema/air_v52_0"

    host_token: list[HostToken1] = field(
        default_factory=list,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
