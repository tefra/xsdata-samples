from dataclasses import dataclass, field
from typing import List, Optional
from npo.models.owner_type_enum import OwnerTypeEnum
from npo.models.target_group_enum import TargetGroupEnum

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class TargetGroupsType:
    class Meta:
        name = "targetGroupsType"

    target_group: List[TargetGroupEnum] = field(
        default_factory=list,
        metadata={
            "name": "targetGroup",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    owner: Optional[OwnerTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
