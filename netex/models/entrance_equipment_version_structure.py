from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

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


@dataclass
class EntranceEquipmentVersionStructure(AccessEquipmentVersionStructure):
    class Meta:
        name = "EntranceEquipment_VersionStructure"

    door: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Door",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    door_orientation: Optional[CompassBearing8Enumeration] = field(
        default=None,
        metadata={
            "name": "DoorOrientation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    door_handle_outside: Optional[DoorHandleEnumeration] = field(
        default=None,
        metadata={
            "name": "DoorHandleOutside",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    door_handle_inside: Optional[DoorHandleEnumeration] = field(
        default=None,
        metadata={
            "name": "DoorHandleInside",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    kept_open: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeptOpen",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    revolving_door: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RevolvingDoor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    barrier: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Barrier",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    number_of_gates: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfGates",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    staffing: Optional[StaffingEnumeration] = field(
        default=None,
        metadata={
            "name": "Staffing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    entrance_requires_staffing: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EntranceRequiresStaffing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    entrance_requires_ticket: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EntranceRequiresTicket",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    entrance_requires_passport: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EntranceRequiresPassport",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    drop_kerb_outside: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DropKerbOutside",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    acoustic_sensor: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AcousticSensor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    automatic_door: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AutomaticDoor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    door_control_element_height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DoorControlElementHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    glass_door: Optional[bool] = field(
        default=None,
        metadata={
            "name": "GlassDoor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    airlock: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Airlock",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    wheelchair_passable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WheelchairPassable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    wheelchair_unaided: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WheelchairUnaided",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    audio_or_video_intercom: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AudioOrVideoIntercom",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    entrance_attention: Optional[EntranceAttentionEnumeration] = field(
        default=None,
        metadata={
            "name": "EntranceAttention",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    doorstep_mark: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DoorstepMark",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    necessary_force_to_open: Optional[NecessaryForceEnumeration] = field(
        default=None,
        metadata={
            "name": "NecessaryForceToOpen",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    suitable_for_cycles: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SuitableForCycles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    audio_passthrough_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AudioPassthroughIndicator",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    ramp_doorbell: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RampDoorbell",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    recognizable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Recognizable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    turning_space_position: Optional[
        EntranceTurningSpacePositionEnumeration
    ] = field(
        default=None,
        metadata={
            "name": "TurningSpacePosition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    wheelchair_turning_circle: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "WheelchairTurningCircle",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
