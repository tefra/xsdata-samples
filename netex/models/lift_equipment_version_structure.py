from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from .access_equipment_version_structure import AccessEquipmentVersionStructure
from .handrail_enumeration import HandrailEnumeration
from .reached_floor_announcement_enumeration import (
    ReachedFloorAnnouncementEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LiftEquipmentVersionStructure(AccessEquipmentVersionStructure):
    class Meta:
        name = "LiftEquipment_VersionStructure"

    depth: Decimal | None = field(
        default=None,
        metadata={
            "name": "Depth",
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
    wheelchair_passable: bool | None = field(
        default=None,
        metadata={
            "name": "WheelchairPassable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    wheelchair_turning_circle: Decimal | None = field(
        default=None,
        metadata={
            "name": "WheelchairTurningCircle",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    internal_width: Decimal | None = field(
        default=None,
        metadata={
            "name": "InternalWidth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    internal_height: Decimal | None = field(
        default=None,
        metadata={
            "name": "InternalHeight",
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
    call_button_height: Decimal | None = field(
        default=None,
        metadata={
            "name": "CallButtonHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    direction_button_height: Decimal | None = field(
        default=None,
        metadata={
            "name": "DirectionButtonHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    raised_buttons: bool | None = field(
        default=None,
        metadata={
            "name": "RaisedButtons",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    braille_buttons: bool | None = field(
        default=None,
        metadata={
            "name": "BrailleButtons",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tactile_ground_floor_button: bool | None = field(
        default=None,
        metadata={
            "name": "TactileGroundFloorButton",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    ground_mark_aligned_with_button: bool | None = field(
        default=None,
        metadata={
            "name": "GroundMarkAlignedWithButton",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    through_loader: bool | None = field(
        default=None,
        metadata={
            "name": "ThroughLoader",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    mirror_on_opposite_side: bool | None = field(
        default=None,
        metadata={
            "name": "MirrorOnOppositeSide",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    attendant: bool | None = field(
        default=None,
        metadata={
            "name": "Attendant",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    automatic: bool | None = field(
        default=None,
        metadata={
            "name": "Automatic",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    external_floor_selection: bool | None = field(
        default=None,
        metadata={
            "name": "ExternalFloorSelection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    alarm_button: bool | None = field(
        default=None,
        metadata={
            "name": "AlarmButton",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tactile_actuators: bool | None = field(
        default=None,
        metadata={
            "name": "TactileActuators",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    audio_announcements: bool | None = field(
        default=None,
        metadata={
            "name": "AudioAnnouncements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accoustic_announcements: bool | None = field(
        default=None,
        metadata={
            "name": "AccousticAnnouncements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    reached_floor_announcement: ReachedFloorAnnouncementEnumeration | None = (
        field(
            default=None,
            metadata={
                "name": "ReachedFloorAnnouncement",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    magnetic_induction_loop: bool | None = field(
        default=None,
        metadata={
            "name": "MagneticInductionLoop",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    signage_to_lift: bool | None = field(
        default=None,
        metadata={
            "name": "SignageToLift",
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
    buttons_height: Decimal | None = field(
        default=None,
        metadata={
            "name": "ButtonsHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
