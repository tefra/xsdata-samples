from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from xsdata.models.datatype import XmlDuration

from .accessibility_assessment import AccessibilityAssessment
from .passenger_equipment_version_structure import (
    PassengerEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class HelpPointEquipmentVersionStructure(PassengerEquipmentVersionStructure):
    class Meta:
        name = "HelpPointEquipment_VersionStructure"

    accessibility_assessment: None | AccessibilityAssessment = field(
        default=None,
        metadata={
            "name": "AccessibilityAssessment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    height_from_ground: None | Decimal = field(
        default=None,
        metadata={
            "name": "HeightFromGround",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    phone: None | bool = field(
        default=None,
        metadata={
            "name": "Phone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    induction_loop: None | bool = field(
        default=None,
        metadata={
            "name": "InductionLoop",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    induction_loop_sign: None | bool = field(
        default=None,
        metadata={
            "name": "InductionLoopSign",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    stop_request_button: None | bool = field(
        default=None,
        metadata={
            "name": "StopRequestButton",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    stop_request_timeout: None | XmlDuration = field(
        default=None,
        metadata={
            "name": "StopRequestTimeout",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
