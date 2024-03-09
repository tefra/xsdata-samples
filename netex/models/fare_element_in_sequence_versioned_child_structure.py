from dataclasses import dataclass, field
from typing import Optional
from .entity_in_version_structure import VersionedChildStructure
from .multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareElementInSequenceVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "FareElementInSequence_VersionedChildStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    is_first_in_sequence: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsFirstInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    is_last_in_sequence: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsLastInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    access_number_is_limited: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AccessNumberIsLimited",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_access: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinimumAccess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_access: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumAccess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    access_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "AccessNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
