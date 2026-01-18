from dataclasses import dataclass, field
from decimal import Decimal

from .access_equipment_version_structure import AccessEquipmentVersionStructure
from .gradient_enumeration import GradientEnumeration
from .handrail_enumeration import HandrailEnumeration
from .ramp_turning_space_position_enumeration import (
    RampTurningSpacePositionEnumeration,
)
from .safety_edge_enumeration import SafetyEdgeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RampEquipmentVersionStructure(AccessEquipmentVersionStructure):
    class Meta:
        name = "RampEquipment_VersionStructure"

    length: Decimal | None = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_load: Decimal | None = field(
        default=None,
        metadata={
            "name": "MaximumLoad",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    gradient: int | None = field(
        default=None,
        metadata={
            "name": "Gradient",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    gradient_type: GradientEnumeration | None = field(
        default=None,
        metadata={
            "name": "GradientType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    pedestal: bool | None = field(
        default=None,
        metadata={
            "name": "Pedestal",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    handrail_type: HandrailEnumeration | None = field(
        default=None,
        metadata={
            "name": "HandrailType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    handrail_height: Decimal | None = field(
        default=None,
        metadata={
            "name": "HandrailHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    lower_handrail_height: Decimal | None = field(
        default=None,
        metadata={
            "name": "LowerHandrailHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tactile_writing: bool | None = field(
        default=None,
        metadata={
            "name": "TactileWriting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tactile_guidance_strips: bool | None = field(
        default=None,
        metadata={
            "name": "TactileGuidanceStrips",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    visual_guidance_bands: bool | None = field(
        default=None,
        metadata={
            "name": "VisualGuidanceBands",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    temporary: bool | None = field(
        default=None,
        metadata={
            "name": "Temporary",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    suitable_for_cycles: bool | None = field(
        default=None,
        metadata={
            "name": "SuitableForCycles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    rest_stop_distance: Decimal | None = field(
        default=None,
        metadata={
            "name": "RestStopDistance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    safety_edge: SafetyEdgeEnumeration | None = field(
        default=None,
        metadata={
            "name": "SafetyEdge",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    turning_space: RampTurningSpacePositionEnumeration | None = field(
        default=None,
        metadata={
            "name": "TurningSpace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
