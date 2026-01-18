from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from .access_mode_enumeration import AccessModeEnumeration
from .entity_in_version_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString
from .transfer_duration_structure import TransferDurationStructure
from .type_of_transfer_ref import TypeOfTransferRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TransferVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "Transfer_VersionStructure"

    name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_transfer_ref: None | TypeOfTransferRef = field(
        default=None,
        metadata={
            "name": "TypeOfTransferRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    distance: None | Decimal = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transfer_duration: None | TransferDurationStructure = field(
        default=None,
        metadata={
            "name": "TransferDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    walk_transfer_duration: None | TransferDurationStructure = field(
        default=None,
        metadata={
            "name": "WalkTransferDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    both_ways: None | bool = field(
        default=None,
        metadata={
            "name": "BothWays",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transfer_mode: None | AccessModeEnumeration = field(
        default=None,
        metadata={
            "name": "TransferMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
