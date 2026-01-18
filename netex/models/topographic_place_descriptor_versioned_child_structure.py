from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .entity_in_version_structure import VersionedChildStructure
from .multilingual_string import MultilingualString
from .topographic_place_ref import TopographicPlaceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TopographicPlaceDescriptorVersionedChildStructure(
    VersionedChildStructure
):
    class Meta:
        name = "TopographicPlaceDescriptor_VersionedChildStructure"

    name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    short_name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    qualify: TopographicPlaceDescriptorVersionedChildStructure.Qualify | None = field(
        default=None,
        metadata={
            "name": "Qualify",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )

    @dataclass
    class Qualify:
        qualifier_name: MultilingualString | None = field(
            default=None,
            metadata={
                "name": "QualifierName",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "required": True,
            },
        )
        topographic_place_ref: TopographicPlaceRef | None = field(
            default=None,
            metadata={
                "name": "TopographicPlaceRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
