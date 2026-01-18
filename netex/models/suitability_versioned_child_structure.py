from __future__ import annotations

from dataclasses import dataclass, field

from .suitable_enumeration import SuitableEnumeration
from .user_need_versioned_child_structure import (
    UserNeedVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SuitabilityVersionedChildStructure(UserNeedVersionedChildStructure):
    class Meta:
        name = "Suitability_VersionedChildStructure"

    suitable: None | SuitableEnumeration = field(
        default=None,
        metadata={
            "name": "Suitable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
