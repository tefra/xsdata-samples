from dataclasses import dataclass, field
from typing import List, Optional
from npo.models.owner_type_enum import OwnerTypeEnum
from npo.models.topic_type import TopicType

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class TopicsType:
    class Meta:
        name = "topicsType"

    topic: List[TopicType] = field(
        default_factory=list,
        metadata={
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
