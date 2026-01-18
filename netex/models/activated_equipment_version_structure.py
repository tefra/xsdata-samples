from __future__ import annotations

from dataclasses import dataclass, field

from .activation_assignments_rel_structure import (
    ActivationAssignmentsRelStructure,
)
from .equipment_version_structure import EquipmentVersionStructure
from .traffic_control_point_ref import TrafficControlPointRef
from .type_of_activation_ref import TypeOfActivationRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ActivatedEquipmentVersionStructure(EquipmentVersionStructure):
    class Meta:
        name = "ActivatedEquipment_VersionStructure"

    traffic_control_point_ref: None | TrafficControlPointRef = field(
        default=None,
        metadata={
            "name": "TrafficControlPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_activation_ref: None | TypeOfActivationRef = field(
        default=None,
        metadata={
            "name": "TypeOfActivationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    assignments: None | ActivationAssignmentsRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
