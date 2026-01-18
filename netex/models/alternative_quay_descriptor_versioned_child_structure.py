from dataclasses import dataclass, field
from typing import Optional

from .alternative_name_versioned_child_structure import (
    AlternativeNameVersionedChildStructure,
)
from .multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AlternativeQuayDescriptorVersionedChildStructure(
    AlternativeNameVersionedChildStructure
):
    class Meta:
        name = "AlternativeQuayDescriptor_VersionedChildStructure"

    cross_road: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "CrossRoad",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    landmark: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Landmark",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
