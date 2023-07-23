from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.key_mapping_3 import KeyMapping3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class RequestKeyMappings3:
    """
    All the elements for which mapping key sent in the request is different from
    the mapping key comes in the response.
    """
    class Meta:
        name = "RequestKeyMappings"
        namespace = "http://www.travelport.com/schema/common_v33_0"

    key_mapping: list[KeyMapping3] = field(
        default_factory=list,
        metadata={
            "name": "KeyMapping",
            "type": "Element",
            "max_occurs": 999,
        }
    )
