from dataclasses import dataclass, field
from typing import List
from npo.models.group import Group

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class GroupTableType:
    class Meta:
        name = "groupTableType"

    group: List[Group] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "min_occurs": 1,
        }
    )
