from __future__ import annotations
from dataclasses import dataclass, field
from npo.models.intention_enum import IntentionEnum
from npo.models.owner_type_enum import OwnerTypeEnum

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class IntentionType:
    class Meta:
        name = "intentionType"

    intention: list[IntentionEnum] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    owner: None | OwnerTypeEnum = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
