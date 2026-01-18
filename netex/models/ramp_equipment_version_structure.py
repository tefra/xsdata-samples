from __future__ import annotations

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

    length: None | Decimal = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_load: None | Decimal = field(
        default=None,
        metadata={
            "name": "MaximumLoad",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    gradient: None | int = field(
        default=None,
        metadata={
            "name": "Gradient",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    gradient_type: None | GradientEnumeration = field(
        default=None,
        metadata={
            "name": "GradientType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    pedestal: None | bool = field(
        default=None,
        metadata={
            "name": "Pedestal",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    handrail_type: None | HandrailEnumeration = field(
        default=None,
        metadata={
            "name": "HandrailType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    handrail_height: None | Decimal = field(
        default=None,
        metadata={
            "name": "HandrailHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    lower_handrail_height: None | Decimal = field(
        default=None,
        metadata={
            "name": "LowerHandrailHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tactile_writing: None | bool = field(
        default=None,
        metadata={
            "name": "TactileWriting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tactile_guidance_strips: None | bool = field(
        default=None,
        metadata={
            "name": "TactileGuidanceStrips",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    visual_guidance_bands: None | bool = field(
        default=None,
        metadata={
            "name": "VisualGuidanceBands",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    temporary: None | bool = field(
        default=None,
        metadata={
            "name": "Temporary",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    suitable_for_cycles: None | bool = field(
        default=None,
        metadata={
            "name": "SuitableForCycles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    rest_stop_distance: None | Decimal = field(
        default=None,
        metadata={
            "name": "RestStopDistance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    safety_edge: None | SafetyEdgeEnumeration = field(
        default=None,
        metadata={
            "name": "SafetyEdge",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    turning_space: None | RampTurningSpacePositionEnumeration = field(
        default=None,
        metadata={
            "name": "TurningSpace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
