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

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    qualify: Optional[
        "TopographicPlaceDescriptorVersionedChildStructure.Qualify"
    ] = field(
        default=None,
        metadata={
            "name": "Qualify",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )

    @dataclass
    class Qualify:
        qualifier_name: Optional[MultilingualString] = field(
            default=None,
            metadata={
                "name": "QualifierName",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "required": True,
            },
        )
        topographic_place_ref: Optional[TopographicPlaceRef] = field(
            default=None,
            metadata={
                "name": "TopographicPlaceRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
