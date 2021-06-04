from dataclasses import dataclass, field
from typing import Optional
from netex.models.assignment_version_structure_2 import AssignmentVersionStructure2
from netex.models.scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from netex.models.transfer_constraint_type_enumeration import TransferConstraintTypeEnumeration
from netex.models.type_of_transfer_ref import TypeOfTransferRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TransferRestrictionVersionStructure(AssignmentVersionStructure2):
    class Meta:
        name = "TransferRestriction_VersionStructure"

    type_of_transfer_ref: Optional[TypeOfTransferRef] = field(
        default=None,
        metadata={
            "name": "TypeOfTransferRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    both_ways: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BothWays",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    restriction_type: Optional[TransferConstraintTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "RestrictionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    from_point_ref: Optional[ScheduledStopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "FromPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    to_point_ref: Optional[ScheduledStopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "ToPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
