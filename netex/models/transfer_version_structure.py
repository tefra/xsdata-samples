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

    name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_transfer_ref: TypeOfTransferRef | None = field(
        default=None,
        metadata={
            "name": "TypeOfTransferRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    distance: Decimal | None = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transfer_duration: TransferDurationStructure | None = field(
        default=None,
        metadata={
            "name": "TransferDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    walk_transfer_duration: TransferDurationStructure | None = field(
        default=None,
        metadata={
            "name": "WalkTransferDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    both_ways: bool | None = field(
        default=None,
        metadata={
            "name": "BothWays",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transfer_mode: AccessModeEnumeration | None = field(
        default=None,
        metadata={
            "name": "TransferMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
