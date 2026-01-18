from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from .access_equipment_version_structure import AccessEquipmentVersionStructure
from .handrail_enumeration import HandrailEnumeration
from .reached_floor_announcement_enumeration import (
    ReachedFloorAnnouncementEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LiftEquipmentVersionStructure(AccessEquipmentVersionStructure):
    class Meta:
        name = "LiftEquipment_VersionStructure"

    depth: None | Decimal = field(
        default=None,
        metadata={
            "name": "Depth",
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
    wheelchair_passable: None | bool = field(
        default=None,
        metadata={
            "name": "WheelchairPassable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    wheelchair_turning_circle: None | Decimal = field(
        default=None,
        metadata={
            "name": "WheelchairTurningCircle",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    internal_width: None | Decimal = field(
        default=None,
        metadata={
            "name": "InternalWidth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    internal_height: None | Decimal = field(
        default=None,
        metadata={
            "name": "InternalHeight",
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
    call_button_height: None | Decimal = field(
        default=None,
        metadata={
            "name": "CallButtonHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    direction_button_height: None | Decimal = field(
        default=None,
        metadata={
            "name": "DirectionButtonHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    raised_buttons: None | bool = field(
        default=None,
        metadata={
            "name": "RaisedButtons",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    braille_buttons: None | bool = field(
        default=None,
        metadata={
            "name": "BrailleButtons",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tactile_ground_floor_button: None | bool = field(
        default=None,
        metadata={
            "name": "TactileGroundFloorButton",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    ground_mark_aligned_with_button: None | bool = field(
        default=None,
        metadata={
            "name": "GroundMarkAlignedWithButton",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    through_loader: None | bool = field(
        default=None,
        metadata={
            "name": "ThroughLoader",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    mirror_on_opposite_side: None | bool = field(
        default=None,
        metadata={
            "name": "MirrorOnOppositeSide",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    attendant: None | bool = field(
        default=None,
        metadata={
            "name": "Attendant",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    automatic: None | bool = field(
        default=None,
        metadata={
            "name": "Automatic",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    external_floor_selection: None | bool = field(
        default=None,
        metadata={
            "name": "ExternalFloorSelection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    alarm_button: None | bool = field(
        default=None,
        metadata={
            "name": "AlarmButton",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tactile_actuators: None | bool = field(
        default=None,
        metadata={
            "name": "TactileActuators",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    audio_announcements: None | bool = field(
        default=None,
        metadata={
            "name": "AudioAnnouncements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accoustic_announcements: None | bool = field(
        default=None,
        metadata={
            "name": "AccousticAnnouncements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    reached_floor_announcement: None | ReachedFloorAnnouncementEnumeration = (
        field(
            default=None,
            metadata={
                "name": "ReachedFloorAnnouncement",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    magnetic_induction_loop: None | bool = field(
        default=None,
        metadata={
            "name": "MagneticInductionLoop",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    signage_to_lift: None | bool = field(
        default=None,
        metadata={
            "name": "SignageToLift",
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
    buttons_height: None | Decimal = field(
        default=None,
        metadata={
            "name": "ButtonsHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
