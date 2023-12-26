from dataclasses import dataclass, field
from typing import Optional
from .activated_equipment_ref_structure import ActivatedEquipmentRefStructure
from .activation_link_ref_structure import ActivationLinkRefStructure
from .activation_point_ref_structure import ActivationPointRefStructure
from .assignment_version_structure_1 import AssignmentVersionStructure1

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ActivationAssignmentVersionStructure(AssignmentVersionStructure1):
    class Meta:
        name = "ActivationAssignment_VersionStructure"

    equipment_ref: Optional[ActivatedEquipmentRefStructure] = field(
        default=None,
        metadata={
            "name": "EquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    link_ref: Optional[ActivationLinkRefStructure] = field(
        default=None,
        metadata={
            "name": "LinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    point_ref: Optional[ActivationPointRefStructure] = field(
        default=None,
        metadata={
            "name": "PointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
