from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from .access_equipment_version_structure import AccessEquipmentVersionStructure
from .compass_bearing8_enumeration import CompassBearing8Enumeration
from .door_handle_enumeration import DoorHandleEnumeration
from .entrance_attention_enumeration import EntranceAttentionEnumeration
from .entrance_turning_space_position_enumeration import (
    EntranceTurningSpacePositionEnumeration,
)
from .necessary_force_enumeration import NecessaryForceEnumeration
from .staffing_enumeration import StaffingEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EntranceEquipmentVersionStructure(AccessEquipmentVersionStructure):
    class Meta:
        name = "EntranceEquipment_VersionStructure"

    door: None | bool = field(
        default=None,
        metadata={
            "name": "Door",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    door_orientation: None | CompassBearing8Enumeration = field(
        default=None,
        metadata={
            "name": "DoorOrientation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    door_handle_outside: None | DoorHandleEnumeration = field(
        default=None,
        metadata={
            "name": "DoorHandleOutside",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    door_handle_inside: None | DoorHandleEnumeration = field(
        default=None,
        metadata={
            "name": "DoorHandleInside",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    kept_open: None | bool = field(
        default=None,
        metadata={
            "name": "KeptOpen",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    revolving_door: None | bool = field(
        default=None,
        metadata={
            "name": "RevolvingDoor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    barrier: None | bool = field(
        default=None,
        metadata={
            "name": "Barrier",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    number_of_gates: None | int = field(
        default=None,
        metadata={
            "name": "NumberOfGates",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    staffing: None | StaffingEnumeration = field(
        default=None,
        metadata={
            "name": "Staffing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    entrance_requires_staffing: None | bool = field(
        default=None,
        metadata={
            "name": "EntranceRequiresStaffing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    entrance_requires_ticket: None | bool = field(
        default=None,
        metadata={
            "name": "EntranceRequiresTicket",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    entrance_requires_passport: None | bool = field(
        default=None,
        metadata={
            "name": "EntranceRequiresPassport",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    drop_kerb_outside: None | bool = field(
        default=None,
        metadata={
            "name": "DropKerbOutside",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    acoustic_sensor: None | bool = field(
        default=None,
        metadata={
            "name": "AcousticSensor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    automatic_door: None | bool = field(
        default=None,
        metadata={
            "name": "AutomaticDoor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    door_control_element_height: None | Decimal = field(
        default=None,
        metadata={
            "name": "DoorControlElementHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    glass_door: None | bool = field(
        default=None,
        metadata={
            "name": "GlassDoor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    airlock: None | bool = field(
        default=None,
        metadata={
            "name": "Airlock",
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
    wheelchair_unaided: None | bool = field(
        default=None,
        metadata={
            "name": "WheelchairUnaided",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    audio_or_video_intercom: None | bool = field(
        default=None,
        metadata={
            "name": "AudioOrVideoIntercom",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    entrance_attention: None | EntranceAttentionEnumeration = field(
        default=None,
        metadata={
            "name": "EntranceAttention",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    doorstep_mark: None | bool = field(
        default=None,
        metadata={
            "name": "DoorstepMark",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    necessary_force_to_open: None | NecessaryForceEnumeration = field(
        default=None,
        metadata={
            "name": "NecessaryForceToOpen",
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
    audio_passthrough_indicator: None | bool = field(
        default=None,
        metadata={
            "name": "AudioPassthroughIndicator",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    ramp_doorbell: None | bool = field(
        default=None,
        metadata={
            "name": "RampDoorbell",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    recognizable: None | bool = field(
        default=None,
        metadata={
            "name": "Recognizable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    turning_space_position: None | EntranceTurningSpacePositionEnumeration = (
        field(
            default=None,
            metadata={
                "name": "TurningSpacePosition",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    wheelchair_turning_circle: None | Decimal = field(
        default=None,
        metadata={
            "name": "WheelchairTurningCircle",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
