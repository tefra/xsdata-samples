from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from .access_equipment_version_structure import AccessEquipmentVersionStructure
from .handrail_enumeration import HandrailEnumeration
from .stair_end_structure import StairEndStructure
from .stair_ramp_enumeration import StairRampEnumeration
from .step_condition_enumeration import StepConditionEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StairEquipmentVersionStructure(AccessEquipmentVersionStructure):
    class Meta:
        name = "StairEquipment_VersionStructure"

    depth: Decimal | None = field(
        default=None,
        metadata={
            "name": "Depth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    number_of_steps: int | None = field(
        default=None,
        metadata={
            "name": "NumberOfSteps",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    step_height: Decimal | None = field(
        default=None,
        metadata={
            "name": "StepHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    step_length: Decimal | None = field(
        default=None,
        metadata={
            "name": "StepLength",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    step_colour_contrast: bool | None = field(
        default=None,
        metadata={
            "name": "StepColourContrast",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    step_condition: StepConditionEnumeration | None = field(
        default=None,
        metadata={
            "name": "StepCondition",
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
    stair_ramp: StairRampEnumeration | None = field(
        default=None,
        metadata={
            "name": "StairRamp",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    top_end: StairEndStructure | None = field(
        default=None,
        metadata={
            "name": "TopEnd",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    bottom_end: StairEndStructure | None = field(
        default=None,
        metadata={
            "name": "BottomEnd",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
