from dataclasses import dataclass, field
from typing import Optional

from .assignment_version_structure_1 import AssignmentVersionStructure1
from .scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from .transfer_constraint_type_enumeration import (
    TransferConstraintTypeEnumeration,
)
from .type_of_transfer_ref import TypeOfTransferRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TransferRestrictionVersionStructure(AssignmentVersionStructure1):
    class Meta:
        name = "TransferRestriction_VersionStructure"

    type_of_transfer_ref: TypeOfTransferRef | None = field(
        default=None,
        metadata={
            "name": "TypeOfTransferRef",
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
    restriction_type: TransferConstraintTypeEnumeration | None = field(
        default=None,
        metadata={
            "name": "RestrictionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    from_point_ref: ScheduledStopPointRefStructure | None = field(
        default=None,
        metadata={
            "name": "FromPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    to_point_ref: ScheduledStopPointRefStructure | None = field(
        default=None,
        metadata={
            "name": "ToPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
