from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from netex.models.access_equipment_version_structure import AccessEquipmentVersionStructure
from netex.models.handrail_enumeration import HandrailEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LiftEquipmentVersionStructure(AccessEquipmentVersionStructure):
    class Meta:
        name = "LiftEquipment_VersionStructure"

    depth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Depth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_load: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumLoad",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    wheelchair_passable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WheelchairPassable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    wheelchair_turning_circle: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "WheelchairTurningCircle",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    internal_width: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "InternalWidth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    handrail_type: Optional[HandrailEnumeration] = field(
        default=None,
        metadata={
            "name": "HandrailType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    handrail_height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "HandrailHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    lower_handrail_height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "LowerHandrailHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    call_button_height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CallButtonHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    direction_button_height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DirectionButtonHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    raised_buttons: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RaisedButtons",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    braille_buttons: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BrailleButtons",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tactile_ground_floor_button: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TactileGroundFloorButton",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    ground_mark_aligned_with_button: Optional[bool] = field(
        default=None,
        metadata={
            "name": "GroundMarkAlignedWithButton",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    through_loader: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ThroughLoader",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    mirror_on_opposite_side: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MirrorOnOppositeSide",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    attendant: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Attendant",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    automatic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Automatic",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    external_floor_selection: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ExternalFloorSelection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    alarm_button: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AlarmButton",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tactile_actuators: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TactileActuators",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    audio_announcements: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AudioAnnouncements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    accoustic_announcements: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AccousticAnnouncements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    magnetic_induction_loop: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MagneticInductionLoop",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    signage_to_lift: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SignageToLift",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    suitable_for_cycles: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SuitableForCycles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
