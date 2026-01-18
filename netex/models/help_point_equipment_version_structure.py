from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from xsdata.models.datatype import XmlDuration

from .accessibility_assessment import AccessibilityAssessment
from .passenger_equipment_version_structure import (
    PassengerEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class HelpPointEquipmentVersionStructure(PassengerEquipmentVersionStructure):
    class Meta:
        name = "HelpPointEquipment_VersionStructure"

    accessibility_assessment: AccessibilityAssessment | None = field(
        default=None,
        metadata={
            "name": "AccessibilityAssessment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    height_from_ground: Decimal | None = field(
        default=None,
        metadata={
            "name": "HeightFromGround",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    phone: bool | None = field(
        default=None,
        metadata={
            "name": "Phone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    induction_loop: bool | None = field(
        default=None,
        metadata={
            "name": "InductionLoop",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    induction_loop_sign: bool | None = field(
        default=None,
        metadata={
            "name": "InductionLoopSign",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    stop_request_button: bool | None = field(
        default=None,
        metadata={
            "name": "StopRequestButton",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    stop_request_timeout: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "StopRequestTimeout",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
